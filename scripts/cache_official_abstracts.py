#!/usr/bin/env python3
"""Cache abstracts from official CVPR, ICLR, and NeurIPS paper pages.

The proceedings indexes expose titles but not enough text for a comprehensive
hallucination search.  This script first selects every plausible LVLM/VLM paper
from the complete official indexes, then retrieves its official abstract page.
The cache is intentionally kept in /private/tmp; the reviewed subset is emitted
into the committed static corpus by build_expanded_corpus.py.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from build_expanded_corpus import CVFParser, ProceedingsParser, clean


DEFAULT_CACHE = Path("/private/tmp/mllm-official-abstracts.json")
DISCOVERY_TERMS = (
    "hallucin", "vision-language", "vision language", "vision-and-language",
    "visual language", "large multimodal", "large multi-modal", "multimodal large",
    "multi-modal large", "mllm", "lvlm", "vlm", "video llm", "videollm",
    "video-language", "image caption", "visual question", "visual reasoning",
    "visual instruction", "image-text", "visual grounding", "visual evidence",
    "multimodal reasoning", "multi-modal reasoning",
)


def candidates() -> list[dict]:
    rows: list[dict] = []
    sources = []
    for year in (2023, 2024, 2025, 2026):
        sources.append((Path(f"/private/tmp/cvpr{year}.html"), CVFParser,
                        "CVPR", year, "https://openaccess.thecvf.com"))
    for year in (2024, 2025, 2026):
        sources.append((Path(f"/private/tmp/iclr{year}.html"), ProceedingsParser,
                        "ICLR", year, "https://proceedings.iclr.cc"))
    for year, filename in ((2023, "neurips2023.html"), (2024, "neurips2024.html"),
                           (2025, "neurips2025-main.html")):
        sources.append((Path("/private/tmp") / filename, ProceedingsParser,
                        "NeurIPS", year, "https://proceedings.neurips.cc"))

    for path, parser_type, venue, year, base in sources:
        if not path.exists():
            continue
        parser = parser_type()
        parser.feed(path.read_text(errors="ignore"))
        for title, href in parser.rows:
            low = title.lower()
            if any(term in low for term in DISCOVERY_TERMS):
                rows.append({
                    "title": title,
                    "venue": venue,
                    "year": year,
                    "url": base + href,
                })
    return rows


def extract_abstract(page: str) -> str:
    match = re.search(r'<div id="abstract">(.*?)</div>', page, re.S | re.I)
    if not match:
        match = re.search(r'<p class="paper-abstract">(.*?)</p>\s*</p>', page, re.S | re.I)
    if not match:
        match = re.search(r'<p class="paper-abstract">(.*?)</p>', page, re.S | re.I)
    return clean(html.unescape(match.group(1))) if match else ""


def fetch(row: dict) -> tuple[str, str]:
    request = urllib.request.Request(
        row["url"], headers={"User-Agent": "MLLM-literature-audit/1.0"}
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                page = response.read().decode("utf-8", errors="ignore")
            return row["url"], extract_abstract(page)
        except Exception:
            if attempt == 2:
                return row["url"], ""
            time.sleep(0.5 * (attempt + 1))
    return row["url"], ""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cache", type=Path, default=DEFAULT_CACHE)
    parser.add_argument("--workers", type=int, default=24)
    args = parser.parse_args()

    rows = candidates()
    existing = {}
    if args.cache.exists():
        existing = {row["url"]: row for row in json.loads(args.cache.read_text())}

    pending = [row for row in rows if not existing.get(row["url"], {}).get("abstract")]
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        future_rows = {pool.submit(fetch, row): row for row in pending}
        for index, future in enumerate(as_completed(future_rows), 1):
            row = future_rows[future]
            _, abstract = future.result()
            row["abstract"] = abstract
            existing[row["url"]] = row
            if index % 100 == 0:
                print(f"fetched {index}/{len(pending)}", flush=True)

    ordered = []
    for row in rows:
        cached = existing.get(row["url"], row)
        cached.setdefault("abstract", "")
        ordered.append(cached)
    args.cache.write_text(json.dumps(ordered, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "candidates": len(ordered),
        "abstracts": sum(bool(row["abstract"]) for row in ordered),
        "cache": str(args.cache),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
