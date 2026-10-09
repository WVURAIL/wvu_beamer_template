# WVU presentation artwork

The SVGs in `sources/` retain the original published artwork. The prepared tag and solid-topo SVG/PDF pairs contain vectors and transparent backgrounds and require no fonts or external resources. The additional pattern assets are documented separately in [PATTERN_SOURCES.md](PATTERN_SOURCES.md).

| Source | Use |
| --- | --- |
| [Topo - Solid](https://designsystem.wvu.edu/patterns/topo.svg) | Contour pattern; unchanged geometry in WVU Blue, white, and WVU Gold. |
| [Slashes](https://ccdam.wvu.edu/scm-main/Tags_Slashes.svg) | WVU Gold, WVU Blue, and Not Quite White slashes, cropped to the original motif clipping rectangles. |
| [Arrows](https://ccdam.wvu.edu/scm-main/Tags_Arrows.svg) | WVU Gold, WVU Blue, and Not Quite White arrows, cropped to the original motif clipping rectangles. |
| [Locations](https://ccdam.wvu.edu/scm-main/Tags_Locations.svg) | WVU Gold, WVU Blue, and Not Quite White pins with contrasting outlines and transparent centers, cropped to the original motif clipping rectangles. |
| [POIs](https://ccdam.wvu.edu/scm-main/Tags_POIs.svg) | WVU Gold, WVU Blue, and Not Quite White circular point-of-interest markers, cropped to the original motif clipping rectangles. |
| [Corner Slashes](https://ccdam.wvu.edu/scm-main/Tags_CornerSlashes.svg) | WVU Gold, WVU Blue, and Not Quite White corner slashes reconstructed with straight vector edges from the published raster sheet; see below. |

Retrieved October 9, 2026. The design-system host returned HTTP 403 for the contour pattern, so its source was retrieved from the [official WVU design-system repository](https://github.com/wvuweb/wvu-ds-v3-hugo/blob/f3c5a0fbea12a34ae0f2da6659c0ecc547f357b0/static/patterns/topo.svg).

Prepared artwork uses the template's WVU Gold `#EEAA00` and WVU Blue `#002855`; these replace the source sheets' export colors. The Not Quite White treatment uses the approved web neutral `#F7F7F7` and Safety Blue `#0062A3` outline in place of the source export colors `#F7F5F5` and `#0B74BB`. Outlines, proportions, and curves from the vector sheets are retained. White contours are available for dark backgrounds. Pattern placement and opacity are controlled by the theme.

The published Corner Slashes SVG contains only an embedded 767-by-230-pixel PNG.
The prepared corner slashes reconstruct its repeated right-triangle shape using
three straight vector edges, preserving its approximately 153:230 aspect ratio
and two-pixel outline at the source scale. These are traced presentation assets,
not original vector files supplied by WVU. The embedded PNG remains intact in
`sources/Tags_CornerSlashes.svg` for comparison and provenance.

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
