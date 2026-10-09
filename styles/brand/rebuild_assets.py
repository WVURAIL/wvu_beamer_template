#!/usr/bin/env python3
"""Rebuild portable vector assets from the retained official SVG sources."""
from pathlib import Path
import argparse
import copy
import subprocess
import xml.etree.ElementTree as ET

NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)
ROOT = Path(__file__).resolve().parent
GOLD, BLUE = "#EEAA00", "#002855"
OFFWHITE, ACCENT_BLUE = "#F7F7F7", "#0062A3"

# Bounds are the clipping rectangles in the published vector sheets.
TAG_ASSETS = [
    ("Tags_Slashes.svg", "Slash-Tag-124", "53.3 -0.07 77.48 59.09", "slash-gold"),
    ("Tags_Slashes.svg", "Slash-Tag-295", "0 -0.07 77.89 59.09", "slash-blue"),
    ("Tags_Slashes.svg", "Slash-Tag-NQW", "106.19 -0.07 77.89 59.09", "slash-offwhite"),
    ("Tags_Arrows.svg", "Arrow-Tag-124", "65.48 0 53.14 56.32", "arrow-gold"),
    ("Tags_Arrows.svg", "Arrow-Tag-295", "130.95 0 53.14 56.32", "arrow-blue"),
    ("Tags_Arrows.svg", "Arrow-Tag-NQW", "0 0 53.14 56.32", "arrow-offwhite"),
    ("Tags_Locations.svg", "Location-Tag-124", "64.92 0 54.06 74.36", "location-gold"),
    ("Tags_Locations.svg", "Location-Tag-295", "0 0 54.06 74.36", "location-blue"),
    ("Tags_Locations.svg", "Location-Tag-NQW", "130.03 0 54.06 74.36", "location-offwhite"),
    ("Tags_POIs.svg", "POI-Tag-124", "62.79 0 58.5 58.5", "poi-gold"),
    ("Tags_POIs.svg", "POI-Tag-295", "0 0 58.5 58.5", "poi-blue"),
    ("Tags_POIs.svg", "POI-Tag-NQW", "125.58 0 58.5 58.5", "poi-offwhite"),
]

def write_svg(name, root):
    xml = ET.tostring(root, encoding="utf-8", xml_declaration=True).decode("utf-8")
    (ROOT / f"{name}.svg").write_text("\n".join(line.rstrip() for line in xml.splitlines()) + "\n", encoding="utf-8")

def motif(source, group_id, viewbox, name):
    source_root = ET.parse(ROOT / "sources" / source).getroot()
    root = ET.Element(f"{{{NS}}}svg", {"viewBox": viewbox})
    defs = copy.deepcopy(source_root.find(f"{{{NS}}}defs"))
    for style in defs.iter(f"{{{NS}}}style"):
        for old in ("#f0b012", "#f0af13"):
            style.text = style.text.replace(old, GOLD)
        for old in ("#002d5b", "#193059"):
            style.text = style.text.replace(old, BLUE)
        style.text = style.text.replace("#f7f5f5", OFFWHITE).replace("#0b74bb", ACCENT_BLUE)
    root.append(defs)
    root.append(copy.deepcopy(next(e for e in source_root if e.get("id") == group_id)))
    write_svg(name, root)

def corner_slash(name, fill, stroke):
    # The official corner-slash SVG embeds a 767x230 PNG, not vector paths.
    # Its repeated straight-edged triangle is traced in source-pixel units;
    # keeping the outline separate preserves crisp edges at any output size.
    root = ET.Element(f"{{{NS}}}svg", {"viewBox": "0 0 153 230"})
    ET.SubElement(root, f"{{{NS}}}polygon", {
        "points": "1,3.25 151,228.25 1,228.25",
        "fill": fill, "stroke": stroke, "stroke-width": "2",
        "stroke-linejoin": "miter",
    })
    write_svg(name, root)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--renderer", default="rsvg-convert", help="Path to rsvg-convert")
    args = parser.parse_args()
    names = []
    for name, color in [("topo", BLUE), ("topo-white", "#FFFFFF"), ("topo-gold", GOLD)]:
        root = ET.parse(ROOT / "sources" / "topo.svg").getroot()
        root.set("fill", color)
        write_svg(name, root)
        names.append(name)
    for source, group_id, viewbox, name in TAG_ASSETS:
        motif(source, group_id, viewbox, name)
        names.append(name)
    for color, fill, stroke in [("gold", GOLD, BLUE), ("blue", BLUE, GOLD),
                                ("offwhite", OFFWHITE, ACCENT_BLUE)]:
        name = f"corner-slash-{color}"
        corner_slash(name, fill, stroke)
        names.append(name)
    for name in names:
        subprocess.run([args.renderer, "--format", "pdf1.5", "--output", str(ROOT / f"{name}.pdf"), str(ROOT / f"{name}.svg")], check=True)
        print(f"Built {name}.svg and {name}.pdf")

if __name__ == "__main__":
    main()
