#!/usr/bin/env python3
"""Lightweight audit for Ultimate PPT output folders."""

from pathlib import Path
import argparse
import re
import sys


def read_pptx_text(path):
    try:
        from pptx import Presentation
    except Exception:
        return None, "python-pptx is not installed"
    prs = Presentation(path)
    slides = []
    for slide in prs.slides:
        slides.append("\n".join(shape.text for shape in slide.shapes if hasattr(shape, "text")))
    return slides, None


def audit_folder(folder):
    folder = Path(folder)
    errors = []
    warnings = []
    pptx_files = list(folder.glob("*.pptx"))
    html_files = list(folder.glob("*.html"))

    if not pptx_files and not html_files:
        errors.append("No PPTX or HTML deck found.")

    for pptx in pptx_files:
        slides, err = read_pptx_text(pptx)
        if err:
            warnings.append(f"{pptx.name}: {err}; skipped PPTX text audit.")
            continue
        if len(slides) < 5:
            warnings.append(f"{pptx.name}: only {len(slides)} slides.")
        first = slides[0] if slides else ""
        if "github.com" not in first and "http" not in first:
            warnings.append(f"{pptx.name}: first slide has no visible URL/source footer.")
        for i, text in enumerate(slides, 1):
            words = re.findall(r"[\w\u4e00-\u9fff]+", text)
            if len(words) > 120:
                warnings.append(f"{pptx.name} slide {i}: high text density ({len(words)} tokens).")

    for html in html_files:
        text = html.read_text(encoding="utf-8", errors="ignore")
        if "<section" not in text and "class=\"slide" not in text and "class='slide" not in text:
            warnings.append(f"{html.name}: no obvious slide sections.")
        if "100vh" not in text and "100dvh" not in text:
            warnings.append(f"{html.name}: no 100vh/100dvh viewport constraint found.")

    if not (folder / "run-log.md").exists() and not (folder / "skill-run.md").exists():
        warnings.append("No run-log.md or skill-run.md found.")

    return errors, warnings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Output folder to audit")
    args = parser.parse_args()
    errors, warnings = audit_folder(args.path)
    if errors:
        print("FAIL")
        for item in errors:
            print(f"ERROR: {item}")
        for item in warnings:
            print(f"WARN: {item}")
        return 1
    print("PASS")
    for item in warnings:
        print(f"WARN: {item}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
