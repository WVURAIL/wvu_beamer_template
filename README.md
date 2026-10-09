# WVU Beamer template

A widescreen Beamer presentation template using WVU colors and logos with
the [Amurmaple theme](https://ctan.org/pkg/beamerthemeamurmaple).

## Start a presentation

1. Copy the repository, keeping `styles/` and `title_graphics/` beside `main.tex`.
2. Edit the title, author, affiliation, date, email, and website placeholders in
   `styles/amurmaplewvu.sty`.
3. Choose a title graphic and secondary colors in that same file. The default
   is the vector GWAC logo; the other college graphics remain in `title_graphics/`.
4. Replace the example slides in `main.tex`, retaining `aspectratio=169`.

Compile with **LuaLaTeX**, using a TeX Live installation that includes Beamer,
Amurmaple, its dependencies, and `latexmk`. CI uses the full TeX Live 2025
environment. From the repository root:

```sh
latexmk -lualatex -file-line-error -halt-on-error -interaction=nonstopmode main.tex
```

`latexmkrc` adds `styles/` to TeX's search path. The output is `main.pdf`.
Run `latexmk -c main.tex` to remove intermediate build files. Generated output
is ignored by Git; the checked-in example PDFs remain reference material.

For Overleaf, upload the repository and select LuaLaTeX as the compiler and
`main.tex` as the main document. Preserve the folder layout.

## Fonts and vector logos

The template uses **TeX Gyre Heros** for sans-serif slide text through
`fontspec`. It is a Helvetica-compatible substitute included with TeX Live and
Overleaf, not the proprietary Helvetica or Helvetica Neue font. This follows
WVU's use of Helvetica as a general-purpose typeface while keeping the template
portable. See the [WVU typography guidance](https://scm.wvu.edu/brand/visual-identity/)
and [TeX Gyre Heros documentation](https://ctan.org/pkg/tex-gyre-heros).
The font is selected in `styles/amurmaplewvu.sty`; the logo lettering remains
part of the vector artwork.

The SVG sources and matching PDF copies of both logos are in `styles/`.
The template includes the PDFs directly, so normal builds do not need Inkscape
or shell escape. After editing an SVG, regenerate its PDF before compiling.
With `rsvg-convert` installed, run:

```sh
rsvg-convert -f pdf1.5 -o styles/gwac.pdf styles/gwac.svg
rsvg-convert -f pdf1.5 -o styles/wv_logo.pdf styles/wv_logo.svg
```

## Check changes

Pushes and pull requests compile the example with LuaLaTeX. After a successful
**Build template** run, download **wvu-beamer-example** from its Actions page.
Review that PDF for clipped text, image proportions, readable colors, and slide
numbering; compilation alone does not establish visual quality. Dependencies
used by Actions receive weekly grouped minor/patch update pull requests.

## Attribution and reuse

The example and theme configuration retain their source attribution in
`main.tex`. See the bundled `beamer-amurmaple-doc.pdf` and the upstream theme
documentation for theme usage. This repository does not currently include a
repository-wide license; do not infer new reuse terms from these instructions.
WVU names and logos have separate [brand requirements](https://scm.wvu.edu/brand/).
