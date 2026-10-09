# WVU presentation artwork

The SVGs in `sources/` retain the original published artwork. The adjacent SVG/PDF pairs are prepared for inclusion in the presentation; the PDFs contain vectors and transparent backgrounds and require no fonts or external resources.

| Source | Use |
| --- | --- |
| [Topo](https://designsystem.wvu.edu/patterns/topo.svg) | Contour pattern; unchanged geometry in navy, white, and gold. |
| [Slashes](https://ccdam.wvu.edu/scm-main/Tags_Slashes.svg) | Gold slash with navy outline, cropped to the original motif clipping rectangle. |
| [Arrows](https://ccdam.wvu.edu/scm-main/Tags_Arrows.svg) | Gold right-pointing arrow with navy outline, cropped to the original motif clipping rectangle. |
| [Locations](https://ccdam.wvu.edu/scm-main/Tags_Locations.svg) | Gold and navy location pins with contrasting outlines and transparent centers, cropped to the original motif clipping rectangles. |

Retrieved October 9, 2026. The design-system host returned HTTP 403 for the contour pattern, so its source was retrieved from the [official WVU design-system repository](https://github.com/wvuweb/wvu-ds-v3-hugo/blob/f3c5a0fbea12a34ae0f2da6659c0ecc547f357b0/static/patterns/topo.svg).

Prepared artwork uses the template's digital gold `#EEAA00` and navy `#002855`; these replace the source sheets' export colors. Outlines, proportions, and curves are retained. White contours are available for dark backgrounds. Pattern placement and opacity are controlled by the theme.

Pinstripes are drawn as vector lines in `wvubrand-patterns.sty`, following the
[official pinstripe pattern](https://ccdam.wvu.edu/scm-main/Texture_Pinstripes.png).
The QR frame combines a generated QR code with the official slash and template
colors; it is a presentation component, not a copied QR library asset.

## Regenerate

With Python 3 and `rsvg-convert` installed, run from the repository root:

```sh
python3 styles/brand/rebuild_assets.py
```

Use `--renderer /path/to/rsvg-convert` for a renderer outside `PATH`. PDF output is explicitly version 1.5. Rebuilding uses the retained source SVGs and does not access the network.
