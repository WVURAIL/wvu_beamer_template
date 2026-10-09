# WVU presentation artwork

The template keeps one working file for each artwork variant:

- `styles/tags/`: 15 vector SVGs, covering five tag families in three colors.
- `styles/patterns/`: three solid-topo SVG color variants and four PNG textures.
- `styles/gwac.svg` and `styles/wv_logo.svg`: title/closing and sidebar logos.

The `svg` package converts SVGs through Inkscape at compilation time. Its PDF
cache is ignored by Git; no prepared PDF copies are needed in the source tree.
The four PNG textures are used directly. Wrapping a PNG in SVG or PDF would not
make it a scalable vector or improve its resolution.

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

Pinstripes are drawn directly as vector lines in `wvubrand-patterns.sty`, following
the [official pattern](https://ccdam.wvu.edu/scm-main/Texture_Pinstripes.png).
The QR frame combines a generated QR code with the official slash and template
colors; it is a presentation component.

## Raster patterns

These textures use the public PNG artwork linked from
[WVU Visual Identity](https://scm.wvu.edu/brand/visual-identity/), retrieved
October 9, 2026. The prepared white overlays preserve the source pixel dimensions,
orientation, and crop. They are not traced or upsampled.

| Pattern | Public artwork | Dimensions |
| --- | --- | --- |
| Distressed Lines | [Texture_DistressedLines.png](https://ccdam.wvu.edu/scm-main/Texture_DistressedLines.png) | 2000 x 1001 |
| Rolling Hills | [Texture_RollingHills.png](https://ccdam.wvu.edu/scm-main/Texture_RollingHills.png) | 2000 x 529 |
| Topo - Dashed | [Texture_TopoDashed.png](https://ccdam.wvu.edu/scm-main/Texture_TopoDashed.png) | 2000 x 997 |
| Topo - Morgantown | [Texture_Topo-Morgantown.png](https://ccdam.wvu.edu/scm-main/Texture_Topo-Morgantown.png) | 1000 x 506 |

For Distressed Lines, Topo - Dashed, and Topo - Morgantown, white replaces the
source color while the original alpha channel is retained exactly. For Rolling
Hills, source luminance is multiplied into the original alpha channel to preserve
the shaded layers as variations in white opacity. Slide placement adds the
template's opacity, clipping, and fade.

SHA-256 hashes of the original downloads:

| Pattern | SHA-256 |
| --- | --- |
| Distressed Lines | `c66e352624543458ec8032453aa93614daf3ddb5d81ba9d9a1dadc5ba925eb56` |
| Rolling Hills | `13a98839d41767b7eb7b8a90772950bdd44d6d6fd1190ff933593b219ceb5f88` |
| Topo - Dashed | `4c7ecf3b7677d21dd517cd4e30438a53cca48450d4c7ab6ab413899f1c51811b` |
| Topo - Morgantown | `abb52f663de85c90c4858d299507879156b299fe1164c5b8b7e0e3c98e025cfa` |

The separate downloaded source sheets and conversion scripts were removed from
the working template. Earlier Git revisions retain them for exact regeneration.
The full production library linked by WVU may offer other source formats; the
four textures here preserve the publicly supplied raster artwork.
