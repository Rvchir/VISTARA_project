# VISTARA — stadium ticket booking (HTML + CSS only)

A working seven-page booking flow for football tickets. No JavaScript runs anywhere
on the site: selection, totals, dropdowns and view-switching are all done with CSS.

Open `index.html` in a browser. Nothing to install, nothing to build.

## The flow

| Page | What it does |
| --- | --- |
| `index.html` | Home. The seating bowl is the hero — every block links straight into the seat picker. |
| `fixtures.html` | All fixtures, with filter controls. |
| `event.html` | One fixture: listings on the left, interactive seating plan on the right. |
| `seats.html` | Seat-level picker for a block, with live counts and money totals. |
| `checkout.html` | Buyer details, delivery choice, payment form, order summary. |
| `confirmation.html` | Ticket stub with entry code. |
| `track.html` | Order lookup, delivery table, refund rules. |

## Files

```
index.html  fixtures.html  event.html  seats.html
checkout.html  confirmation.html  track.html
css/
  tokens.css      colour, type scale, spacing — change the brand here
  base.css        reset, typography, masthead, nav, footer
  components.css  buttons, fixtures, offer stubs, filters, forms, the bowl SVG styling
  seatmap.css     the seat grid, selection states, counter maths
  _blocks.css     generated — 68 rules, one per block on the bowl
assets/
  bowl.svg.html   the seating-plan SVG, pasted into index.html and event.html
tools/
  build_bowl.py   regenerates the bowl SVG and _blocks.css
  build_site.py   regenerates all seven pages from the data at the top of the file
```

## How the no-JavaScript parts work

**Seat selection** — every free seat is a hidden `<input type="checkbox">` with a styled
`<label>`. `:checked` paints it amber. Sold seats are plain `<span>`s with no input, so
they cannot be picked by mouse or keyboard.

**Live totals** — CSS counters do the arithmetic:

```css
.zone--mid .seat input:checked + label { counter-increment: picked 1 subtotal 12000 fees 150 total 12150; }
.tally__total::after { content: "₹" counter(total); }
```

The tally bar sits after the grid in the DOM, so it reads the accumulated values. Four
seats across two price zones really does add up correctly.

**Empty and disabled states** — `.seatwrap:not(:has(.seat input:checked))` shows the
prompt and greys out the continue button until something is selected.

**Block switching** — each block on the bowl links to `seats.html#b214`. Hidden anchors
sit before `<main>`, so `#b214:target ~ .seatwrap .blk-name::after { content: "214" }`
swaps the heading. That is what `_blocks.css` contains, one rule set per block.

**Nav dropdowns** — `li:hover > .submenu, li:focus-within > .submenu { display: flex }`,
so they open on keyboard focus too.

## What CSS alone cannot do

These are honest gaps, not bugs:

- Prices are fixed per zone. A genuinely variable price needs script or a server.
- CSS `counter()` output has no thousands separator, so the tally bar reads e.g. "₹19250"
  rather than "₹19,250". Fixing that needs script or a server-rendered value.
- Selections do not survive the jump to `checkout.html`; that page shows a fixed example
  order. Carrying them across needs a form POST and a backend.
- No cap on how many seats can be picked at once.
- No real search, no real payment, no live availability.

## Design notes

Palette is a floodlit pitch: deep grass-black `#0D2A20`, chalk paper `#EEF1EB`,
floodlight amber `#F5B93F`, terrace claret `#7A1E3C`. Headings are Archivo, body is
Spline Sans, seat numbers are Spline Sans Mono so the grid lines up. The offer cards
carry a perforated ticket-stub edge; that is the one decorative flourish, everything
else is hairline borders and flat fills.

Fonts load from Google Fonts. Offline, the system fallbacks in `tokens.css` take over.

Clubs, grounds, fixtures and prices are invented. Prices are in Indian Rupees (₹),
ranging roughly ₹2,000 to ₹30,000 a seat.

## Regenerating

```bash
python3 tools/build_bowl.py   # bowl SVG + _blocks.css
python3 tools/build_site.py   # all seven pages
```

Edit the `FIXTURES` and `OFFERS` lists at the top of `build_site.py` to change content.
