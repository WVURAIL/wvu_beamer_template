# WVU Beamer template

Write a presentation with standard Beamer commands and Amurmaple's additional
layouts. The WVU theme supplies the colors, Helvetica-compatible font, bullets,
logos, and background patterns automatically.

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
or MiKTeX. Install Inkscape for automatic SVG conversion.

| File | Use |
| --- | --- |
| `main.tex` | A short starter for your own presentation |
| `guide.tex` | Beamer and Amurmaple examples with the WVU theme |
| `examples/` | Individual guide sections and reusable slide layouts |
| `beamerthemeWVU.sty`, `styles/` | Theme implementation and bundled artwork |
| `latexmkrc` | Compiler settings and automatic SVG conversion |
| `beamer-amurmaple-doc.pdf` | The original Amurmaple manual |

Artwork is organized in `styles/patterns/` and `styles/tags/`. The theme handles
it automatically; you do not need to prepare separate PDF copies.

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

The optional short forms fit the sidebar. Use `\maketitle` immediately after
`\begin{document}` for the title slide. It automatically omits the sidebar
navigation and slide number.

Amurmaple's contact features are enabled in the starter: `\mail` puts your email
on the title and along the right side of ordinary slides; `\webpage` adds the
title-page website; `\collaboration` adds a line beneath the title and subtitle.
Replace the sample values with your own. An empty value, such as `\mail{}`,
omits that detail.

A `frame` is a slide; `\section` organizes the navigation. Use normal Beamer
lists and blocks inside each frame:

```latex
\section{Results}
\begin{frame}{The key result}
  \begin{itemize}
    \item State the finding.
    \item Explain the evidence.
  \end{itemize}
  \begin{block}{Takeaway}
    Explain why the result matters.
  \end{block}
\end{frame}
```

Use `enumerate` for numbered lists, `columns` for comparisons, and
`\includegraphics` for figures. `alertblock` and `exampleblock` take a required
title just like `block`. Standard mathematical environments such as `theorem`,
`definition`, and `proof` are also styled automatically. Choose each environment
for what it means in your talk.

Beamer features such as `\pause`, overlay specifications like `\item<2->`,
`\note{...}`, `\tableofcontents`, and navigation buttons work normally.
Code listings or verbatim text require `\begin{frame}[fragile]{Title}`.
The guide demonstrates these features; the
[Beamer manual](https://ctan.org/pkg/beamer) covers the full syntax.

## Use Amurmaple's additions

The WVU theme retains these useful Amurmaple commands and environments:

| Feature | Usage |
| --- | --- |
| Information callout | `\begin{information}[Optional title] ... \end{information}` |
| Remark | `\begin{remark}[Optional label] ... \end{remark}` |
| Attributed quotation | `\begin{quotation}[Author] ... \end{quotation}` |
| Heading within a slide | `\framesection{Heading}` |
| Boxed inline emphasis | `\boxalert{Important text}` |
| Divider with contents | `\sepframe[title={Results}]` |
| Closing slide | `\thanksframe{Questions and discussion}` |

Put `\sepframe` and `\thanksframe` between frames; they create their own slides.
Without a `title` option, `\sepframe` uses the current section name. The closing
slide reuses the title graphic.

See [the bundled Amurmaple manual](beamer-amurmaple-doc.pdf) and
[Amurmaple on CTAN](https://ctan.org/pkg/beamerthemeamurmaple) for more examples.
Load `WVU` as your theme; it loads Amurmaple and applies the WVU styling.

Amurmaple's layout controls also work in the WVU theme options:

| Option | Effect |
| --- | --- |
| `nogauge` | Hide the progress gauge |
| `nomail` | Hide the right-margin email while keeping it on the title |
| `sidebarwidth=64pt` | Change the sidebar width (default: 58pt) |
| `toplogo` | Move the sidebar logo to the top |
| `leftframetitle` | Align frame titles to the left |

For example, replace the theme line with
`\usetheme[toplogo,sidebarwidth=64pt]{WVU}`. The default keeps the margin email
and progress gauge visible, with the logo at the bottom and frame titles on
the right.

## Optional presentation settings

The defaults work without extra configuration. To change the pattern or hide
the navigation sidebar, replace the theme line with:

```latex
\usetheme[pattern=pinstripes,sidebar=false]{WVU}
```

The default pattern is **Topo - Solid** (`topo-solid`). Other selectors are
`pinstripes`, `distressed-lines`, `rolling-hills`, `topo-dashed`,
`topo-morgantown`, and `none`. The guide shows each pattern.

The GWAC SVG is the default title and closing graphic. To adjust its size,
add this to the preamble:

```latex
\wvusetup{
  logo-width=6.5cm
}
```

Every setting is optional. Use `logo=path/to/your-logo.svg` for a different SVG
or `logo=none` to omit the title and closing graphic. Standard
`\titlegraphic{...}` also works for custom content or other image formats.
Change the pattern later with `\wvusetup{pattern=rolling-hills}`; a change
inside a TeX group applies only within that group.

The `email`, `website`, and `collaboration` keys in `\wvusetup` remain aliases
for Amurmaple's `\mail`, `\webpage`, and `\collaboration` commands.

WVU extras include `\wvuheading{Heading}`, `\wvuarrow`,
`\wvulocation{Place}`, `\wvupoi{Point of interest}`, and
`\wvuqr[2.5cm]{https://example.org}{Paper and slides}`. The guide's WVU extras
section shows the patterns, tags, and QR examples in context.

## Build locally or on Overleaf

On Overleaf, compile `main.tex` for your talk or select `guide.tex` as the main
document to browse the examples. Both use LuaLaTeX.

From the project directory, build locally with:

```sh
latexmk -lualatex -file-line-error -halt-on-error -interaction=nonstopmode main.tex
latexmk -lualatex -file-line-error -halt-on-error -interaction=nonstopmode guide.tex
```

The outputs are `main.pdf` and `guide.pdf`. Logos, tags, and solid-topo patterns
use SVG sources. Four textures supplied by WVU as raster artwork remain PNGs.
The `svg` package converts the SVGs through Inkscape during compilation;
`latexmkrc` enables the required shell escape automatically. For a local build,
make sure the `inkscape` command is available on your PATH. Generated files in
`svg-inkscape/` are a build cache and do not need to be edited or distributed.
The theme finds its support files itself; `latexmkrc` also preserves support
for the older `\usepackage{amurmaplewvu}` entry point.

GitHub Actions builds both documents. After a successful **Build template** run,
the **wvu-beamer-example** and **wvu-beamer-guide** artifacts contain the PDFs.
Check the compiled slides for readable text, spacing, and image proportions.

## Sources

This is a WVU adaptation of Maxime Chupin's
[Amurmaple theme](https://ctan.org/pkg/beamerthemeamurmaple), with TeX Gyre Heros
for portable Helvetica-compatible text. The reference example's attribution
is retained in `guide.tex`.

WVU's [visual identity](https://scm.wvu.edu/brand/visual-identity/) and
[Design System cheat sheet](https://designsystem.wvu.edu/utilities/cheat-sheet/)
provide the brand references. Artwork sources and preparation details are in
[the artwork notes](docs/ARTWORK.md). Optional maintainer details
are in [the brand notes](docs/BRAND_NOTES.md).
