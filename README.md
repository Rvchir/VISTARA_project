# VISTARA — Stadium Ticket Booking & Interactive 3D Seat Preview

A complete, modern frontend football stadium ticket booking web platform and procedural 3D stadium seat preview application. Built with semantic HTML, modern responsive CSS, and Three.js WebGL graphics — with **zero backend dependencies**.

---

## 🏟 Experiences Included

1. **Interactive 3D Stadium Experience (`view3d.html`):**
   - Procedural WebGL 3D football stadium built with Three.js.
   - Interactive camera orbit and seat-level fly-in preview.
   - Match perspective from thousands of individual seats across 4 tiers.
   - Real-time seat quality scoring, audio crowd atmosphere, and client-side digital ticket generation with QR code via jsPDF.

2. **VISTARA 7-Page Supporter Ticket Booking Flow (`index.html`):**
   - **`index.html`** — Homepage featuring the stadium seating bowl hero linking directly into seat picking.
   - **`fixtures.html`** — Complete fixture listings with league & cup competition filters.
   - **`event.html`** — Match details with interactive SVG seating bowl and 3D preview link.
   - **`seats.html`** — Interactive seat-level picker with live totals calculated using CSS counters.
   - **`checkout.html`** — Demonstration checkout form with order summary and payment selection.
   - **`confirmation.html`** — Matchday ticket stub with entry code and gate details.
   - **`track.html`** — Order lookup, ticket delivery schedules, and ground regulations.

---

## 🚀 Quick Start

No Node.js, no MongoDB, no build step, and no package installation required.

### Option 1: Open directly in your browser
Simply double-click `index.html` (or `view3d.html`) to launch in any modern browser (Chrome, Firefox, Safari, Edge).

### Option 2: Run a local static server
```bash
# Using Python
python3 -m http.server 8000

# Or using npx
npx serve .
```
Then navigate to `http://localhost:8000`.

---

## 🛠 Project Structure

```
.
├── index.html            # Main landing page
├── fixtures.html         # Fixture listings
├── event.html            # Match details & SVG seating bowl
├── seats.html            # Block seat picker with live counter arithmetic
├── checkout.html         # Order checkout
├── confirmation.html     # Ticket confirmation stub
├── track.html            # Order lookup & delivery info
├── view3d.html           # 3D Three.js WebGL Stadium exploration
├── css/
│   ├── tokens.css        # Design tokens: palette, type scale, radii, spacing
│   ├── base.css          # Reset, typography, navigation, layout
│   ├── components.css    # Buttons, fixtures, offer stubs, forms, bowl SVG styling
│   ├── seatmap.css       # Seating grid, selection states, counter math
│   └── _blocks.css       # Generated styles for bowl blocks
├── assets/
│   └── bowl.svg.html     # Interactive SVG seating bowl component
└── tools/
    ├── build_bowl.py     # Regenerates the SVG bowl and _blocks.css
    └── build_site.py     # Regenerates the static HTML pages
```

---

## 💡 Frontend Architecture Highlights

- **CSS Counter Arithmetic:** On `seats.html`, seat count and money totals are computed entirely in CSS without JavaScript:
  ```css
  .zone--mid .seat input:checked + label { counter-increment: picked 1 subtotal 12000 fees 150 total 12150; }
  .tally__total::after { content: "₹" counter(total); }
  ```
- **CSS `:target` State Switching:** Block switching uses URI fragments (`seats.html#b214`) to swap active blocks using `:target` selector chains.
- **Procedural 3D Graphics:** `view3d.html` builds an entire 60,000+ seat stadium geometry procedurally using Three.js instanced meshes for 60fps rendering in WebGL.
