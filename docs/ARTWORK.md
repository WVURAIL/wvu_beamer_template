# WVU presentation artwork

The template keeps one working file for each artwork variant:

- `styles/tags/`: 15 vector SVGs, covering five tag families in three colors.
- `styles/patterns/`: `topo-blue.svg`, `topo-gold.svg`, and `topo-white.svg`.
- `styles/gwac.svg` and `styles/wv_logo.svg`: title/closing and sidebar logos.

The `svg` package converts SVGs through Inkscape at compilation time. Its PDF
cache is ignored by Git; no prepared PDF copies are needed in the source tree.
The theme uses `topo-white.svg` on its blue panels. The blue and gold variants
are available for use in custom artwork.

## Vector artwork

| Source | Preparation |
| --- | --- |
| [Topo - Solid](https://designsystem.wvu.edu/patterns/topo.svg) | Unchanged contour geometry in WVU Blue, white, and WVU Gold. |
| [Slashes](https://ccdam.wvu.edu/scm-main/Tags_Slashes.svg) | Cropped to the original motif clipping rectangles. |
| [Arrows](https://ccdam.wvu.edu/scm-main/Tags_Arrows.svg) | Cropped to the original motif clipping rectangles. |
| [Locations](https://ccdam.wvu.edu/scm-main/Tags_Locations.svg) | Cropped pins with contrasting outlines and transparent centers. |
| [POIs](https://ccdam.wvu.edu/scm-main/Tags_POIs.svg) | Cropped circular markers with contrasting outlines and transparent centers. |
| [Corner Slashes](https://ccdam.wvu.edu/scm-main/Tags_CornerSlashes.svg) | Straight-edge vector reconstructions of the published raster sheet. |

Retrieved October 9, 2026. The design-system host returned HTTP 403 for the
solid-topo source, so it was retrieved from the
[official WVU repository](https://github.com/wvuweb/wvu-ds-v3-hugo/blob/f3c5a0fbea12a34ae0f2da6659c0ecc547f357b0/static/patterns/topo.svg).

Prepared tags use WVU Gold `#EEAA00`, WVU Blue `#002855`, Not Quite White
`#F7F7F7`, and Safety Blue `#0062A3` for the light treatment's outline. These
replace the source sheets' export colors while preserving their vector outlines,
proportions, and curves.

The published Corner Slashes SVG contains an embedded 767-by-230-pixel PNG.
The prepared corner slashes trace its repeated right triangle with three straight
edges, preserving its approximately 153:230 aspect ratio and two-pixel outline
at the source scale. They are traced presentation assets, not original vectors
supplied by WVU.

The QR frame combines a generated QR code with the official slash and template
colors; it is a presentation component.

The separate downloaded source sheets and conversion scripts were removed from
the working template. Earlier Git revisions retain them for exact regeneration.
