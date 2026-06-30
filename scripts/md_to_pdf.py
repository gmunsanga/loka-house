#!/usr/bin/env python3
"""Convertit le SAD Markdown en PDF avec une mise en page soignee."""
import sys
import markdown
from xhtml2pdf import pisa

SRC = "docs/SAD_Loka_House.md"
OUT = "docs/SAD_Loka_House.pdf"

CSS = """
@page { size: A4; margin: 1.8cm 1.6cm; }
body { font-family: Helvetica, Arial, sans-serif; font-size: 10pt; color: #1a1a1a; line-height: 1.4; }
h1 { font-size: 20pt; color: #0b3d2e; border-bottom: 2px solid #0b3d2e; padding-bottom: 4px; }
h2 { font-size: 15pt; color: #0b5d44; margin-top: 16px; border-bottom: 1px solid #cccccc; padding-bottom: 2px; }
h3 { font-size: 12pt; color: #117a5b; margin-top: 12px; }
h4 { font-size: 11pt; color: #444444; }
p { margin: 4px 0; }
a { color: #0b5d44; text-decoration: none; }
table { width: 100%; border-collapse: collapse; margin: 8px 0; }
th { background-color: #0b5d44; color: #ffffff; padding: 5px 6px; text-align: left; font-size: 9pt; }
td { border: 1px solid #cccccc; padding: 4px 6px; font-size: 9pt; vertical-align: top; }
tr:nth-child(even) td { background-color: #f2f7f5; }
pre { background-color: #f5f5f5; border: 1px solid #dddddd; padding: 6px; font-family: Courier, monospace;
      font-size: 6.5pt; line-height: 1.1; white-space: pre; }
code { font-family: Courier, monospace; font-size: 9pt; background-color: #f0f0f0; padding: 1px 3px; }
pre code { background-color: transparent; padding: 0; font-size: 6.5pt; }
ul, ol { margin: 4px 0 4px 4px; }
li { margin: 2px 0; }
hr { border: none; border-top: 1px solid #cccccc; margin: 12px 0; }
"""

def main():
    with open(SRC, "r", encoding="utf-8") as f:
        text = f.read()
    html_body = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists", "nl2br"],
    )
    html = f"""<!DOCTYPE html><html><head><meta charset="utf-8">
<style>{CSS}</style></head><body>{html_body}</body></html>"""
    with open(OUT, "wb") as out:
        result = pisa.CreatePDF(html, dest=out, encoding="utf-8")
    if result.err:
        print("Erreur lors de la generation du PDF", file=sys.stderr)
        sys.exit(1)
    print(f"PDF genere : {OUT}")

if __name__ == "__main__":
    main()
