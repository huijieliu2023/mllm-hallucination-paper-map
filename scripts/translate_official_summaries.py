#!/usr/bin/env python3
"""Translate source-grounded title/abstract excerpts for the static paper map.

Only records carrying an official abstract receive a translated abstract. The
cache records provenance so the UI can distinguish translated abstracts from
short topic summaries used when no abstract was available in the proceedings
index.
"""

from __future__ import annotations

import concurrent.futures
import json
import os
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = Path("/private/tmp/mllm-translation-source.json")
CACHE = ROOT / "data/zh-summaries.json"
ENDPOINT = "https://translate.googleapis.com/translate_a/single"
MICROSOFT_AUTH = "https://edge.microsoft.com/translate/auth"
MICROSOFT_ENDPOINT = "https://api-edge.cognitive.microsofttranslator.com/translate"
SENTINEL = "ZXQSECTIONBREAKZXQ"
OFFLINE = os.getenv("MLLM_OFFLINE_TRANSLATION") == "1"
MICROSOFT = os.getenv("MLLM_MICROSOFT_TRANSLATION") == "1"
BING = os.getenv("MLLM_BING_TRANSLATION") == "1"
CT2 = os.getenv("MLLM_CT2_TRANSLATION") == "1"
REFRESH = os.getenv("MLLM_REFRESH_TRANSLATIONS") == "1"

CURATED_OVERRIDES = {
    "Faithful-First Reasoning, Planning, and Acting for Multimodal LLMs": {
        "zhTitle": "面向多模态大语言模型的忠实性优先推理、规划与行动",
        "zhAbstract": "多模态大语言模型生成的推理链可能偏离视觉证据，或与最终预测相矛盾。论文提出忠实性优先的 RPA 框架：FaithEvi 在步骤与推理链两个层级评估中间推理的忠实性，FaithAct 据此规划并执行面向忠实性的推理动作。多项多模态推理基准上的实验显示，该框架在不降低任务准确率的情况下提升了感知忠实性，并减少幻觉行为。",
    },
    "SPD-Faith Bench: Diagnosing and Improving Faithfulness in Chain-of-Thought for Multimodal Large Language Models": {
        "zhTitle": "SPD-Faith Bench：诊断并提升多模态大语言模型思维链的忠实性",
        "zhAbstract": "论文关注多模态思维链是否忠实于视觉证据，而不只关注最终答案是否正确。作者提出 SPD-Faith Bench，通过细粒度图像差异推理削弱语言先验，并识别出感知盲区和感知—推理解耦两类系统性失效；在此基础上又提出无需训练的 SAGE，以视觉证据校准改善视觉信息路由，使推理过程与感知结果更加一致。",
    },
    "VisuLogic: A Benchmark for Evaluating Visual Reasoning in Multi-modal Large Language Models": {
        "zhTitle": "VisuLogic：评估多模态大语言模型视觉推理能力的基准",
        "zhAbstract": "现有多模态推理评测常把图像转写为文本，模型可能借助语言捷径作答，因而不能充分衡量真正的视觉推理。VisuLogic 收录 1,000 道经人工核验的问题，覆盖数量变化、空间关系和属性比较等六类任务。对主流模型的评测显示，多数模型的准确率低于 30%，仅略高于 25% 的随机水平，并明显低于人类表现。",
    },
    "Pelican: Correcting Hallucination in Vision-LLMs via Claim Decomposition and Program of Thought Verification": {
        "zhTitle": "Pelican：通过声明分解与思维程序验证纠正 Vision-LLM 幻觉",
        "zhAbstract": "Pelican 将视觉声明分解为由一阶谓词构成的子声明链，再以思维程序提示生成 Python 代码，组合外部工具回答相应问题。框架通过中间变量精确定位对象实例，并共享子问题计算以发现不一致、执行自适应纠正，最后依据各子声明问答对的一致性与置信度验证原声明。论文在多个基准上报告了相对基线模型和既有幻觉缓解方法的持续改进。",
    },
    "FREAK: A Fine-grained Hallucination Evaluation Benchmark for Advanced MLLMs": {
        "zhTitle": "FREAK：面向先进多模态大语言模型的细粒度幻觉评测基准",
        "zhAbstract": "FREAK 针对现有幻觉基准任务过于简单、指标趋于饱和和样本多样性不足的问题，使用具有细粒度反常识编辑的高质量逼真图像，评估多模态大语言模型在细节视觉感知中的幻觉现象。",
    },
    "Look Carefully: Adaptive Visual Reinforcements in Multimodal Large Language Models for Hallucination Mitigation": {
        "zhTitle": "仔细看：用于缓解多模态大语言模型幻觉的自适应视觉增强",
        "zhAbstract": "论文提出 AIR：先用基于原型的 token 压缩减少冗余视觉 token，再依据最优传输估计隐藏状态与图像块表示的一致性，将最相关的图像块选择性注入前馈层。该方法旨在不增加训练监督的情况下增强模型对关键视觉信息的依赖，并在多种多模态模型上降低幻觉、保持通用能力。",
    },
}


