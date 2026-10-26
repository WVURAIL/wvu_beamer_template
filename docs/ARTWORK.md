# WVU presentation artwork

The template keeps one working file for each artwork variant:

- `styles/tags/`: 15 vector SVGs, covering five tag families in three colors.
- `styles/patterns/`: `topo-blue.svg`, `topo-gold.svg`, and `topo-white.svg`.
- `styles/gwac.svg` and `styles/wv_logo.svg`: title/closing and sidebar logos.

At compilation time, the SVGs are converted to PDF through Inkscape by the
`svg` package. Git ignores the PDF cache of this conversion, so no PDF copies
are kept in the source tree. On its blue panels, the theme uses
`topo-white.svg`, and the blue and gold variants are available for custom
artwork.

## Vector artwork

| Source | Preparation |
| --- | --- |
| [Topo - Solid](https://designsystem.wvu.edu/patterns/topo.svg) | Unchanged contour geometry in WVU Blue, white, and WVU Gold. |
| [Slashes](https://ccdam.wvu.edu/scm-main/Tags_Slashes.svg) | Cropped to the original motif clipping rectangles. |
| [Arrows](https://ccdam.wvu.edu/scm-main/Tags_Arrows.svg) | Cropped to the original motif clipping rectangles. |
| [Locations](https://ccdam.wvu.edu/scm-main/Tags_Locations.svg) | Cropped pins with contrasting outlines and transparent centers. |
| [POIs](https://ccdam.wvu.edu/scm-main/Tags_POIs.svg) | Cropped circular markers with contrasting outlines and transparent centers. |
| [Corner Slashes](https://ccdam.wvu.edu/scm-main/Tags_CornerSlashes.svg) | Straight-edge vector reconstructions of the published raster sheet. |

All sources were retrieved on October 9, 2026. For the solid-topo source, the
design-system host returned HTTP 403, so it was retrieved from the
[official WVU repository](https://github.com/wvuweb/wvu-ds-v3-hugo/blob/f3c5a0fbea12a34ae0f2da6659c0ecc547f357b0/static/patterns/topo.svg).

The prepared tags use WVU Gold `#EEAA00`, WVU Blue `#002855`, Not Quite White
`#F7F7F7`, and Safety Blue `#0062A3` for the outline of the light treatment.
These colors replace the export colors of the source sheets, and the vector
outlines, proportions, and curves are unchanged.

The published Corner Slashes SVG contains an embedded 767-by-230-pixel PNG. Each
prepared corner slash traces the repeated right triangle of that image with
three straight edges, which keeps its aspect ratio of about 153:230 and its
two-pixel outline at the source scale. These shapes are tracings made for the
template from the WVU raster and are not original WVU vectors.

In the QR component of the template, a generated QR code is set in WVU Blue
in a WVU Blue frame on white, and its caption is marked with the official
slash.

In commit dba6de5, the downloaded source sheets and the conversion scripts were
removed from `styles/brand/`. For exact regeneration, they are restored from
its parent with `git checkout dba6de5^ -- styles/brand`.
