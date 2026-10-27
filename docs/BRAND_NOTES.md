# Brand notes for maintainers

These notes record the template's design choices for maintainers. Presentation authors need no color configuration, since each environment shown in [the README](../README.md) and `guide.tex` takes its color from the theme.

The theme uses the WVU palette defined in `styles/beamercolorthemewvu.sty`. By default, alerts are Woodburn, information is Hemlock, and examples are Old Gold. Each box family has its own accent. Pale accents take Coal text, and dark accents take Not Quite White text.

| Environment or command | Accent | Hex |
| --- | --- | --- |
| `block` | Safety Blue | `#0062A3` |
| `alertblock`, `\alert`, `\boxalert` | Woodburn | `#8D4638` |
| `exampleblock`, `example`, `examples` | Old Gold | `#7F6310` |
| `information` | Hemlock | `#6A724F` |
| `remark` | Wild Flour | `#F2E6C2` |
| `abstract` | Star City Blue | `#9DDAE6` |
| `quotation` | Buckskin | `#B3A169` |
| `theorem` | Rattler Gray | `#554741` |
| `definition`, `definitions` | Canary | `#F7DD63` |
| `corollary` | Coopers Gray | `#BEB7B3` |
| `lemma` | Seneca Gray | `#988E8B` |
| `fact` | Sunset | `#F58672` |
| `problem` | Coal | `#1C2B39` |
| `solution` | Not Quite White, with a Coal body | `#F7F7F7` |
| `proof` | WVU Gold | `#EEAA00` |

The [State Partners toolkit](https://scm.wvu.edu/brand/tools-and-downloads/audience-toolkits/#state-partners) guides which colors are used first, and the rest of WVU's approved palette stays available. The most frequent environments, `block`, `alertblock`, `exampleblock`, `information`, and `remark`, all take colors from that toolkit. For this reason Wild Flour is given to remarks, and Sunset is kept as the accent of the less common `fact` environment. WVU does not assign colors to Beamer environments, so this assignment by frequency is a template choice.

Each of the 14 secondary and neutral colors is given to one of the 14 box families, and proofs use the primary WVU Gold. Plural names and Beamer's capitalized or German compatibility names take the color of their family, and `example` takes the color of `exampleblock`.

Normal text is Coal, page backgrounds are Not Quite White, and the main structure is WVU Blue and Gold. Sidebar text, buttons, lists, notes, bibliography text, and the gray details hard-coded in Amurmaple also use named palette colors. Except for the inverted `solution` body, box bodies are Not Quite White. For the inline alert, Woodburn text is set on Wild Flour.

These mappings are defined in `styles/beamercolorthemewvu.sty`. The palette gallery is kept in the optional `examples/01-brand-hierarchy.tex`, which `guide.tex` does not load.

Imported logo artwork keeps its original colors. QR codes keep pure white for their background and quiet zone, which a scanner needs. The tonal variation of the patterns comes from opacity applied to the approved base colors. These three cases are not covered by the text, box, and interface colors above.

Palette values are taken from the [WVU visual identity](https://scm.wvu.edu/brand/visual-identity/).

Color names follow the [WVU Design System cheat sheet](https://designsystem.wvu.edu/utilities/cheat-sheet/), with `wvu-blue`, `wvu-gold`, and hyphenated secondary and neutral names under the `wvu-` prefix (such as `wvu-wild-flour` and `wvu-not-quite-white`). The earlier compact names are kept as aliases. WVU's official display labels for its artwork, such as Topo - Solid, Topo - Dashed, Topo - Morgantown, Corner Slashes, and POIs, are used as written. The template's LaTeX commands draw these assets and are not WVU website utility classes.

The RGB values are those of the SCM visual identity palette. The Design System pages give different values for Gold and Coal, and their printed Seneca Gray differs from their own CSS, so the SCM values are kept. The primary, secondary, and tertiary priorities in the gallery are local presentation choices. WVU's official palette groups are Primary, Secondary, and Neutral.
