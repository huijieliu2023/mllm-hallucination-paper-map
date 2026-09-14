#!/usr/bin/env python3
"""Build the official-venue expansion used by the static paper map.

Input pages are downloaded from the official proceedings sites to /private/tmp.
The scanner uses title plus official abstract text when the directory exposes
abstracts (ACL Anthology), and a strict title-based rule otherwise.  Direct
hallucination work and adjacent faithfulness/reliability work stay visibly
separated in the generated corpus.
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
    "vision-language", "vision language", "visual language", "multimodal",
    "multi-modal", "mllm", "lvlm", "vlm", "videollm", "video llm",
    "video large language", "audio-visual", "audio visual", "visual",
    "image", "cross-modal", "cross modal", "gui", "caption", "ocr",
    "object hallucination", "relationship hallucination", "relation hallucination",
    "spatial hallucination", "temporal hallucination", "motion hallucination",
    "scene hallucination", "3d-llm",
)

# Strong title-level cues.  These intentionally exclude the bare word "image":
# in an abstract it is too easy for a text-only hallucination paper to mention
# an illustrative image or an image-domain comparison in passing.
VISUAL_TITLE_TERMS = (
    "vision-language", "vision language", "visual language", "multimodal",
    "multi-modal", "mllm", "lvlm", "vlm", "videollm", "video llm",
    "video large language", "video language model", "audio-visual", "audio visual", "visual hallucination",
    "image caption", "captioning", "object hallucination", "relationship hallucination",
    "relation hallucination", "spatial hallucination", "motion hallucination",
    "scene hallucination", "document vqa", "ocr",
)

ABSTRACT_VISUAL_CUES = (
    "vision-language", "vision language", "large vision-language",
    "large vision language", "multimodal large language",
    "multi-modal large language", "large multimodal model",
    "large multi-modal model", "visual input", "visual evidence",
    "visual grounding", "image input", "image caption", "captioning",
    "video llm", "video language", "audio-visual", "cross-modal",
    "cross modal", "document vqa",
)

MODEL_TERMS = (
    "vision-language model", "vision language model", "visual language model",
    "large vision-language", "large vision language", "multimodal large language",
    "multi-modal large language", "large multimodal model", "large multi-modal model",
    "mllm", "lvlm", "video llm", "videollm", "video language model", "audio-visual large language",
    "vision) language model", "image-text generation", "interleaved image",
    "document vqa",
)

RELATED_CUES = (
    "faithful", "faithfulness", "factual", "factuality", "fact-check",
    "visual evidence", "visual grounding", "image grounding", "image-grounded",
    "evidence-grounded", "grounded reasoning", "perceptual faithfulness",
    "reasoning faithfulness", "perception and reasoning", "perception-reasoning",
    "misleading visual", "visual uncertainty", "epistemic uncertainty",
    "calibrating vision-language", "calibration of vision-language",
    "calibrated vision-language", "trustworthy vision-language",
    "reasoning limitations of multimodal", "reasoning improve seeing",
    "visual information gain", "visual information steering",
    "representational failures in vision", "visual counting bottleneck",
    "perceptual bandwidth bottleneck", "visual persuasion",
)


def is_direct(title: str, abstract: str = "") -> bool:
    title_low = title.lower()
    if "hallucin" in title_low:
        return title_is_visual(title)
    return False


def title_is_visual(title: str) -> bool:
    title_low = title.lower()
    visual_in_title = any(term in title_low for term in VISUAL_TITLE_TERMS)
    acronym_in_title = bool(re.search(r"\b(?:mllms?|lvlms?|vlms?)\b", title_low))
    # MLLM is also used for "multilingual LLM" in NLP papers.
    if "multilingual" in title_low and not visual_in_title:
        acronym_in_title = False
    return bool(visual_in_title or acronym_in_title or re.search(r"\bgui\b", title_low))


def is_abstract_core(title: str, abstract: str = "") -> bool:
    """Hallucination is a repeated subject in an official LVLM/VLM abstract."""
    abstract_low = abstract.lower()
    return (
        abstract_low.count("hallucin") >= 2
        and any(term in abstract_low for term in MODEL_TERMS)
        and any(term in abstract_low for term in ABSTRACT_VISUAL_CUES)
    )


def is_abstract_related(title: str, abstract: str = "") -> bool:
    """Conservative fallback for event pages outside the detail-page audit."""
    title_low = title.lower()
    abstract_low = abstract.lower()
    return (
        abstract_low.count("hallucin") >= 2
        and any(term in abstract_low for term in MODEL_TERMS)
        and any(term in abstract_low for term in ABSTRACT_VISUAL_CUES)
        and any(term in title_low for term in (
            "vision", "visual", "image", "multimodal", "multi-modal", "mllm",
            "lvlm", "vlm", "video", "caption", "ground", "factual", "evidence",
            "alignment", "calibration", "attention",
        ))
    )


def scope_for_detail_page(title: str, abstract: str = "") -> str | None:
    """Richer rule used only for audited CVPR/ICLR/NeurIPS detail pages."""
    if is_direct(title, abstract):
        return "Core"
    abstract_low = abstract.lower()
    if is_related(title) or is_abstract_core(title, abstract) or (
        "hallucin" in abstract_low
        and title_is_visual(title)
        and any(term in abstract_low for term in MODEL_TERMS)
        and any(term in abstract_low for term in ABSTRACT_VISUAL_CUES)
    ):
        return "Related"
    return None


def is_related(title: str) -> bool:
    low = title.lower()
    return any(term in low for term in MODEL_TERMS) and any(
        cue in low for cue in RELATED_CUES
    )


def scope_for(title: str, abstract: str = "") -> str | None:
    if is_direct(title, abstract):
        return "Core"
    if is_related(title) or is_abstract_related(title, abstract):
        return "Related"
    return None


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
        if tag == "a" and re.search(r"/virtual/20\d{2}/poster/", href):
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


def pmlr_rows(text: str) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    pattern = re.compile(
        r'<div class="paper">.*?<p class="title">(.*?)</p>.*?'
        r'<p class="links">\s*\[<a href="([^"]+\.html)">abs</a>',
        re.S,
    )
    for raw_title, href in pattern.findall(text):
        rows.append((clean(raw_title), href))
    return rows


def anthology_rows(text: str, year: int, family: str) -> list[tuple[str, str, str, bool]]:
    """Return official ACL-family paper id, title, abstract, and Findings flag."""
    pattern = re.compile(
        r'<strong><a[^>]+href=/?([^/" >]+)/(?:[^>]*)>(.*?)</a></strong>',
        re.S,
    )
    matches = list(pattern.finditer(text))
    rows: list[tuple[str, str, str, bool]] = []
    family_low = family.lower()
    accepted_prefixes = (f"{year}.{family_low}-", f"{year}.findings-{family_low}.")
    for index, match in enumerate(matches):
        paper_id = match.group(1)
        if not paper_id.startswith(accepted_prefixes):
            continue
        title = clean(match.group(2))
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        segment = text[match.end():end]
        abstract_match = re.search(
            r'class="card-body p-3 small">(.*?)</div></div>', segment, re.S
        )
        abstract = clean(abstract_match.group(1)) if abstract_match else ""
        rows.append((paper_id, title, abstract, f"findings-{family_low}" in paper_id))
    return rows


RELATED_ICML_BY_YEAR = {
2023: {
    "ILLUME: Rationalizing Vision-Language Models through Human Interactions",
    "Grounding Language Models to Images for Multimodal Inputs and Outputs",
    "Calibrating Multimodal Learning",
    "Retrieval-Augmented Multimodal Language Modeling",
},
2024: {
    "MLLM-as-a-Judge: Assessing Multimodal LLM-as-a-Judge with Vision-Language Benchmark",
    "GeoReasoner: Geo-localization with Reasoning in Street Views using a Large Vision-Language Model",
    "Revisiting the Role of Language Priors in Vision-Language Models",
    "An Empirical Study Into What Matters for Calibrating Vision-Language Models",
    "ConTextual: Evaluating Context-Sensitive Text-Rich Visual Reasoning in Large Multimodal Models",
    "Diagnosing the Compositional Knowledge of Vision Language Models from a Game-Theoretic View",
    "MMT-Bench: A Comprehensive Multimodal Benchmark for Evaluating Large Vision-Language Models Towards Multitask AGI",
    "MM-Vet: Evaluating Large Multimodal Models for Integrated Capabilities",
},
2025: {
    "DEFAME: Dynamic Evidence-based FAct-checking with Multimodal Experts",
    "Can MLLMs Reason in Multimodality? EMMA: An Enhanced MultiModal ReAsoning Benchmark",
    "Do Vision-Language Models Really Understand Visual Language?",
    "MME-CoT: Benchmarking Chain-of-Thought in Large Multimodal Models for Reasoning Quality, Robustness, and Efficiency",
    "Toward Robust Hyper-Detailed Image Captioning: A Multiagent Approach and Dual Evaluation Metrics for Factuality and Coverage",
    "Core Knowledge Deficits in Multi-Modal Language Models",
    "Reasoning Limitations of Multimodal Large Language Models. A case study of Bongard Problems",
    "Generalizing from SIMPLE to HARD Visual Reasoning: Can We Mitigate Modality Imbalance in VLMs?",
    "Towards Rationale-Answer Alignment of LVLMs via Self-Rationale Calibration",
    "Re-ranking Reasoning Context with Tree Search Makes Large Vision-Language Models Stronger",
    "Robust Multimodal Large Language Models Against Modality Conflict",
},
2026: {
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
},
}


# Audited adjacent work from the same complete official proceedings indexes.
# These papers test perceptual evidence use, compositional failures, confidence,
# calibration, or reasoning faithfulness without necessarily using the word
# "hallucination" in the title or abstract.
RELATED_OFFICIAL_BY_VENUE_YEAR = {
    ("CVPR", 2023): {
        "CREPE: Can Vision-Language Foundation Models Reason Compositionally?",
        "Exploring the Effect of Primitives for Compositional Generalization in Vision-and-Language",
        "Improving Visual Grounding by Encouraging Consistent Gradient-Based Explanations",
        "MAP: Multimodal Uncertainty-Aware Vision-Language Pre-Training Model",
        "ViLEM: Visual-Language Error Modeling for Image-Text Retrieval",
        "Visual Programming: Compositional Visual Reasoning Without Training",
    },
    ("CVPR", 2024): {
        "Compositional Chain-of-Thought Prompting for Large Multimodal Models",
        "Consistency and Uncertainty: Identifying Unreliable Responses From Black-Box Vision-Language Models for Selective Visual Question Answering",
        "Grounding Everything: Emerging Localization Properties in Vision-Language Transformers",
        "Improved Visual Grounding through Self-Consistent Explanations",
        "Iterated Learning Improves Compositionality in Large Vision-Language Models",
    },
    ("CVPR", 2025): {
        "Can Large Vision-Language Models Correct Semantic Grounding Errors By Themselves?",
        "CoSpace: Benchmarking Continuous Space Perception Ability for Vision-Language Models",
        "Critic-V: VLM Critics Help Catch VLM Errors in Multimodal Reasoning",
        "DART: Disease-aware Image-Text Alignment and Self-correcting Re-alignment for Trustworthy Radiology Report Generation",
        "Debiasing Multimodal Large Language Models via Noise-Aware Preference Optimization",
        "Enhancing Vision-Language Compositional Understanding with Multimodal Synthetic Data",
        "Identifying and Mitigating Position Bias of Multi-image Vision-Language Models",
        "O-TPT: Orthogonality Constraints for Calibrating Test-time Prompt Tuning in Vision-Language Models",
        "Perception Tokens Enhance Visual Reasoning in Multimodal Language Models",
        "VELOCITI: Benchmarking Video-Language Compositional Reasoning with Strict Entailment",
    },
    ("CVPR", 2026): {
        "Beyond Perceptual Shortcuts: Causal-Inspired Debiasing Optimization for Generalizable Video Reasoning in Lightweight MLLMs",
        "CC-VQA: Conflict- and Correlation-Aware Method for Mitigating Knowledge Conflict in Knowledge-Based Visual Question Answering",
        "CodeV: Code with Images for Faithful Visual Reasoning via Tool-Aware Policy Optimization",
        "Do VLMs Perceive or Recall? Probing Visual Perception vs. Memory with Classic Visual Illusions",
        "Dual-Level Confidence based Implicit Self-Refinement for Medical Visual Question Answering",
        "Linking Perception, Confidence and Accuracy in MLLMs",
        "PDCR: Perception-Decomposed Confidence Reward for Vision-Language Reasoning",
        "Proof-of-Perception: Certified Tool-Using Multimodal Reasoning with Compositional Conformal Guarantees",
        "Revisiting Visual Corruptions in LVLMs: A Shape-Texture Perspective on Model Failures",
        "Saliency-R1: Enforcing Interpretable and Faithful Vision-language Reasoning via Saliency-map Alignment Reward",
        "Same or Not? Enhancing Visual Perception in Vision-Language Models",
        "Uncertainty-Aware Knowledge Distillation for Multimodal Large Language Models",
    },
    ("ICLR", 2024): {
        "C-TPT: Calibrated Test-Time Prompt Tuning for Vision-Language Models via Text Feature Dispersion",
        "Faithful Vision-Language Interpretation via Concept Bottleneck Models",
        "Grounding Multimodal Large Language Models to the World",
        "RAPPER: Reinforced Rationale-Prompted Paradigm for Natural Language Explanation in Visual Question Answering",
    },
    ("ICLR", 2025): {
        "Dysca: A Dynamic and Scalable Benchmark for Evaluating Perception Ability of LVLMs",
        "Have the VLMs Lost Confidence? A Study of Sycophancy in VLMs",
        "Mind the GAP: Glimpse-based Active Perception improves generalization and sample efficiency of visual reasoning",
        "MLLMs Know Where to Look: Training-free Perception of Small Visual Details with Multimodal LLMs",
        "Natural Language Inference Improves Compositionality in Vision-Language Models",
        "See What You Are Told: Visual Attention Sink in Large Multimodal Models",
        "Two Effects, One Trigger: On the Modality Gap, Object Bias, and Information Imbalance in Contrastive Vision-Language Models",
    },
    ("ICLR", 2026): {
        "The Unseen Bias: How Norm Discrepancy in Pre-Norm MLLMs Leads to Visual Information Loss",
        "Let's Think in Two Steps: Mitigating Agreement Bias in MLLMs with Self-Grounded Verification",
        "Math Blind: Failures in Diagram Understanding Undermine Reasoning in MLLMs",
        "Perception-Aware Policy Optimization for Multimodal Reasoning",
        "RegionReasoner: Region-Grounded Multi-Round Visual Reasoning",
        "Revisiting Confidence Calibration for Misclassification Detection in VLMs",
        "SpaCE-10: A Comprehensive Benchmark for Multimodal Large Language Models in Compositional Spatial Intelligence",
        "SpatialViz-Bench: A Cognitively-Grounded Benchmark for Diagnosing Spatial Visualization in MLLMs",
        "Teaching VLMs to Admit Uncertainty in OCR from Lossy Visual Inputs",
        "Understanding Language Prior of LVLMs by Contrasting Chain-of-Embedding",
        "ViPER: Empowering the Self-Evolution of Visual Perception Abilities in Vision-Language Models",
        "VisuRiddles: Fine-grained Perception is a Primary Bottleneck for Multimodal Large Language Models in Abstract Visual Reasoning",
        "Why Keep Your Doubts to Yourself? Trading Visual Uncertainties among Vision-Language Models",
    },
    ("NeurIPS", 2023): {
        "COCO-Counterfactuals: Automatically Constructed Counterfactual Examples for Image-Text Pairs",
        "Interactive Visual Reasoning under Uncertainty",
        "SugarCrepe: Fixing Hackable Benchmarks for Vision-Language Compositionality",
    },
    ("NeurIPS", 2024): {
        "BiVLC: Extending Vision-Language Compositionality Evaluation with Text-to-Image Retrieval",
        "ConMe: Rethinking Evaluation of Compositional Reasoning for Modern VLMs",
        "MultiTrust: A Comprehensive Benchmark Towards Trustworthy Multimodal Large Language Models",
        "SpatialRGPT: Grounded Spatial Reasoning in Vision-Language Models",
        "Towards Calibrated Robust Fine-Tuning of Vision-Language Models",
        "WildVision: Evaluating Vision-Language Models in the Wild with Human Preferences",
    },
    ("NeurIPS", 2025): {
        "ColorBench: Can VLMs See and Understand the Colorful World? A Comprehensive Benchmark for Color Perception, Reasoning, and Robustness",
        "CURV: Coherent Uncertainty-Aware Reasoning in Vision-Language Models for X-Ray Report Generation",
        "Dual-Stage Value-Guided Inference with Margin-Based Reward Adjustment for Fast and Faithful VLM Captioning",
        "Grounded Reinforcement Learning for Visual Reasoning",
        "MMPerspective: Do MLLMs Understand Perspective? A Comprehensive Benchmark for Perspective Perception, Reasoning, and Robustness",
        "Point-RFT: Improving Multimodal Reasoning with Visually Grounded Reinforcement Finetuning",
        "Struct2D: A Perception-Guided Framework for Spatial Reasoning in MLLMs",
        "Understanding and Rectifying Safety Perception Distortion in VLMs",
        "Unveiling the Compositional Ability Gap in Vision-Language Reasoning Model",
        "ViCrit: A Verifiable Reinforcement Learning Proxy Task for Visual Perception in VLMs",
    },
}


EXCLUDE = (
    "3d generation", "3d content generation", "image restoration", "deepfake",
    "text-to-image synthesis", "hallucination-inducing image generation",
    "controlled visual hallucination via thalamus", "sign language translation",
    "visual scene hallucination",
    "hallucinating latent positives", "scene graph hallucination diffusion",
    "generative restoration models", "hallucination-aware diffusion priors",
    "hallugen: synthesizing", "dehallu3d", "audio hallucinations in large audio-language",
    "leveraging hallucinations to reduce manual prompt dependency",
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

    # ICLR 2023 predates the proceedings.iclr.cc index used for later years.
    # These accepted papers were verified on the official OpenReview venue.
    for title, url in (
        (
            "Visually-Augmented Language Modeling",
            "https://openreview.net/forum?id=8IN-qLkl215",
        ),
        (
            "When and Why Vision-Language Models Behave Like Bags-of-Words, and What to Do About It?",
            "https://openreview.net/forum?id=KRLUvxh8uaX",
        ),
    ):
        add(rows, seen, title, url, "ICLR 2023", 2023, "Related")

    # ICML 2023-2025 PMLR volumes and the ICML 2026 official poster directory.
    # Earlier versions only expanded 2026, which distorted the year distribution.
    for year in (2023, 2024, 2025):
        path = Path(f"/private/tmp/icml{year}.html")
        if not path.exists():
            continue
        for title, href in pmlr_rows(path.read_text(errors="ignore")):
            scope = "Related" if title in RELATED_ICML_BY_YEAR.get(year, set()) else scope_for(title)
            if scope:
                add(rows, seen, title, href, f"ICML {year}", year, scope)

    path = Path("/private/tmp/icml2026.html")
    if path.exists():
        parser = ICMLParser(); parser.feed(path.read_text(errors="ignore"))
        for title, href in parser.rows:
            scope = "Related" if title in RELATED_ICML_BY_YEAR[2026] else scope_for(title)
            if scope:
                add(rows, seen, title, "https://icml.cc" + href, "ICML 2026", 2026, scope)

    # Full-detail audit for CVPR, ICLR, and NeurIPS.  The complete proceedings
    # indexes are title-only; the companion cache retrieves every plausible
    # LVLM/VLM paper's official abstract so generic method names are not missed.
    abstract_cache = Path("/private/tmp/mllm-official-abstracts.json")
    if abstract_cache.exists():
        for record in json.loads(abstract_cache.read_text()):
            title = record["title"]
            key = (record["venue"], int(record["year"]))
            if title in RELATED_OFFICIAL_BY_VENUE_YEAR.get(key, set()):
                scope = "Related"
            else:
                scope = scope_for_detail_page(title, record.get("abstract", ""))
            if scope:
                add(
                    rows, seen, title, record["url"],
                    f"{record['venue']} {record['year']}", int(record["year"]), scope,
                )

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
            scope = scope_for(title)
            if scope:
                add(rows, seen, title, base + href, venue, year, scope)

    # CVPR and ICCV official CVF Open Access indexes.
    for path in sorted(Path("/private/tmp").glob("cvpr20*.html")) + sorted(Path("/private/tmp").glob("iccv20*.html")):
        match = re.search(r"(20\d{2})", path.name)
        if not match:
            continue
        year = int(match.group(1))
        venue = ("CVPR" if path.name.startswith("cvpr") else "ICCV") + f" {year}"
        parser = CVFParser(); parser.feed(path.read_text(errors="ignore"))
        for title, href in parser.rows:
            scope = scope_for(title)
            if scope:
                add(rows, seen, title, "https://openaccess.thecvf.com" + href, venue, year, scope)

    # ECCV official ECVA index (currently relevant 2024 entries).
    path = Path("/private/tmp/eccv-index.html")
    if path.exists():
        parser = CVFParser(); parser.feed(path.read_text(errors="ignore"))
        for title, href in parser.rows:
            match = re.search(r"eccv_(20\d{2})", href.lower())
            if not match:
                continue
            year = int(match.group(1))
            scope = scope_for(title)
            if scope:
                add(rows, seen, title, "https://www.ecva.net/" + href, f"ECCV {year}", year, scope)

    # ACL Anthology event pages for ACL/EMNLP/NAACL.  These official pages expose
    # abstracts, so a paper whose title is generic but whose abstract explicitly
    # studies visual/multimodal hallucination can still be recovered.
    anthology_paths = (
        sorted(Path("/private/tmp").glob("acl20*.html"))
        + sorted(Path("/private/tmp").glob("emnlp20*.html"))
        + sorted(Path("/private/tmp").glob("naacl20*.html"))
    )
    for path in anthology_paths:
        match = re.search(r"(20\d{2})", path.name)
        if not match:
            continue
        year = int(match.group(1))
        family = "ACL" if path.name.startswith("acl") else ("EMNLP" if path.name.startswith("emnlp") else "NAACL")
        for paper_id, title, abstract, findings in anthology_rows(path.read_text(errors="ignore"), year, family):
            scope = scope_for(title, abstract)
            if scope:
                venue = family + (" Findings" if findings else "") + f" {year}"
                add(rows, seen, title, f"https://aclanthology.org/{paper_id}/", venue, year, scope)

    # Additional AAAI papers verified on the official OJS article pages.
    manual = [
        (2026, "Adaptive Hallucination Alleviation in Multimodal Large Language Models: From Strategic Data Selection to Severity-Guided Training", "https://ojs.aaai.org/index.php/AAAI/article/view/39955"),
        (2026, "InEx: Hallucination Mitigation via Introspection and Cross-Modal Multi-Agent Collaboration", "https://ojs.aaai.org/index.php/AAAI/article/view/40229"),
        (2026, "Verb Mirage: Unveiling and Assessing Verb Concept Hallucinations in Multimodal Large Language Models", "https://ojs.aaai.org/index.php/AAAI/article/view/38005"),
        (2026, "OmniDPO: A Preference Optimization Framework to Address Omni-Modal Hallucination", "https://ojs.aaai.org/index.php/AAAI/article/view/39104"),
        (2026, "Multi-Agent Undercover Gaming: Hallucination Removal Through Counterfactual Test for Multimodal Reasoning", "https://ojs.aaai.org/index.php/AAAI/article/view/37613"),
        (2026, "Seeing Is Believing: Rich-Context Hallucination Detection for MLLMs via Backward Visual Grounding", "https://ojs.aaai.org/index.php/AAAI/article/view/40345"),
        (2026, "ASCD: Attention-Steerable Contrastive Decoding for Reducing Hallucination in MLLM", "https://ojs.aaai.org/index.php/AAAI/article/view/38000"),
        (2026, "Ground What You See: Hallucination-Resistant MLLMs via Caption Feedback, Diversity-Aware Sampling, and Conflict Regularization", "https://ojs.aaai.org/index.php/AAAI/article/view/37772"),
        (2026, "When Eyes and Ears Disagree: Can MLLMs Discern Audio-Visual Confusion?", "https://ojs.aaai.org/index.php/AAAI/article/view/38183"),
        (2025, "ConVis: Contrastive Decoding with Hallucination Visualization for Mitigating Hallucinations in Multimodal Large Language Models", "https://ojs.aaai.org/index.php/AAAI/article/view/32689"),
        (2025, "MoLE: Decoding by Mixture of Layer Experts Alleviates Hallucination in Large Vision-Language Models", "https://ojs.aaai.org/index.php/AAAI/article/view/34056"),
        (2025, "MHBench: Demystifying Motion Hallucination in VideoLLMs", "https://ojs.aaai.org/index.php/AAAI/article/view/32463"),
        (2025, "RoVRM: A Robust Visual Reward Model Optimized via Auxiliary Textual Preference Data", "https://ojs.aaai.org/index.php/AAAI/article/view/34721"),
        (2024, "Adventures of Trustworthy Vision-Language Models: A Survey", "https://ojs.aaai.org/index.php/AAAI/article/view/30275"),
    ]
    for year, title, url in manual:
        scope = "Related" if title.startswith(("When Eyes and Ears", "RoVRM", "Adventures of Trustworthy")) else "Core"
        add(rows, seen, title, url, f"AAAI {year}", year, scope)

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
