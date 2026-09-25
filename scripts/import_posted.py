"""Import published articles from Eric's posted shelf into the site.

Reads ~/Vaults/Eric/Journal/Publications/posted/YYYYMMDD-slug/ packets (front matter:
public_title, published_at, canonical_urls, cover) and writes:
  src/content/articles/<slug>.md    one entry per article, linking to its canonical URL
  public/covers/<slug>.webp          the cover banner, resized to 1200px wide

Run locally after a new article is posted:
  uv run --with pillow --with pyyaml python scripts/import_posted.py
Entries are regenerated from the shelf, so re-running is safe.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml
from PIL import Image

SHELF = Path.home() / "Vaults/Eric/Journal/Publications/posted"
ROOT = Path(__file__).resolve().parents[1]
ARTICLES = ROOT / "src/content/articles"
COVERS = ROOT / "public/covers"


def first_paragraph(body: str, limit: int = 240) -> str:
    for block in re.split(r"\n\s*\n", body):
        text = block.strip()
        if not text or text.startswith(("#", "!", ">", "|", "```", "-", "*")):
            continue
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
        text = re.sub(r"[*_`]", "", " ".join(text.split()))
        if len(text) <= limit:
            return text
        cut = text[:limit]
        stop = max(cut.rfind(". "), cut.rfind("? "), cut.rfind("! "))
        return cut[: stop + 1] if stop > 80 else cut.rsplit(" ", 1)[0] + "…"
    return ""


def main() -> int:
    ARTICLES.mkdir(parents=True, exist_ok=True)
    COVERS.mkdir(parents=True, exist_ok=True)
    count = 0
    for packet in sorted(p for p in SHELF.iterdir() if p.is_dir()):
        mds = [m for m in packet.glob("*.md") if m.name != "linkedin-lead-in.md"]
        if not mds:
            continue
        text = mds[0].read_text()
        _, fm_raw, body = text.split("---", 2)
        fm = yaml.safe_load(fm_raw)
        if fm.get("status") != "published":
            continue
        slug = packet.name.split("-", 1)[1]
        urls = fm.get("canonical_urls") or {}
        url = urls.get("linkedin") or urls.get("huggingface")
        venue = "LinkedIn" if urls.get("linkedin") else "Hugging Face"
        if not url:
            print(f"skip {slug}: no canonical URL", file=sys.stderr)
            continue
        cover_line = ""
        if fm.get("cover"):
            src = packet / fm["cover"]
            if src.exists():
                img = Image.open(src).convert("RGB")
                if img.width > 1200:
                    img = img.resize((1200, round(img.height * 1200 / img.width)), Image.LANCZOS)
                img.save(COVERS / f"{slug}.webp", "WEBP", quality=82, method=6)
                cover_line = f"cover: '/covers/{slug}.webp'\n"
        title = fm.get("public_title") or packet.name
        summary = first_paragraph(body)
        entry = (
            "---\n"
            f"title: {yaml.safe_dump(title, allow_unicode=True, width=10_000).strip().removesuffix('...').strip()}\n"
            f"summary: {yaml.safe_dump(summary, allow_unicode=True, width=10_000).strip().removesuffix('...').strip()}\n"
            f"date: {fm['published_at']}\n"
            f"venue: {venue}\n"
            f"url: '{url}'\n"
            f"{cover_line}"
            "---\n"
        )
        (ARTICLES / f"{slug}.md").write_text(entry)
        count += 1
    print(f"imported {count} articles")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