def select_excerpt(abstract: str) -> str:
    abstract = " ".join(abstract.split())
    if not abstract:
        return ""
    sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z])", abstract)
    selected: list[str] = []
    for index in (0,):
        if index < len(sentences):
            selected.append(sentences[index])
    for cues in (
        ("we propose", "we introduce", "we present", "this paper proposes", "our method"),
        ("experiment", "results", "outperform", "achieve", "evaluation shows", "we find"),
    ):
        match = next((s for s in sentences if any(cue in s.lower() for cue in cues)), "")
        if match and match not in selected:
            selected.append(match)
    if len(selected) < 3:
        for sentence in sentences[1:]:
            if sentence not in selected:
                selected.append(sentence)
            if len(selected) == 3:
                break
    return " ".join(selected)[:1400]


def translate(text: str) -> str:
    if OFFLINE:
        from argostranslate.translate import translate as argos_translate
        return argos_translate(text, "en", "zh").strip()
    query = urllib.parse.urlencode({
        "client": "gtx", "sl": "en", "tl": "zh-CN", "dt": "t", "q": text,
    })
    request = urllib.request.Request(
        f"{ENDPOINT}?{query}", headers={"User-Agent": "Mozilla/5.0"}
    )
    for attempt in range(4):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = json.loads(response.read().decode("utf-8"))
            return "".join(chunk[0] for chunk in payload[0] if chunk and chunk[0]).strip()
        except Exception:
            if attempt == 3:
                raise
            time.sleep(1.2 * (attempt + 1))
    return ""


