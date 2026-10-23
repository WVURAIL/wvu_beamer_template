#!/usr/bin/env python3
"""Export the Beamer palette for standalone scientific figure generators.

Example: python tools/export_plot_palette.py --python ../dtv-rs/figsrc/wvu_palette.py
Use --check to verify an existing copy without changing it.
"""

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "styles/beamercolorthemewvu.sty"
HEADER = "Generated from wvu_beamer_template/styles/beamercolorthemewvu.sty."

SUPPORT = '''
# White and black remain available for paper backgrounds and binary masks.
WHITE = "#FFFFFF"
BLACK = "#000000"
MEASURED = BLUE
MODEL = OLD_GOLD
CONDITIONAL = HEMLOCK
FAILURE = WOODBURN
PENDING = SENECA_GRAY
INK = COAL
MUTED = RATTLER_GRAY
SERIES = (BLUE, OLD_GOLD, SAFETY_BLUE, WOODBURN, HEMLOCK, SUNSET, COAL, SENECA_GRAY)
LINESTYLES = ("-", "--", "-.", ":", "--", "-.", ":", "-")
MARKERS = ("o", "s", "^", "D", "v", "P", "X", "h")


def tint(color, fraction=0.12):
    """Mix a palette color with white; fraction is the color's contribution."""
    if not 0 <= fraction <= 1:
        raise ValueError("tint fraction must be between zero and one")
    rgb = [int(color[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(255 + fraction * (c - 255)):02X}" for c in rgb)


def sequential_cmap():
    """White-to-blue intensity scale with monotonically decreasing lightness.

    Missing values stay neutral gray. This map is for ordered values, not
    categories or cyclic phase. Importing palette constants needs no Matplotlib.
    """
    from matplotlib.colors import LinearSegmentedColormap

    cmap = LinearSegmentedColormap.from_list(
        "wvu_blue", [NOT_QUITE_WHITE, STAR_CITY_BLUE, SAFETY_BLUE, BLUE], N=256
    )
    return cmap.with_extremes(bad=COOPERS_GRAY)


def plot_rcparams():
    """Color defaults only; leave journal fonts, dimensions, and ticks intact."""
    from cycler import cycler

    return {
        "axes.prop_cycle": cycler(color=SERIES),
        "axes.edgecolor": MUTED,
        "axes.labelcolor": INK,
        "text.color": INK,
        "xtick.color": MUTED,
        "ytick.color": MUTED,
        "grid.color": tint(SENECA_GRAY, 0.3),
        "figure.facecolor": WHITE,
        "axes.facecolor": WHITE,
        "savefig.facecolor": WHITE,
    }
'''


def colors():
    entries = re.findall(
        r"\\definecolor\{(wvu-[a-z-]+)\}\{RGB\}\{([0-9, ]+)\}",
        SOURCE.read_text(),
    )
    if len(entries) != 16:
        raise ValueError("Expected the template's 16 named WVU colors")
    return [(name, "#" + "".join(f"{int(c):02X}" for c in rgb.split(",")))
            for name, rgb in entries]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--python", action="append", type=Path, default=[])
    parser.add_argument("--tex", action="append", type=Path, default=[])
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    if not args.python and not args.tex:
        parser.error("choose at least one --python or --tex output")
    palette = colors()
    py = f'"""{HEADER}\n\nStandalone copy; update with tools/export_plot_palette.py in that repository.\n"""\n\n'
    py += "\n".join(f'{name[4:].replace("-", "_").upper()} = "{value}"'
                    for name, value in palette) + "\n" + SUPPORT
    tex = f"% {HEADER}\n% Standalone copy; no Beamer dependency.\n"
    tex += "\n".join(f"\\definecolor{{{name}}}{{HTML}}{{{value[1:]}}}"
                     for name, value in palette) + "\n"
    for paths, content in [(args.python, py), (args.tex, tex)]:
        for path in paths:
            if args.check:
                if not path.exists() or path.read_text() != content:
                    raise SystemExit(f"Palette differs: {path}")
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(content)
            print(path)


if __name__ == "__main__":
    main()
