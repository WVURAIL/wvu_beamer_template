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
    root.append(defs)
    root.append(copy.deepcopy(next(e for e in source_root if e.get("id") == group_id)))
    write_svg(name, root)

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--renderer", default="rsvg-convert", help="Path to rsvg-convert")
    args = parser.parse_args()
    for name, color in [("topo", BLUE), ("topo-white", "#FFFFFF"), ("topo-gold", GOLD)]:
        root = ET.parse(ROOT / "sources" / "topo.svg").getroot()
        root.set("fill", color)
        write_svg(name, root)
    motif("Tags_Slashes.svg", "Slash-Tag-124", "53.3 -0.07 77.48 59.09", "slash-gold")
    motif("Tags_Arrows.svg", "Arrow-Tag-124", "65.48 0 53.14 56.32", "arrow-gold")
    motif("Tags_Locations.svg", "Location-Tag-124", "64.92 0 54.06 74.36", "location-gold")
    motif("Tags_Locations.svg", "Location-Tag-295", "0 0 54.06 74.36", "location-blue")
    for name in ["topo", "topo-white", "topo-gold", "slash-gold", "arrow-gold", "location-gold", "location-blue"]:
        subprocess.run([args.renderer, "--format", "pdf1.5", "--output", str(ROOT / f"{name}.pdf"), str(ROOT / f"{name}.svg")], check=True)
        print(f"Built {name}.svg and {name}.pdf")

if __name__ == "__main__":
    main()
