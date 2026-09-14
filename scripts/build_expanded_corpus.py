#!/usr/bin/env python3
"""Build the official-venue expansion used by the static paper map.

Input pages are downloaded from the official proceedings sites to /private/tmp.
The title filter is deliberately conservative: direct hallucination papers must
name both hallucination and a visual/multimodal model in the title.  A small,
audited ICML list is retained as adjacent faithfulness/reliability work.
"""

from __future__ import annotations

import html
import json
import re
import unicodedata
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "dist/index.html"
OUT = ROOT / "dist/expanded-corpus.js"


def norm(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def clean(value: str) -> str:
    return " ".join(html.unescape(re.sub(r"<[^>]+>", "", value)).split())


VISUAL_TERMS = (
    "vision-language", "vision language", "multimodal", "multi-modal", "mllm",
    "lvlm", "videollm", "video llm", "video large language", "audio-visual",
    "visual hallucination", "image token", "cross-modal", "gui grounding",
    "mlrm", "3d-llm",
)


def is_direct(title: str) -> bool:
    low = title.lower()
    return "hallucin" in low and any(term in low for term in VISUAL_TERMS)


class ProceedingsParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.active = False
        self.href = ""
        self.buf: list[str] = []
        self.rows: list[tuple[str, str]] = []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == "a" and data.get("title") == "paper title":
            self.active = True
            self.href = data.get("href", "")
            self.buf = []

    def handle_data(self, data):
        if self.active:
            self.buf.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self.active:
            self.rows.append((" ".join("".join(self.buf).split()), self.href))
            self.active = False


class CVFParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.in_title = False
        self.active = False
        self.href = ""
        self.buf: list[str] = []
        self.rows: list[tuple[str, str]] = []

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        if tag == "dt" and "ptitle" in data.get("class", "").split():
            self.in_title = True
        if tag == "a" and self.in_title:
            self.active = True
            self.href = data.get("href", "")
            self.buf = []

    def handle_data(self, data):
        if self.active:
            self.buf.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self.active:
            self.rows.append((" ".join("".join(self.buf).split()), self.href))
            self.active = False
        if tag == "dt":
            self.in_title = False


class ICMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.active = False
        self.href = ""
        self.buf: list[str] = []
        self.rows: list[tuple[str, str]] = []

    def handle_starttag(self, tag, attrs):
        href = dict(attrs).get("href", "")
        if tag == "a" and "/virtual/2026/poster/" in href:
            self.active = True
            self.href = href
            self.buf = []

    def handle_data(self, data):
        if self.active:
            self.buf.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self.active:
            self.rows.append((" ".join("".join(self.buf).split()), self.href))
            self.active = False


RELATED_ICML = {
    "Bad Seeing or Bad Thinking? Rewarding Perception for Multimodal Reasoning",
    "Decomposed On-Policy Distillation for Vision-Language Reasoning: Steering Gradients for Visual Grounding",
    "DeFacto: Counterfactual Thinking with Images for Enforcing Evidence-Grounded and Faithful Reasoning",
    "Dismantling Pathological Shortcuts: A Causal Framework for Faithful LVLM Decoding",
    "Does Reasoning Improve Seeing? Understanding When Vision-Language Models Benefit from Thinking",
    "Do Vision and Text Cues Exhibit Evidential Coupling? UFO: A Benchmark for Compositional Multimodal Reasoning in Unified Models",
    "Focusing Where Vision Matters: Selective Training for Large Vision Language Models via Visual Information Gain",
    "From Blind Spots to Gains: Diagnostic-Driven Iterative Training for Large Multimodal Models",
    "From Seeing to Thinking: Decoupling Perception and Reasoning Improves Post-Training of Vision-Language Models",
    "FUSE: Quantifying Uncertainty in Vision-Language Models by Bayesian Fusing Epistemic and Aleatoric Uncertainty",
    "Look on Demand: A Cognitive Scheduling Framework for Visual Evidence Acquisition in Multimodal Reasoning",
    "MVI-Bench: A Comprehensive Benchmark for Evaluating Robustness to Misleading Visual Inputs in LVLMs",
    "PerceptionRubrics: Calibrating Multimodal Evaluation to Human Perception",
    "Risk Awareness Injection: Calibrating Vision-Language Models for Safety without Compromising Utility",
    "The Abstraction Gap in Vision-Language Causal Reasoning",
    "The Art of Interrogation: Consistency Amplifies Factuality in Spatial Reasoning",
    "The Geometry of Representational Failures in Vision Language Models",
    "The Perceptual Bandwidth Bottleneck in Vision-Language Models: Active Visual Reasoning via Sequential Experimental Design",
    "Unveiling the Visual Counting Bottleneck in Vision-Language Models",
    "Vision Language Models Cannot Reason About Physical Transformation",
    "Visual Persuasion: What Influences Decisions of Vision-Language Models?",
    "VLM-RobustBench: A Comprehensive Benchmark for Robustness of Vision-Language Models",
    "ZeroBench: An Impossible Visual Benchmark for Contemporary Large Multimodal Models",
}


EXCLUDE = (
    "3d generation", "3d content generation", "image restoration", "deepfake",
    "text-to-image synthesis", "hallucination-inducing image generation",
    "controlled visual hallucination via thalamus", "sign language translation",
)


def role_for(title: str) -> str:
    low = title.lower()
    evaluation = any(x in low for x in (
        "evaluat", "benchmark", "detect", "assess", "discover", "understanding",
        "why ", "study", "analysis", "uncertainty", "revealing", "exposing",
        "localization", "know what they know", "fails to",
    ))
    mitigation = any(x in low for x in (
        "mitigat", "reduc", "alleviat", "combat", "suppress", "steering",
        "decoding", "intervention", "optimization", "editing", "training",
        "grounding", "reinforcement", "self-reflection", "reallocation",
    ))
    if evaluation and mitigation:
        return "评价与检测；缓解方法"
    return "缓解方法" if mitigation else "评价与检测"


def method_for(title: str) -> str:
    if ":" in title:
        return title.split(":", 1)[0].strip()[:54]
    words = title.split()
    return " ".join(words[:5])[:54]


def zh_title(title: str) -> str:
    pairs = (
        ("Large Vision-Language Models", "大型视觉语言模型"),
        ("Large Vision Language Models", "大型视觉语言模型"),
        ("Vision-Language Models", "视觉语言模型"),
        ("Vision Language Models", "视觉语言模型"),
        ("Multimodal Large Language Models", "多模态大语言模型"),
        ("Multi-modal Large Language Models", "多模态大语言模型"),
        ("Large Multi-Modal Models", "大型多模态模型"),
        ("Large Multimodal Models", "大型多模态模型"),
        ("Hallucination Mitigation", "幻觉缓解"),
        ("Hallucinations", "幻觉"),
        ("Hallucination", "幻觉"),
        ("Evaluating", "评估"),
        ("Evaluation", "评测"),
        ("Benchmarking", "基准评测"),
        ("Benchmark", "基准"),
        ("Detecting", "检测"),
        ("Detection", "检测"),
        ("Mitigating", "缓解"),
        ("Reducing", "减少"),
        ("Alleviating", "缓解"),
        ("Understanding", "理解"),
        ("Visual", "视觉"),
        ("Multimodal", "多模态"),
        ("Object", "对象"),
        ("Reasoning", "推理"),
        ("Attention", "注意力"),
        ("Grounding", "接地"),
        ("Faithful", "忠实"),
        ("Uncertainty", "不确定性"),
        (" via ", "：通过"),
        (" through ", "：通过"),
        (" for ", "：面向"),
        (" in ", "：在"),
    )
    out = title
    for source, target in pairs:
        out = out.replace(source, target)
    return out


def guide_for(title: str, label: str, scope: str) -> str:
    if scope == "Related":
        return "该论文研究视觉证据、感知失真、推理忠实性或不确定性，与多模态幻觉的成因和评测直接相邻；本站将其标为“相关研究”，不计作题名明确的核心幻觉论文。"
    if "评价" in label and "缓解" in label:
        return "该论文同时分析或评测多模态幻觉，并提出相应的检测或缓解方案；具体实验设置、数据集和数值结论以官方摘要与论文正文为准。"
    if "缓解" in label:
        return "该论文提出针对视觉/多模态生成幻觉的缓解方法，重点减少输出中缺乏输入视觉证据支持的内容；方法细节和实验结论以官方论文为准。"
    return "该论文聚焦视觉或多模态模型幻觉的定义、评测、检测或机制分析，并通过官方论文所述基准与实验刻画模型输出和视觉证据之间的不一致。"


def add(rows, seen, title, url, venue, year, scope="Core"):
    title = " ".join(title.split()).strip(" .")
    if not title or norm(title) in seen:
        return
    if any(term in title.lower() for term in EXCLUDE):
        return
    label = role_for(title)
    rows.append({
        "year": year,
        "method": method_for(title),
        "title": title,
        "url": url,
        "venue": venue,
        "label": label,
        "scope": scope,
        "zhTitle": zh_title(title),
        "zhAbstract": guide_for(title, label, scope),
    })
    seen.add(norm(title))


def main() -> None:
    # Deduplicate within this official expansion only.  Do not drop an official
    # record merely because an older arXiv/preprint version is already present;
    # the browser's normalized-title merge deliberately lets the official row
    # replace that preprint row.
    seen: set[str] = set()
    rows: list[dict] = []

    # ICML 2026 official poster directory.
    path = Path("/private/tmp/icml2026.html")
    if path.exists():
        parser = ICMLParser(); parser.feed(path.read_text(errors="ignore"))
        for title, href in parser.rows:
            if is_direct(title):
                add(rows, seen, title, "https://icml.cc" + href, "ICML 2026", 2026)
            elif title in RELATED_ICML:
                add(rows, seen, title, "https://icml.cc" + href, "ICML 2026", 2026, "Related")

    # ICLR and NeurIPS official proceedings indexes.
    for path in sorted(Path("/private/tmp").glob("iclr20*.html")) + sorted(Path("/private/tmp").glob("neurips20*.html")):
        if path.name == "neurips2025.html":
            continue
        match = re.search(r"(20\d{2})", path.name)
        if not match:
            continue
        year = int(match.group(1))
        venue = ("ICLR" if path.name.startswith("iclr") else "NeurIPS") + f" {year}"
        base = "https://proceedings.iclr.cc" if venue.startswith("ICLR") else "https://proceedings.neurips.cc"
        parser = ProceedingsParser(); parser.feed(path.read_text(errors="ignore"))
        for title, href in parser.rows:
            if is_direct(title):
                add(rows, seen, title, base + href, venue, year)

    # CVPR and ICCV official CVF Open Access indexes.
    for path in sorted(Path("/private/tmp").glob("cvpr20*.html")) + sorted(Path("/private/tmp").glob("iccv20*.html")):
        match = re.search(r"(20\d{2})", path.name)
        if not match:
            continue
        year = int(match.group(1))
        venue = ("CVPR" if path.name.startswith("cvpr") else "ICCV") + f" {year}"
        parser = CVFParser(); parser.feed(path.read_text(errors="ignore"))
        for title, href in parser.rows:
            if is_direct(title):
                add(rows, seen, title, "https://openaccess.thecvf.com" + href, venue, year)

    # ECCV official ECVA index (currently relevant 2024 entries).
    path = Path("/private/tmp/eccv-index.html")
    if path.exists():
        parser = CVFParser(); parser.feed(path.read_text(errors="ignore"))
        for title, href in parser.rows:
            if "eccv_2024" in href.lower() and is_direct(title):
                add(rows, seen, title, "https://www.ecva.net/" + href, "ECCV 2024", 2024)

    # ACL Anthology event pages for EMNLP/NAACL. Title-level matching avoids
    # pulling in papers that merely mention hallucination in related work.
    pattern = re.compile(r'<strong><a[^>]+href=/?([^/ >]+)/(?:[^>]*)>(.*?)</a></strong>', re.S)
    for path in sorted(Path("/private/tmp").glob("emnlp20*.html")) + sorted(Path("/private/tmp").glob("naacl20*.html")):
        match = re.search(r"(20\d{2})", path.name)
        if not match:
            continue
        year = int(match.group(1))
        family = "EMNLP" if path.name.startswith("emnlp") else "NAACL"
        for paper_id, raw_title in pattern.findall(path.read_text(errors="ignore")):
            title = clean(raw_title)
            if is_direct(title):
                venue = family + (" Findings" if "findings" in paper_id else "") + f" {year}"
                add(rows, seen, title, f"https://aclanthology.org/{paper_id}/", venue, year)

    # Additional AAAI papers verified on the official OJS article pages.
    manual = [
        (2026, "Adaptive Hallucination Alleviation in Multimodal Large Language Models: From Strategic Data Selection to Severity-Guided Training", "https://ojs.aaai.org/index.php/AAAI/article/view/39955"),
        (2026, "InEx: Hallucination Mitigation via Introspection and Cross-Modal Multi-Agent Collaboration", "https://ojs.aaai.org/index.php/AAAI/article/view/40229"),
        (2026, "Verb Mirage: Unveiling and Assessing Verb Concept Hallucinations in Multimodal Large Language Models", "https://ojs.aaai.org/index.php/AAAI/article/view/38005"),
        (2026, "OmniDPO: A Preference Optimization Framework to Address Omni-Modal Hallucination", "https://ojs.aaai.org/index.php/AAAI/article/view/39104"),
        (2026, "Multi-Agent Undercover Gaming: Hallucination Removal Through Counterfactual Test for Multimodal Reasoning", "https://ojs.aaai.org/index.php/AAAI/article/view/37613"),
        (2025, "ConVis: Contrastive Decoding with Hallucination Visualization for Mitigating Hallucinations in Multimodal Large Language Models", "https://ojs.aaai.org/index.php/AAAI/article/view/32689"),
        (2025, "MoLE: Decoding by Mixture of Layer Experts Alleviates Hallucination in Large Vision-Language Models", "https://ojs.aaai.org/index.php/AAAI/article/view/34056"),
        (2025, "MHBench: Demystifying Motion Hallucination in VideoLLMs", "https://ojs.aaai.org/index.php/AAAI/article/view/32463"),
    ]
    for year, title, url in manual:
        add(rows, seen, title, url, f"AAAI {year}", year)

    # IJCV currently has adjacent LVLM reliability work but no title-explicit
    # core hallucination paper in the audited 2023-2026 results.
    add(rows, seen,
        "Structural Pruning of Large Vision Language Models: A Comprehensive Study on Pruning Dynamics, Recovery, and Data Efficiency",
        "https://link.springer.com/article/10.1007/s11263-026-02865-5", "IJCV 2026", 2026, "Related")
    add(rows, seen,
        "Near OOD Detection for Vision-Language Prompt Learning with Contrastive Logit Score",
        "https://link.springer.com/article/10.1007/s11263-026-02760-z", "IJCV 2026", 2026, "Related")
    add(rows, seen,
        "HiLM-D: Enhancing MLLMs with Multi-scale High-Resolution Details for Autonomous Driving",
        "https://link.springer.com/article/10.1007/s11263-025-02433-3", "IJCV 2025", 2025, "Related")

    # WWW has few title-explicit LVLM hallucination papers in the audited main
    # proceedings; retain closely related multimodal truth/fact-checking work.
    add(rows, seen,
        "Navigating Truth in Multimodal Fact-checking via Retrieval- and Reasoning-Enhanced Large Language Models",
        "https://doi.org/10.1145/3774904.3792706", "WWW 2026", 2026, "Related")
    add(rows, seen,
        "LPEdit: Locality-Preserving Knowledge Editing for MultiModal Large Language Models",
        "https://www2026.thewebconf.org/program/full-schedule.html", "WWW 2026", 2026, "Related")

    rows.sort(key=lambda item: (-item["year"], item["venue"], item["title"]))
    for index, row in enumerate(rows, 1):
        row["id"] = f"X{index:03d}"
    OUT.write_text("window.EXPANDED_CORPUS = " + json.dumps(rows, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")

    counts: dict[str, int] = {}
    for row in rows:
        key = row["venue"].split()[0]
        counts[key] = counts.get(key, 0) + 1
    print(json.dumps({"added": len(rows), "byVenue": counts}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
