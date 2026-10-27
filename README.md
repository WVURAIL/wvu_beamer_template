# WVU Beamer template

The WVU Beamer template is a theme for West Virginia University presentations,
built on Maxime Chupin's Amurmaple theme. Slides are written with standard
Beamer commands and Amurmaple's additional layouts, and the colors,
Helvetica-compatible font, bullets, logos, and background patterns are applied
by the theme.

## Start a presentation

1. Upload the project to Overleaf, or open it in your local LaTeX editor.
2. Select **LuaLaTeX** as the compiler and **main.tex** as the main document.
3. Edit the title, author, institute, date, email, webpage, collaboration, and
   slides in `main.tex`.
4. Compile. Open `guide.tex` separately when you want examples to copy.

The starter loads the theme with `\usetheme{WVU}`. Keep `beamerthemeWVU.sty`,
`latexmkrc`, and the complete `styles/` directory beside your presentation file,
along with any figures you use. A local TeX installation also needs Beamer,
Amurmaple, the `svg` package, and their dependencies, available through TeX Live
or MiKTeX. Inkscape is needed for the automatic SVG conversion.

| File | Use |
| --- | --- |
| `main.tex` | A short starter for your own presentation |
| `guide.tex` | Beamer and Amurmaple examples with the WVU theme |
| `examples/` | Individual guide sections and reusable slide layouts |
| `beamerthemeWVU.sty`, `styles/` | Theme implementation and bundled artwork |
| `latexmkrc` | Compiler settings and automatic SVG conversion |
| `beamer-amurmaple-doc.pdf` | The original Amurmaple manual |

The artwork is stored as SVG files in `styles/patterns/` and `styles/tags/`.
These files are converted to PDF at compile time, so no PDF copies need to be
prepared.

## Write your slides

Set the presentation information in your document's preamble:

```latex
\documentclass[aspectratio=169,10pt]{beamer}
\usetheme{WVU}

\title[Short title]{Presentation title}
\subtitle{Optional subtitle}
\author[Short name]{Your name}
\institute[WVU]{West Virginia University}
\date{\today}
\mail{you@mail.wvu.edu}
\webpage{https://example.org}
\collaboration{Your collaboration}
```

The optional short forms in square brackets are used in the sidebar. Put
`\maketitle` immediately after `\begin{document}` for the title slide, which is
drawn without the sidebar navigation and slide number.

Amurmaple's contact commands are set in the starter. `\mail` prints your email on
the title slide and along the right edge of ordinary slides. `\webpage` adds a
website to the title slide, and `\collaboration` adds a line below the title and
subtitle. Replace the sample values with your own. An empty value, such as
`\mail{}`, removes that detail.

Each `frame` is one slide, and each `\section` adds an entry to the sidebar
navigation. Normal Beamer lists and blocks are used in each frame:

```latex
\section{Results}
\begin{frame}{Main result}
  \begin{itemize}
    \item State the finding.
    \item Explain the evidence.
  \end{itemize}
  \begin{block}{Takeaway}
    State what the audience should remember.
  \end{block}
\end{frame}
```

Use `enumerate` for numbered lists, `columns` for side-by-side material, and
`\includegraphics` for figures. `alertblock` and `exampleblock` take a required
title just like `block`. Standard mathematical environments such as `theorem`,
`definition`, and `proof` are also styled by the theme. Each environment has a
fixed accent color, listed in [the brand notes](docs/BRAND_NOTES.md), so choose
each environment by its meaning in the talk.

