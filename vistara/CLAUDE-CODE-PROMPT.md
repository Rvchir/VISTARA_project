# Prompt for Claude Code

Paste this into Claude Code from the unzipped `vistara/` directory.

---

You are working on VISTARA, a stadium ticket booking site built with **HTML and CSS only**.
No JavaScript, no frameworks, no build step, no npm. Everything must work by opening
`index.html` directly from the filesystem.

Read `README.md` first — it documents the seven pages, the CSS file split, and the
three CSS-only techniques the site depends on (checkbox seat selection, CSS counters for
running totals, `:target` for switching the displayed block).

## Hard rules

1. No `<script>` tags, no inline event handlers, no `javascript:` URLs. If a feature
   cannot be done in CSS, say so plainly and propose the closest CSS-only alternative
   rather than reaching for script.
2. Design tokens live in `css/tokens.css`. Do not hardcode colours, font sizes or
   spacing anywhere else — use the custom properties.
3. `css/_blocks.css` is generated. Do not hand-edit it; change `tools/build_bowl.py`
   and re-run it.
4. Keep every interactive control reachable by keyboard, with a visible focus ring.
   Labels stay tied to inputs with `for`/`id`.
5. Keep the pages working down to a 360px viewport.
6. Clubs, grounds and prices are invented. Keep it that way — do not put real club or
   competition names into the markup.

## How to work

- After changing anything, check the affected pages render correctly and report what
  you verified. Flag anything you could not verify.
- Prefer editing `tools/build_site.py` and re-running it over hand-editing seven HTML
  files, so the masthead, nav and footer stay identical across pages.
- Keep CSS selector specificity flat; the existing sheets rely on single-class selectors.
- Commit in small, described steps if the directory is a git repo.

## First task

Work through this list in order, pausing after each item for review:

1. Read every file and give me a short map of what is where, plus anything you think is
   broken or inconsistent.
2. Add a **`venue.html`** page: one ground, the full bowl, capacity and access
   information, and a list of upcoming fixtures there. Reuse existing components.
3. On `seats.html`, add a CSS-only "best available" shortcut — a radio group that
   pre-highlights a run of adjacent free seats in each price zone.
4. Add a print stylesheet so `confirmation.html` prints as a clean ticket on one page.
5. Add a `css/print.css` and a dark-mode block using `prefers-color-scheme`, driven
   entirely by overriding the tokens.

Start with item 1 and wait for my go-ahead before item 2.