def microsoft_token() -> str:
    request = urllib.request.Request(
        MICROSOFT_AUTH, headers={"User-Agent": "Mozilla/5.0"}
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8").strip()


def microsoft_translate_batch(texts: list[str], token: str) -> list[str]:
    query = urllib.parse.urlencode({
        "api-version": "3.0", "from": "en", "to": "zh-Hans",
    })
    payload = json.dumps([{"Text": value} for value in texts]).encode("utf-8")
    request = urllib.request.Request(
        f"{MICROSOFT_ENDPOINT}?{query}",
        data=payload,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        result = json.loads(response.read().decode("utf-8"))
    return [item["translations"][0]["text"].strip() for item in result]


def bing_session():
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor())
    request = urllib.request.Request(
        "https://www.bing.com/translator", headers={"User-Agent": "Mozilla/5.0"}
    )
    with opener.open(request, timeout=30) as response:
        page = response.read().decode("utf-8", errors="replace")
        base_url = response.geturl()[:-10]
    ig = re.search(r'(?:IG|"ig")[:=]"([^"]+)"', page)
    iids = re.findall(r'data-iid="([^"]+)"', page)
    abuse = re.search(r'params_AbusePreventionHelper\s*=\s*\[(\d+),"([^"]+)"', page)
    if not ig or not abuse or not iids:
        raise RuntimeError("Could not initialize Bing Translator session")
    return opener, base_url, ig.group(1), iids[-1], abuse.group(1), abuse.group(2)


def bing_translate(text: str, session) -> str:
    opener, base_url, ig, iid, key, token = session
    url = f"{base_url}ttranslatev3?isVertical=1&IG={ig}&IID={iid}"
    payload = urllib.parse.urlencode({
        "fromLang": "en", "to": "zh-Hans", "text": text,
        "key": key, "token": token, "tryFetchingGenderDebiasedTranslations": "true",
    }).encode("utf-8")
    request = urllib.request.Request(
        url, data=payload,
        headers={"User-Agent": "Mozilla/5.0", "Content-Type": "application/x-www-form-urlencoded"},
        method="POST",
    )
    with opener.open(request, timeout=45) as response:
        result = json.loads(response.read().decode("utf-8"))
    return result[0]["translations"][0]["text"].strip()


def polish(text: str) -> str:
    replacements = {
        "多式联运大语言模型": "多模态大语言模型",
        "多种形式大语文模式": "多模态大语言模型",
        "多种形式大语言模式": "多模态大语言模型",
        "多模式大型语言模型": "多模态大语言模型",
        "多模式大语言模型": "多模态大语言模型",
        "多模态大语言模式": "多模态大语言模型",
        "多式大型语言模型": "多模态大语言模型",
        "多式大语言模型": "多模态大语言模型",
        "多式语言模型": "多模态语言模型",
        "多式理由": "多模态推理",
        "多模态过程报酬模式": "多模态过程奖励模型",
        "多式联运模式": "多模态模型",
        "多式联运": "多模态",
        "多种形式": "多模态",
        "大视觉语言模型": "大型视觉语言模型",
        "大型视觉语言模式": "大型视觉语言模型",
        "大型视觉-语言模型": "大型视觉语言模型",
        "视觉-语言模式": "视觉语言模型",
        "视觉-语言模型": "视觉语言模型",
        "视觉语言模式": "视觉语言模型",
        "视野-语言模型": "视觉语言模型",
        "视野语言模型": "视觉语言模型",
        "愿景语言模型": "视觉语言模型",
        "大型视野语言模型": "大型视觉语言模型",
        "大视野语言模型": "大型视觉语言模型",
        "大语言模式": "大语言模型",
        "大型语言模式": "大型语言模型",
        "语文模式": "语言模型",
        "有限责任公司": "大语言模型",
        "视觉理由": "视觉推理",
        "空间理由": "空间推理",
        "因果理由": "因果推理",
        "符号理由": "符号推理",
        "多模态理由": "多模态推理",
        "对精益视野的思考": "细粒度视觉推理",
        "培训-自由": "无需训练",
        "培训自由": "无需训练",
        "索赔核查": "声明验证",
        "索赔分解": "声明分解",
        "索赔": "声明",
        "视觉教学": "视觉指令",
        "与幻觉斗争": "存在幻觉问题",
        "语言学前科": "语言先验",
        "语言前科": "语言先验",
        "语言前缀": "语言先验",
        "培训时间": "训练阶段",
        "精细调图": "微调",
        "视觉地面": "视觉接地",
        "地基视野语言模型": "基于几何接地的视觉语言模型",
        "跨摩达尔": "跨模态",
        "多代理": "多智能体",
        "通过透视": "通过内省",
        "标题反馈": "图像描述反馈",
        "多样性-智能取样": "多样性感知采样",
        "冲突规范化": "冲突正则化",
        "后向视觉定位": "反向视觉接地",
        "丰富文字幻觉": "丰富上下文幻觉",
        "动词概念幻象": "动词概念幻觉",
        "解冻和评估": "揭示并评估",
        "消除对多模态的迷幻": "消除多模态推理中的幻觉",
        "远景-语言模型": "视觉语言模型",
        "远景与语言": "视觉与语言",
        "优化优惠": "偏好优化",
        "优惠学习": "偏好学习",
        "认知忠诚度": "感知忠实性",
        "忠于第一": "忠实性优先",
        "忠实-第一": "忠实性优先",
        "爱国军": "RPA",
        "低消费量": "LVLM",
        "幻觉作用": "幻觉现象",
        "幻觉行为": "幻觉输出",
        "忠诚度": "忠实性",
        "托肯": "token",
        "培训": "训练",
        "业绩": "性能",
        "对策": "回答",
        "超理性控制器": "元推理控制器",
        "每一代人中": "每个生成步骤中",
        "感知-回光": "感知—推理",
        "Gated 感知": "门控感知",
        "愿景": "视觉",
        "远景": "视觉",
        "多式": "多模态",
        "多模式": "多模态",
        "跨模式": "跨模态",
        "理由说明": "推理",
        "合理理由": "推理",
        "理由链": "推理链",
        "理性链": "推理链",
        "理由": "推理",
        "最佳化": "优化",
        "优惠": "偏好",
        "精确度": "准确率",
        "概括能力": "泛化能力",
        "可概括性": "泛化能力",
        "图象": "图像",
        "察觉": "感知",
        "幻象": "幻觉",
        "幻听": "幻觉",
        "致幻作用": "幻觉",
        "反竞争": "对比",
        "互换代谢": "对比解码",
        "违反标记": "对比解码",
        "解码标记": "解码",
        "代号": "token",
        "发电质量": "生成质量",
        "发电": "生成",
        "地基": "接地",
        "四环": "接地",
        "校对学习": "对齐学习",
        "协调": "对齐",
        "型号": "模型",
        "视听": "音视频",
        "可信赖": "可信",
        "内审": "内省",
        "多机构": "多智能体",
        "低LLLM": "MLLM",
        "低LLM": "MLLM",
        "MLLLM": "MLLM",
        "MLMLMM": "MLLM",
        "LLLM": "LVLM",
        "LTLM": "LVLM",
        "甚低LM": "VLM",
        "最低生活水平标准": "LVLM",
        "最低运作安保标准": "MLLM",
        "最低运作标准": "MLLM",
        "我们提议": "我们提出",
        "本文提议": "本文提出",
        "作者提议": "作者提出",
        "吵闹": "含噪",
        "基准困难": "基准难度",
        "无形任务": "未见任务",
        "附加说明": "标注",
        "精神模拟": "心理模拟",
        "消亡点": "消失点",
        "产权模型": "专有模型",
        "体现人工智能": "具身人工智能",
        "基因化多模态": "生成式多模态",
        "基因数据强化": "生成式数据增强",
        "插座和游戏": "即插即用",
        "插接和插接": "即插即用",
        "插插和玩": "即插即用",
        "自惯性": "自一致性",
        "图像蒙面": "图像掩码",
        "面具": "掩码",
        "优度优度": "去偏优化",
        "分辨理由": "溯因推理",
        "组合推理": "组合推理",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    return re.sub(r"\s+", " ", text).strip()


def acceptable_translation(translated: str, source: str) -> bool:
    if not translated:
        return False
    if len(translated) > max(1800, int(len(source) * 2.2)):
        return False
    if re.search(r"(.{1,12})\1{5,}", translated):
        return False
    if re.search(r"拉夫拉|地中海低排|女士|有限责任公司|爱国军|高射程|引爆|自动递减|\\text|\$\d|⁇", translated):
        return False
    return True


def restore_method_prefix(title: str, translated: str) -> str:
    if ":" not in title:
        return translated
    prefix, _ = title.split(":", 1)
    if len(prefix) <= 32:
        translated_tail = translated.split(":", 1)[-1].split("：", 1)[-1].strip()
        return f"{prefix}：{translated_tail}"
    return translated


def translate_record(record: dict) -> tuple[str, dict]:
    title = record["title"]
    excerpt = select_excerpt(record.get("abstract", ""))
    if OFFLINE:
        zh_title = restore_method_prefix(title, polish(translate(title)))
        zh_abstract = polish(translate(excerpt)) if excerpt else ""
    else:
        combined = title if not excerpt else f"{title}\n{SENTINEL}\n{excerpt}"
        result = translate(combined)
        if excerpt:
            parts = re.split(rf"\s*{SENTINEL}\s*", result, maxsplit=1, flags=re.I)
            if len(parts) == 1:
                parts = result.split("\n", 1)
            zh_title = restore_method_prefix(title, polish(parts[0]))
            zh_abstract = polish(parts[1]) if len(parts) > 1 else ""
        else:
            zh_title, zh_abstract = restore_method_prefix(title, polish(result)), ""
    return title, {
        "zhTitle": zh_title,
        "zhAbstract": zh_abstract,
        "source": "official-abstract-machine-translation" if zh_abstract else "title-machine-translation",
        "officialUrl": record.get("url", ""),
    }


def microsoft_translate_records(records: list[dict]) -> dict[str, dict]:
    token = microsoft_token()
    translated: dict[str, dict] = {}
    batches: list[list[dict]] = []
    batch: list[dict] = []
    chars = 0
    for record in records:
        excerpt = select_excerpt(record.get("abstract", ""))
        combined = record["title"] if not excerpt else f'{record["title"]}\n{SENTINEL}\n{excerpt}'
        if batch and (len(batch) >= 50 or chars + len(combined) > 45000):
            batches.append(batch)
            batch, chars = [], 0
        enriched = dict(record)
        enriched["_combined"] = combined
        enriched["_has_abstract"] = bool(excerpt)
        batch.append(enriched)
        chars += len(combined)
    if batch:
        batches.append(batch)

    for index, items in enumerate(batches, 1):
        for attempt in range(4):
            try:
                results = microsoft_translate_batch([item["_combined"] for item in items], token)
                break
            except Exception:
                if attempt == 3:
                    raise
                time.sleep(2 * (attempt + 1))
                token = microsoft_token()
        for item, result in zip(items, results):
            title = item["title"]
            if item["_has_abstract"]:
                parts = re.split(rf"\s*{SENTINEL}\s*", result, maxsplit=1, flags=re.I)
                if len(parts) == 1:
                    parts = result.split("\n", 1)
                zh_title = restore_method_prefix(title, polish(parts[0]))
                zh_abstract = polish(parts[1]) if len(parts) > 1 else ""
            else:
                zh_title = restore_method_prefix(title, polish(result))
                zh_abstract = ""
            translated[title] = {
                "zhTitle": zh_title,
                "zhAbstract": zh_abstract,
                "source": "official-abstract-machine-translation" if zh_abstract else "title-machine-translation",
                "officialUrl": item.get("url", ""),
            }
        print(f"translated batch {index}/{len(batches)}")
    return translated


def bing_translate_records(records: list[dict]) -> dict[str, dict]:
    session = bing_session()
    translated: dict[str, dict] = {}
    for index, record in enumerate(records, 1):
        title = record["title"]
        excerpt = select_excerpt(record.get("abstract", ""))
        combined = title if not excerpt else f"{title}\n{SENTINEL}\n{excerpt}"
        for attempt in range(4):
            try:
                result = bing_translate(combined, session)
                break
            except Exception:
                if attempt == 3:
                    raise
                time.sleep(1.5 * (attempt + 1))
                session = bing_session()
        if excerpt:
            parts = re.split(rf"\s*{SENTINEL}\s*", result, maxsplit=1, flags=re.I)
            if len(parts) == 1:
                parts = result.split("\n", 1)
            zh_title = restore_method_prefix(title, polish(parts[0]))
            zh_abstract = polish(parts[1]) if len(parts) > 1 else ""
        else:
            zh_title = restore_method_prefix(title, polish(result))
            zh_abstract = ""
        translated[title] = {
            "zhTitle": zh_title,
            "zhAbstract": zh_abstract,
            "source": "official-abstract-machine-translation" if zh_abstract else "title-machine-translation",
            "officialUrl": record.get("url", ""),
        }
        if index % 50 == 0:
            print(f"translated {index}/{len(records)}")
    return translated


def ct2_translate_records(records: list[dict]) -> dict[str, dict]:
    import ctranslate2
    import sentencepiece as spm

    model_dir = Path(os.getenv("MLLM_CT2_MODEL", "/private/tmp/opus-mt-en-zh-ct2"))
    source_sp = spm.SentencePieceProcessor(model_file=str(model_dir / "source.spm"))
    target_sp = spm.SentencePieceProcessor(model_file=str(model_dir / "target.spm"))
    translator = ctranslate2.Translator(str(model_dir), device="cpu", compute_type="int8")

    jobs: list[tuple[str, str, int]] = []
    record_parts: dict[str, list[str]] = {}
    for record in records:
        title = record["title"]
        excerpt = select_excerpt(record.get("abstract", ""))
        parts = [title]
        if excerpt:
            parts.extend(re.split(r"(?<=[.!?])\s+", excerpt))
        record_parts[title] = parts
        for index, part in enumerate(parts):
            jobs.append((title, part, index))

    translated_parts: dict[str, list[str]] = {
        title: [""] * len(parts) for title, parts in record_parts.items()
    }
    for start in range(0, len(jobs), 32):
        chunk = jobs[start:start + 32]
        source_tokens = [source_sp.encode(part, out_type=str) + ["</s>"] for _, part, _ in chunk]
        results = translator.translate_batch(
            source_tokens, beam_size=4, max_decoding_length=512,
        )
        for (title, _, part_index), result in zip(chunk, results):
            translated_parts[title][part_index] = target_sp.decode(result.hypotheses[0])
        if (start // 32 + 1) % 10 == 0:
            print(f"translated {min(start + 32, len(jobs))}/{len(jobs)} segments")

    translated: dict[str, dict] = {}
    records_by_title = {record["title"]: record for record in records}
    for title, parts in translated_parts.items():
        zh_title = restore_method_prefix(title, polish(parts[0]))
        zh_abstract = polish(" ".join(parts[1:])) if len(parts) > 1 else ""
        if not acceptable_translation(zh_title, title):
            zh_title = ""
        excerpt = select_excerpt(records_by_title[title].get("abstract", ""))
        if zh_abstract and not acceptable_translation(zh_abstract, excerpt):
            zh_abstract = ""
        translated[title] = {
            "zhTitle": zh_title,
            "zhAbstract": zh_abstract,
            "source": "official-abstract-machine-translation" if zh_abstract else "title-machine-translation",
            "officialUrl": records_by_title[title].get("url", ""),
        }
    return translated


def main() -> None:
    records = json.loads(SOURCE.read_text())
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    cache = json.loads(CACHE.read_text()) if CACHE.exists() and not REFRESH else {}
    records_by_title = {record["title"]: record for record in records}
    if os.getenv("MLLM_PRUNE_TRANSLATIONS") == "1":
        cache = {title: value for title, value in cache.items() if title in records_by_title}
    for title, value in cache.items():
        value["zhTitle"] = restore_method_prefix(title, polish(value.get("zhTitle", "")))
        value["zhAbstract"] = polish(value.get("zhAbstract", ""))
        record = records_by_title.get(title, {})
        excerpt = select_excerpt(record.get("abstract", ""))
        if value["zhTitle"] and not acceptable_translation(value["zhTitle"], title):
            value["zhTitle"] = ""
        if value["zhAbstract"] and not acceptable_translation(value["zhAbstract"], excerpt):
            value["zhAbstract"] = ""
    for title, value in CURATED_OVERRIDES.items():
        if title in records_by_title:
            cache.setdefault(title, {}).update(value)
            cache[title]["source"] = "official-abstract-curated-translation"
            cache[title]["officialUrl"] = records_by_title[title].get("url", "")
    pending = [record for record in records if record["title"] not in cache]
    if os.getenv("MLLM_SKIP_PENDING_TRANSLATIONS") == "1":
        pending = []
    print(json.dumps({"records": len(records), "cached": len(cache), "pending": len(pending)}, ensure_ascii=False))
    if MICROSOFT:
        cache.update(microsoft_translate_records(pending))
        for title, value in CURATED_OVERRIDES.items():
            if title in records_by_title:
                cache.setdefault(title, {}).update(value)
                cache[title]["source"] = "official-abstract-curated-translation"
                cache[title]["officialUrl"] = records_by_title[title].get("url", "")
        CACHE.write_text(json.dumps(dict(sorted(cache.items())), ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({"saved": len(cache), "withAbstract": sum(bool(v.get("zhAbstract")) for v in cache.values())}, ensure_ascii=False))
        return
    if BING:
        cache.update(bing_translate_records(pending))
        for title, value in CURATED_OVERRIDES.items():
            if title in records_by_title:
                cache.setdefault(title, {}).update(value)
                cache[title]["source"] = "official-abstract-curated-translation"
                cache[title]["officialUrl"] = records_by_title[title].get("url", "")
        CACHE.write_text(json.dumps(dict(sorted(cache.items())), ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({"saved": len(cache), "withAbstract": sum(bool(v.get("zhAbstract")) for v in cache.values())}, ensure_ascii=False))
        return
    if CT2:
        cache.update(ct2_translate_records(pending))
        for title, value in CURATED_OVERRIDES.items():
            if title in records_by_title:
                cache.setdefault(title, {}).update(value)
                cache[title]["source"] = "official-abstract-curated-translation"
                cache[title]["officialUrl"] = records_by_title[title].get("url", "")
        CACHE.write_text(json.dumps(dict(sorted(cache.items())), ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps({"saved": len(cache), "withAbstract": sum(bool(v.get("zhAbstract")) for v in cache.values())}, ensure_ascii=False))
        return
    with concurrent.futures.ThreadPoolExecutor(max_workers=4 if OFFLINE else 10) as executor:
        futures = {executor.submit(translate_record, record): record["title"] for record in pending}
        for index, future in enumerate(concurrent.futures.as_completed(futures), 1):
            title, value = future.result()
            cache[title] = value
            if index % 50 == 0:
                CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=2), encoding="utf-8")
                print(f"translated {index}/{len(pending)}")
    CACHE.write_text(json.dumps(dict(sorted(cache.items())), ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({"saved": len(cache), "withAbstract": sum(bool(v.get("zhAbstract")) for v in cache.values())}, ensure_ascii=False))


if __name__ == "__main__":
    main()
