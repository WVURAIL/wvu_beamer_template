# Brand notes for maintainers

Presentation authors do not need to configure colors. Use the environments shown in [the README](../README.md) and `guide.tex`; styling is automatic. These notes record the template's design choices.

The theme uses the WVU palette already defined in `styles/beamercolorthemewvu.sty`. The default mappings are Woodburn for alerts, Hemlock for information, and Old Gold for examples. Every box family has a distinct accent; pale accents use Coal text, and dark accents use Not Quite White text.

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

The [State Partners toolkit](https://scm.wvu.edu/brand/tools-and-downloads/audience-toolkits/#state-partners) guides which colors to use first, without excluding the rest of WVU's approved palette. The frequent `block`, `alertblock`, `exampleblock`, `information`, and `remark` environments all use colors included in that toolkit. Wild Flour takes priority for remarks; Sunset remains available as the distinct accent for the less common `fact` environment. This frequency-based assignment is a template choice, not an official environment mapping.

The 14 secondary and neutral colors cover the 14 box families; proofs use primary WVU Gold. Plural names and Beamer's capitalized or German compatibility names retain the corresponding semantic family's color. An `example` deliberately matches an `exampleblock`.

Normal text is Coal, page backgrounds are Not Quite White, and the main structure remains WVU Blue and Gold. Sidebar text, buttons, lists, notes, bibliography text, and the theme's hard-coded gray details also use named palette colors. Box bodies use Not Quite White except for the inverted `solution` body. The existing inline alert uses Woodburn text on Wild Flour.

Maintainers can find the semantic mappings in `styles/beamercolorthemewvu.sty`. The optional `examples/01-brand-hierarchy.tex` preserves the palette gallery; it is not included in the user guide. The public starter needs no color configuration.

Imported logo artwork keeps its original colors. QR codes retain pure white for their functional background and quiet zone. Pattern opacity creates tonal variation from the approved base colors. These are separate from the theme's explicit text, box, and interface color choices.

Palette reference: [WVU visual identity](https://scm.wvu.edu/brand/visual-identity/).

Names follow the [WVU Design System cheat sheet](https://designsystem.wvu.edu/utilities/cheat-sheet/): `wvu-blue`, `wvu-gold`, and the `wvu-` prefixed, hyphenated secondary and neutral names (for example, `wvu-wild-flour` and `wvu-not-quite-white`). Earlier compact names remain aliases. Official display labels include Topo - Solid, Topo - Dashed, Topo - Morgantown, Corner Slashes, and POIs. The template's LaTeX commands wrap these assets; they are not WVU website utility classes.

RGB values retain the SCM visual identity palette. The Design System pages differ for Gold and Coal, and their printed Seneca Gray value differs from their own CSS; this naming update deliberately keeps the established SCM values. Primary/secondary/tertiary usage priorities in the optional gallery are local presentation choices; WVU's official palette groups are Primary, Secondary, and Neutral.