Beamer features such as `\pause`, overlay specifications like `\item<2->`,
`\note{...}`, `\tableofcontents`, and navigation buttons work normally.
Code listings or verbatim text require `\begin{frame}[fragile]{Title}`.
These features are shown in the guide, and the full syntax is given in the
[Beamer manual](https://ctan.org/pkg/beamer).

## Use Amurmaple's additions

The WVU theme keeps the following Amurmaple commands and environments:

| Feature | Usage |
| --- | --- |
| Information callout | `\begin{information}[Optional title] ... \end{information}` |
| Remark | `\begin{remark}[Optional label] ... \end{remark}` |
| Attributed quotation | `\begin{quotation}[Author] ... \end{quotation}` |
| Heading in a slide | `\framesection{Heading}` |
| Boxed inline emphasis | `\boxalert{Important text}` |
| Divider with contents | `\sepframe[title={Results}]` |
| Closing slide | `\thanksframe{Questions and discussion}` |

`\sepframe` and `\thanksframe` create their own slides and are placed between
frames. Without a `title` option, `\sepframe` uses the current section name. The
closing slide reuses the title graphic.

More examples are given in [the bundled Amurmaple manual](beamer-amurmaple-doc.pdf)
and on [CTAN](https://ctan.org/pkg/beamerthemeamurmaple). The `WVU` theme loads
Amurmaple itself and then applies the WVU styling, so only `\usetheme{WVU}` is
needed.

Amurmaple's layout options are also accepted by the WVU theme:

| Option | Effect |
| --- | --- |
| `nogauge` | Hide the progress gauge |
| `nomail` | Hide the right-margin email while keeping it on the title |
| `sidebarwidth=64pt` | Change the sidebar width (default: 58pt) |
| `toplogo` | Move the sidebar logo to the top |
| `leftframetitle` | Align frame titles to the left |

Options are given in the theme line, for example
`\usetheme[toplogo,sidebarwidth=64pt]{WVU}`. By default, the margin email and
progress gauge are shown, the logo is at the bottom, and frame titles are on the
right.

## Optional presentation settings

The pattern and the navigation sidebar are turned off with this theme line:

```latex
\usetheme[pattern=none,sidebar=false]{WVU}
```

The default pattern is Topo - Solid (`topo-solid`, also accepted as `topo`), and
`none` gives a plain panel. Both options are shown in the guide. The artwork
folder holds `topo-blue.svg`, `topo-gold.svg`, and `topo-white.svg`, and the
theme uses the white variant on its blue panels.

The GWAC SVG is the default title and closing graphic. Its size is set in the
preamble:

```latex
\wvusetup{
  logo-width=6.5cm
}
```

A different SVG is set with `logo=path/to/your-logo.svg`, and `logo=none` removes
the title and closing graphic. The standard `\titlegraphic{...}` command also
works for custom content or other image formats. After the pattern is turned
off, `\wvusetup{pattern=topo-solid}` restores it. A change made in a TeX group
applies only to that group.

The `email`, `website`, and `collaboration` keys in `\wvusetup` are aliases for
Amurmaple's `\mail`, `\webpage`, and `\collaboration` commands.

The theme also adds WVU commands such as `\wvuheading{Heading}`, `\wvuarrow`,
`\wvulocation{Place}`, `\wvupoi{Point of interest}`, and
`\wvuqr[2.5cm]{https://example.org}{Paper and slides}`. The WVU extras section
of the guide shows the patterns, tags, and QR code in context.

## Build locally or on Overleaf

On Overleaf, compile `main.tex` for your talk or select `guide.tex` as the main
document to browse the examples. Both use LuaLaTeX.

From the project directory, build locally with:

```sh
latexmk -lualatex -file-line-error -halt-on-error -interaction=nonstopmode main.tex
latexmk -lualatex -file-line-error -halt-on-error -interaction=nonstopmode guide.tex
```

The outputs are `main.pdf` and `guide.pdf`. The logos, tags, and topo patterns
are SVG files, which are converted to PDF through Inkscape by the `svg` package
during compilation. The shell escape that this conversion needs is set in
`latexmkrc`. A local build also needs the `inkscape` command on your PATH.

The converted files in `svg-inkscape/` are a build cache and are not edited or
distributed. The theme finds its own support files. For the older
`\usepackage{amurmaplewvu}` entry point, `latexmkrc` also adds `styles/` to the
TeX search path.

Both documents are built by the **Build template** workflow in GitHub Actions,
and the PDFs are uploaded as the **wvu-beamer-example** and **wvu-beamer-guide**
artifacts for 14 days. The compiled slides should still be checked by eye for
readable text, spacing, and image proportions.

## Sources

This is a WVU adaptation of Maxime Chupin's
[Amurmaple theme](https://ctan.org/pkg/beamerthemeamurmaple), with TeX Gyre Heros
for portable Helvetica-compatible text. The attribution of the reference example
is kept in `guide.tex`.

The brand references are WVU's
[visual identity](https://scm.wvu.edu/brand/visual-identity/) and
[Design System cheat sheet](https://designsystem.wvu.edu/utilities/cheat-sheet/).
The artwork sources and their preparation are described in
[the artwork notes](docs/ARTWORK.md). The color of each environment and the
reasons for it are recorded in [the brand notes](docs/BRAND_NOTES.md).

## Colors in scientific figures

`styles/beamercolorthemewvu.sty` is the palette source for the DTV papers,
PilotProxy, RFIsher, and RadioFisher. Standalone Python or TeX copies are
exported with:

```bash
python3 tools/export_plot_palette.py --python ../dtv-rs/figsrc/wvu_palette.py
python3 tools/export_plot_palette.py --tex ../dtv-rs/figsrc/wvu_palette.tex
```

With `--check`, each copy is compared with a fresh export of the palette
source and left unchanged. Several `--python` and `--tex` paths can be given in
one run. The copies need no Beamer installation, and the Python copy imports
its plotting packages only when `sequential_cmap()` or `plot_rcparams()` is
called.

In the Python copy, measurements are drawn in WVU Blue (`MEASURED`), and model
curves and small labels in Old Gold (`MODEL`). Bright WVU Gold has too little
contrast for small text on white, so it is used for fills and highlights.
Further series take the other named WVU colors in the order of `SERIES`, with
markers, line styles, or direct labels as a second cue.

The blue intensity scale from `sequential_cmap()` has monotonically decreasing
lightness and is meant for ordered values. Binary masks stay in grayscale, and a
diverging or cyclic quantity is given a diverging or cyclic scale. Journal
requirements and scientific readability take priority over the brand colors.
Typography, figure dimensions, normalizations, and scientific inputs are set by
each figure script and are independent of the palette.
