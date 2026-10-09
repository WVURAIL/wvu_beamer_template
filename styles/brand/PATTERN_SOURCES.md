# Additional WVU pattern sources

These four patterns are the official public PNG artwork linked from
[WVU Visual Identity](https://scm.wvu.edu/brand/visual-identity/), retrieved
October 9, 2026. The original downloaded bytes are retained under `sources/`.

| Pattern | Original public artwork | SHA-256 |
| --- | --- | --- |
| `distressed-lines` | [Texture_DistressedLines.png](https://ccdam.wvu.edu/scm-main/Texture_DistressedLines.png) | `c66e352624543458ec8032453aa93614daf3ddb5d81ba9d9a1dadc5ba925eb56` |
| `rolling-hills` | [Texture_RollingHills.png](https://ccdam.wvu.edu/scm-main/Texture_RollingHills.png) | `13a98839d41767b7eb7b8a90772950bdd44d6d6fd1190ff933593b219ceb5f88` |
| `topo-dashed` | [Texture_TopoDashed.png](https://ccdam.wvu.edu/scm-main/Texture_TopoDashed.png) | `4c7ecf3b7677d21dd517cd4e30438a53cca48450d4c7ab6ab413899f1c51811b` |
| `topo-morgantown` | [Texture_Topo-Morgantown.png](https://ccdam.wvu.edu/scm-main/Texture_Topo-Morgantown.png) | `abb52f663de85c90c4858d299507879156b299fe1164c5b8b7e0e3c98e025cfa` |

## Preparation and resolution

The `*-white.png` and `*-white.pdf` files are transparent white overlays for
navy slide panels. They preserve the original pixel dimensions and aspect ratio;
they are **raster artwork**, including when embedded in a PDF. No geometry was
traced, redrawn, or generated. They should not be described as scalable vectors.

| Pattern | Original dimensions | Aspect ratio |
| --- | --- | --- |
| Distressed Lines | 2000 x 1001 | 1.998:1 |
| Rolling Hills | 2000 x 529 | 3.781:1 |
| Topo - Dashed | 2000 x 997 | 2.006:1 |
| Topo - Morgantown | 1000 x 506 | 1.976:1 |

For Distressed Lines, Topo - Dashed, and Topo - Morgantown, white replaces the
source color while the original alpha channel is retained exactly. For Rolling
Hills, the source luminance is multiplied into its original alpha channel to
preserve the shaded layers as variations in white opacity. All four overlays
retain the same orientation and crop as the public source. The presentation
applies its own overall opacity and clipping after placement.

Only the existing solid topo pattern was available as an official public vector
in the WVU design-system repository. The four new patterns use the public raster
artwork rather than an approximate vector reconstruction. The full production
library linked by the WVU brand site may provide higher-resolution originals.

## Rebuild

With Python 3 and Pillow installed, run:

```sh
python3 styles/brand/rebuild_patterns.py
```

The script rebuilds the PNG overlays and PDF 1.5 wrappers using the retained
sources. It performs no downloads, upsampling, smoothing, or color quantization.
The PDFs use lossless compression with an 8-bit alpha mask. Rendering these
assets at very large sizes is limited by the resolutions above.
