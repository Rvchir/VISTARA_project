import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
BOWL = (ROOT / "assets" / "bowl.svg.html").read_text()

FONTS = (
    '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
    '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
    '<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&'
    'family=Spline+Sans:wght@400;500;600&family=Spline+Sans+Mono:wght@400;600&display=swap" rel="stylesheet">'
)


def head(title, desc, extra_css=()):
    css = ['css/tokens.css', 'css/base.css', 'css/components.css'] + list(extra_css)
    links = "\n  ".join(f'<link rel="stylesheet" href="{c}">' for c in css)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} · VISTARA</title>
  <meta name="description" content="{desc}">
  {FONTS}
  {links}
</head>
<body>
<a class="skip" href="#main">Skip to main content</a>
"""


def masthead(current):
    def cur(page):
        return ' aria-current="page"' if page == current else ''
    return f"""
<header class="masthead">
  <div class="shell masthead__bar">
    <a class="wordmark" href="index.html">VISTARA<span>See the game from the right seat</span></a>
    <form class="searchbar" action="fixtures.html" method="get" role="search">
      <label class="visually-hidden" for="q">Search clubs, fixtures or grounds</label>
      <input id="q" name="q" type="text" placeholder="Club, fixture or ground">
      <button type="submit">Search</button>
    </form>
    <div class="masthead__aside">
      <a class="btn btn--ghost btn--sm" href="track.html">Find my order</a>
    </div>
  </div>
  <nav class="nav" aria-label="Primary">
    <div class="shell">
      <ul>
        <li><a href="index.html"{cur('home')}>Home</a></li>
        <li><a href="fixtures.html"{cur('fixtures')}>Fixtures</a></li>
        <li>
          <a href="fixtures.html#competitions">Competitions</a>
          <ul class="submenu">
            <li><a href="fixtures.html">Indian Super League</a></li>
            <li><a href="fixtures.html">Durand Cup</a></li>
            <li><a href="fixtures.html">AFC Champions League Two</a></li>
            <li><a href="fixtures.html">Indian Women's League</a></li>
          </ul>
        </li>
        <li>
          <a href="event.html">Grounds</a>
          <ul class="submenu">
            <li><a href="event.html">Mumbai Football Arena</a></li>
            <li><a href="event.html">Kaloor International Stadium</a></li>
            <li><a href="event.html">Fatorda Stadium</a></li>
            <li><a href="event.html">Sree Kanteerava Stadium</a></li>
          </ul>
        </li>
        <li>
          <a href="track.html">Help</a>
          <ul class="submenu">
            <li><a href="track.html">Track an order</a></li>
            <li><a href="track.html#delivery">Ticket delivery</a></li>
            <li><a href="track.html#refunds">Refunds</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </nav>
</header>

<div class="assurance">
  <div class="shell">
    <span><b>4.7 / 5</b> from 21,212 supporters</span>
    <span>Selling seats since <b>2006</b></span>
    <span><b>1.2 million</b> fans seated</span>
    <span>Every order covered by the <b>Full House Guarantee</b></span>
  </div>
</div>
"""


FOOTER = """
<footer class="footer">
  <div class="shell">
    <div class="footer__cols">
      <div>
        <a class="wordmark" href="index.html">VISTARA<span>See the game from the right seat</span></a>
      </div>
      <div>
        <h4>Buy</h4>
        <ul>
          <li><a href="fixtures.html">All fixtures</a></li>
          <li><a href="event.html">Seating plans</a></li>
          <li><a href="fixtures.html">Season tickets</a></li>
          <li><a href="event.html">Hospitality boxes</a></li>
        </ul>
      </div>
      <div>
        <h4>Support</h4>
        <ul>
          <li><a href="track.html">Track an order</a></li>
          <li><a href="track.html#delivery">Ticket delivery</a></li>
          <li><a href="track.html#refunds">Refunds and resales</a></li>
          <li><a href="track.html">Accessible seating</a></li>
        </ul>
      </div>
      <div>
        <h4>VISTARA</h4>
        <ul>
          <li><a href="index.html">About us</a></li>
          <li><a href="index.html">Sell with us</a></li>
          <li><a href="index.html">Careers</a></li>
          <li><a href="index.html">Press</a></li>
        </ul>
      </div>
    </div>
    <p class="footer__legal">
      A student project. Clubs, grounds, fixtures and prices are invented for demonstration.
      Built with HTML and CSS only — no JavaScript runs on this site.
    </p>
  </div>
</footer>
</body>
</html>
"""

FIXTURES = [
    ("SAT", "Oct 04", "19:45", "Durand Cup", "Mumbai City FC vs Bengaluru FC", "Mumbai Football Arena, Mumbai", 6200, "cup"),
    ("SAT", "Oct 04", "15:00", "Indian Super League", "Kerala Blasters FC vs Chennaiyin FC", "Kaloor International Stadium, Kochi", 4900, "league"),
    ("SUN", "Oct 05", "16:30", "Indian Super League", "FC Goa vs Mumbai City FC", "Fatorda Stadium, Margao", 7600, "league"),
    ("TUE", "Oct 07", "20:00", "AFC Champions League Two", "Bengaluru FC vs Lion City Sailors FC", "Sree Kanteerava Stadium, Bengaluru", 10800, "cont"),
    ("WED", "Oct 08", "19:45", "Durand Cup", "Chennaiyin FC vs Hyderabad FC", "Jawaharlal Nehru Stadium, Chennai", 3700, "cup"),
    ("SAT", "Oct 11", "12:30", "Indian Super League", "Hyderabad FC vs FC Goa", "GMC Balayogi Athletic Stadium, Hyderabad", 5600, "league"),
    ("SAT", "Oct 11", "17:30", "Indian Women's League", "Mumbai City FC Women vs Kerala Blasters FC Women", "Mumbai Football Arena, Mumbai", 2000, "women"),
    ("SUN", "Oct 12", "14:00", "Indian Super League", "Bengaluru FC vs Kerala Blasters FC", "Sree Kanteerava Stadium, Bengaluru", 7000, "league"),
]


def fixture_row(f, featured=False):
    day, date, time, comp, match, venue, price, _ = f
    d1, d2 = date.split(" ")
    return f"""        <article class="fixture">
          <div class="fixture__date">
            <span>{day}</span>
            <b>{d2}</b>
            <span>{d1} · {time}</span>
          </div>
          <div>
            <p class="fixture__comp">{comp}</p>
            <h3>{match}</h3>
            <p class="fixture__venue">{venue}</p>
          </div>
          <div class="fixture__cta">
            <span class="fixture__from">from</span>
            <a class="btn btn--primary" href="event.html">₹{price:,}</a>
          </div>
        </article>
"""


# ---------------------------------------------------------------- index.html
index = head("Football tickets, seat by seat", "Pick your exact seat for Indian Super League and cup football. Interactive seating plans, clear prices.")
index += masthead("home")
index += f"""
<main id="main">

  <section class="hero">
    <div class="shell hero__grid">
      <div>
        <h1>Pick the seat, not just the ticket.</h1>
        <p class="hero__lede">Every ground on VISTARA is mapped block by block, so you know the view and the price before you pay.</p>
        <form class="hero__search" action="fixtures.html" method="get">
          <label class="visually-hidden" for="hero-q">Search clubs, fixtures or grounds</label>
          <input id="hero-q" name="q" type="text" placeholder="Try “Mumbai City FC” or “Mumbai Football Arena”">
          <button type="submit">Search</button>
        </form>
        <div class="hero__quick">
          <a href="fixtures.html">This weekend</a>
          <a href="fixtures.html">Under ₹7,500</a>
          <a href="event.html">Hospitality</a>
          <a href="seats.html">Accessible seats</a>
        </div>
      </div>
      <figure class="hero__bowl">
        {BOWL}
        <figcaption>Mumbai Football Arena, Mumbai — 62,400 seats. Choose a block to start.</figcaption>
      </figure>
    </div>
  </section>

  <section class="section shell">
    <div class="section__head">
      <h2>Going fast this week</h2>
      <p>Prices are per seat and include the booking fee at checkout.</p>
    </div>
    <div class="tiles">
      <a class="tile tile--a" href="fixtures.html">
        <p class="tile__kicker">League football</p>
        <strong>Indian Super League</strong>
        <span class="meta">18 fixtures · from ₹3,700</span>
      </a>
      <a class="tile tile--b" href="fixtures.html">
        <p class="tile__kicker">Knockout</p>
        <strong>Durand Cup</strong>
        <span class="meta">6 fixtures · from ₹2,000</span>
      </a>
      <a class="tile tile--c" href="fixtures.html">
        <p class="tile__kicker">Continental nights</p>
        <strong>AFC Champions League Two</strong>
        <span class="meta">4 fixtures · from ₹10,800</span>
      </a>
      <a class="tile tile--d" href="fixtures.html">
        <p class="tile__kicker">Matchday extras</p>
        <strong>Hospitality boxes</strong>
        <span class="meta">Seats 8 · from ₹30,000</span>
      </a>
    </div>
  </section>

  <section class="section shell">
    <div class="promise">
      <div>
        <h2>What you get for the price</h2>
        <p>No surprise fees at the last screen, and a seat map that matches the ground you walk into.</p>
        <a class="btn btn--dark" href="fixtures.html">Browse fixtures</a>
      </div>
      <div class="promise__list">
        <div>
          <b>Full House Guarantee</b>
          <p>If your seats do not arrive, we replace them or refund you in full.</p>
        </div>
        <div>
          <b>The seat you picked</b>
          <p>Block, row and seat number are locked in the moment you check out.</p>
        </div>
        <div>
          <b>Tickets on your phone</b>
          <p>Delivered to your email up to 48 hours before kick-off.</p>
        </div>
      </div>
    </div>
  </section>

  <section class="section shell" id="competitions">
    <div class="listing">
      <div>
        <div class="section__head">
          <h2>Next fixtures</h2>
          <p><a class="textlink" href="fixtures.html">See all 34</a></p>
        </div>
        <div class="fixtures">
{''.join(fixture_row(f) for f in FIXTURES[:5])}        </div>
      </div>
      <aside>
        <div class="section__head"><h2>By club</h2></div>
        <ul class="index-list">
          <li><a href="fixtures.html">Mumbai City FC <span>7 fixtures</span></a></li>
          <li><a href="fixtures.html">Bengaluru FC <span>6 fixtures</span></a></li>
          <li><a href="fixtures.html">Kerala Blasters FC <span>5 fixtures</span></a></li>
          <li><a href="fixtures.html">FC Goa <span>5 fixtures</span></a></li>
          <li><a href="fixtures.html">Chennaiyin FC <span>4 fixtures</span></a></li>
          <li><a href="fixtures.html">Hyderabad FC <span>4 fixtures</span></a></li>
        </ul>
        <div class="section__head"><h2>By ground</h2></div>
        <ul class="index-list">
          <li><a href="event.html">Mumbai Football Arena <span>62,400</span></a></li>
          <li><a href="event.html">Sree Kanteerava Stadium <span>48,100</span></a></li>
          <li><a href="event.html">Fatorda Stadium <span>41,800</span></a></li>
          <li><a href="event.html">Kaloor International Stadium <span>29,500</span></a></li>
        </ul>
      </aside>
    </div>
  </section>

</main>
"""
index += FOOTER
(ROOT / "index.html").write_text(index)


# ------------------------------------------------------------- fixtures.html
fx = head("Fixtures", "Every fixture on sale, filtered by competition and price.")
fx += masthead("fixtures")
fx += f"""
<main id="main" class="shell section">

  <div class="section__head">
    <h1>Fixtures on sale</h1>
    <p>34 fixtures · updated this morning</p>
  </div>

  <form class="filters">
    <fieldset class="field">
      <legend>Competition</legend>
      <div class="chips">
        <input type="radio" id="c-all" name="comp" checked><label for="c-all">All</label>
        <input type="radio" id="c-lg" name="comp"><label for="c-lg">League</label>
        <input type="radio" id="c-cup" name="comp"><label for="c-cup">Cup</label>
        <input type="radio" id="c-eu" name="comp"><label for="c-eu">Continental</label>
      </div>
    </fieldset>
    <div class="field">
      <label for="when">When</label>
      <select id="when" name="when">
        <option>Any date</option>
        <option>This weekend</option>
        <option>Next 7 days</option>
        <option>Next 30 days</option>
      </select>
    </div>
    <div class="field">
      <label for="ground">Ground</label>
      <select id="ground" name="ground">
        <option>All grounds</option>
        <option>Mumbai Football Arena</option>
        <option>Sree Kanteerava Stadium</option>
        <option>Fatorda Stadium</option>
        <option>Kaloor International Stadium</option>
      </select>
    </div>
    <div class="field">
      <label for="sort">Sort by</label>
      <select id="sort" name="sort">
        <option>Date, soonest first</option>
        <option>Price, lowest first</option>
        <option>Popularity</option>
      </select>
    </div>
  </form>

  <div class="listing">
    <div>
      <div class="fixtures">
{''.join(fixture_row(f) for f in FIXTURES)}      </div>
    </div>
    <aside>
      <div class="section__head"><h2>Cheapest right now</h2></div>
      <ul class="index-list">
        <li><a href="event.html">Mumbai City FC Women vs Kerala Blasters <span>₹2,000</span></a></li>
        <li><a href="event.html">Chennaiyin vs Hyderabad <span>₹3,700</span></a></li>
        <li><a href="event.html">Kerala Blasters vs Chennaiyin <span>₹4,900</span></a></li>
        <li><a href="event.html">Hyderabad vs Goa <span>₹5,600</span></a></li>
      </ul>
      <div class="promise" style="grid-template-columns:1fr">
        <div>
          <h3>Can't find a fixture?</h3>
          <p class="hint">Tickets go on general sale six weeks before kick-off. Leave your email and we will tell you the morning they land.</p>
          <div class="field">
            <label for="alert-email">Email</label>
            <input id="alert-email" type="email" placeholder="you@example.com">
          </div>
          <p></p>
          <a class="btn btn--dark btn--wide" href="fixtures.html">Set a reminder</a>
        </div>
      </div>
    </aside>
  </div>

</main>
"""
fx += FOOTER
(ROOT / "fixtures.html").write_text(fx)


# ---------------------------------------------------------------- event.html
OFFERS = [
    ("Longside Upper, block 214", "bronze", 6200, ["Up to 10 seats together", "Mobile tickets", "Clear view"], "Cheapest in this block", "best"),
    ("Longside Lower, block 108", "silver", 12000, ["Up to 6 seats together", "Mobile tickets", "Behind the dugouts"], None, None),
    ("Halfway Line, block 101", "gold", 19100, ["Up to 4 seats together", "Mobile tickets", "Padded seating"], "3 seats left at this price", "last"),
    ("Hospitality box M04", "box", 30000, ["Seats 8, sold as a whole box", "Includes matchday meal", "Private entrance"], "One box remaining", "last"),
    ("Kop End, block 220", "bronze", 6200, ["Singles only", "Mobile tickets", "Standing-style atmosphere"], None, None),
    ("Halfway Line, block 113", "gold", 20800, ["Up to 2 seats together", "Mobile tickets", "Front six rows"], None, None),
]


def offer(o, i=0):
    name, band, price, facts, flag, flagkind = o
    flag_html = f'<p class="flag flag--{flagkind}">{flag}</p>' if flag else ""
    facts_html = "".join(f"<li>{f}</li>" for f in facts)
    return f"""        <article class="offer">
          <div>
            <h3><span class="offer__band band--{band}"></span>{name}</h3>
            <p class="offer__sub">Home supporters section</p>
            <ul class="offer__facts">{facts_html}</ul>
          </div>
          <div class="offer__buy">
            <p class="offer__price">₹{price:,}<span>per seat</span></p>
            <label class="visually-hidden" for="qty-{i}">Seats</label>
            <select id="qty-{i}" name="qty-{i}" class="qty">
              <option>1 seat</option><option>2 seats</option><option>3 seats</option><option>4 seats</option>
            </select>
            <a class="btn btn--primary" href="seats.html">Choose seats</a>
            {flag_html}
          </div>
        </article>
"""


ev = head("Mumbai City FC vs Bengaluru FC", "Durand Cup at Mumbai Football Arena. Seating plan, live prices and seat-level booking.")
ev += masthead("")
ev += f"""
<main id="main">

  <section class="eventhead">
    <div class="shell eventhead__grid">
      <div>
        <p class="eventhead__comp">Durand Cup · Fourth round</p>
        <h1>Mumbai City FC vs Bengaluru FC</h1>
        <dl>
          <div><dt>Kick-off</dt><dd>Saturday 4 October 2026, 19:45</dd></div>
          <div><dt>Ground</dt><dd>Mumbai Football Arena, Mumbai</dd></div>
          <div><dt>Capacity</dt><dd>62,400 · 1,180 seats left</dd></div>
        </dl>
        <p class="eventhead__price">from ₹6,200 <span>per seat, fees included</span></p>
      </div>
      <ul class="checks">
        <li>Seats confirmed by block, row and number</li>
        <li>Covered by the Full House Guarantee</li>
        <li>Groups seated together unless the listing says otherwise</li>
        <li>Tickets sent to your phone 48 hours before kick-off</li>
      </ul>
    </div>
  </section>

  <div class="shell">
    <ol class="steps">
      <li class="is-current"><b>1</b> Choose a block</li>
      <li><b>2</b> Pick your seats</li>
      <li><b>3</b> Pay</li>
      <li><b>4</b> Get your tickets</li>
    </ol>
  </div>

  <div class="shell">
    <form class="filters">
      <fieldset class="field">
        <legend>How many seats</legend>
        <div class="chips">
          <input type="radio" id="q-any" name="qty" checked><label for="q-any">Any</label>
          <input type="radio" id="q-1" name="qty"><label for="q-1">1</label>
          <input type="radio" id="q-2" name="qty"><label for="q-2">2</label>
          <input type="radio" id="q-3" name="qty"><label for="q-3">3</label>
          <input type="radio" id="q-4" name="qty"><label for="q-4">4+</label>
        </div>
      </fieldset>
      <div class="field">
        <label for="side">Supporter section</label>
        <select id="side"><option>All sections</option><option>Mumbai City FC home ends</option><option>Bengaluru FC away end</option><option>Neutral</option></select>
      </div>
      <div class="field">
        <label for="max">Most I want to pay</label>
        <select id="max"><option>No limit</option><option>₹9,500 a seat</option><option>₹15,800 a seat</option><option>₹24,100 a seat</option></select>
      </div>
      <div class="field">
        <span class="hint">Extras</span>
        <label class="switch"><input type="checkbox"><i></i> Seated together only</label>
        <label class="switch"><input type="checkbox"><i></i> Step-free access</label>
      </div>
    </form>
  </div>

  <section class="shell section" style="padding-top:0">
    <div class="listing">
      <div>
        <div class="section__head">
          <h2>28 listings</h2>
          <p>Sorted by price, lowest first</p>
        </div>
        <div class="offers">
{''.join(offer(o, i) for i, o in enumerate(OFFERS, 1))}        </div>
      </div>

      <div class="mappanel">
        <div class="mappanel__head">
          <h2>Mumbai Football Arena</h2>
          <p>Choose a block to open its seats</p>
        </div>
        {BOWL}
        <div class="legend">
          <span><i style="background:var(--band-box)"></i> Hospitality · ₹30,000</span>
          <span><i style="background:var(--band-gold)"></i> Halfway line · ₹19,100</span>
          <span><i style="background:var(--band-silver)"></i> Longside · ₹12,000</span>
          <span><i style="background:var(--band-bronze)"></i> Behind the goal · ₹6,200</span>
        </div>
      </div>
    </div>
  </section>

</main>
"""
ev += FOOTER
(ROOT / "event.html").write_text(ev)


# ---------------------------------------------------------------- seats.html
ROWS_FRONT = list("ABCDEF")
ROWS_MID = list("GHJKLMN")
ROWS_REAR = list("PQRSTU")
SEATS_PER_SIDE = 11


def taken(row_letter, n):
    """Deterministic, plausible-looking sold pattern."""
    h = (ord(row_letter) * 37 + n * 17) % 23
    return h in (0, 3, 11)


def seat_cell(row_letter, n, zone):
    sid = f"{row_letter}{n}"
    if taken(row_letter, n):
        return f'<span class="seat seat--taken"><span class="seat-no" aria-hidden="true">{n}</span><span class="visually-hidden">Seat {sid} is sold</span></span>'
    access = ' seat--access' if row_letter in ("N", "U") and n in (1, 22) else ''
    return (
        f'<span class="seat{access}">'
        f'<input type="checkbox" id="s{sid}" name="seat" value="{sid}">'
        f'<label for="s{sid}">{n}<span class="visually-hidden"> — row {row_letter}, seat {n}</span></label>'
        f'</span>'
    )


def build_zone(rows, zone, title, price, note):
    out = [f'<div class="zone zone--{zone}">',
           f'  <div class="zone__label"><b>{title}</b><span>₹{price:,} a seat · {note}</span></div>']
    for r in rows:
        cells = []
        for n in range(1, SEATS_PER_SIDE + 1):
            cells.append(seat_cell(r, n, zone))
        cells.append('<span class="aisle" aria-hidden="true"></span>')
        for n in range(SEATS_PER_SIDE + 1, SEATS_PER_SIDE * 2 + 1):
            cells.append(seat_cell(r, n, zone))
        out.append(f'  <div class="row"><span class="row__id">{r}</span>{"".join(cells)}</div>')
    out.append('</div>')
    return "\n".join(out)


anchors = "\n".join(
    f'<i class="anchor" id="b{code}"></i>'
    for code in ([str(101 + i) for i in range(24)]
                 + [f"M{i+1:02d}" for i in range(16)]
                 + [str(201 + i) for i in range(28)])
)

seats = head("Pick your seats", "Choose exact seats. Running totals are calculated without any JavaScript.",
             extra_css=("css/seatmap.css", "css/_blocks.css"))
seats += masthead("")
seats += f"""
{anchors}
<main id="main" class="seatwrap">

  <div class="blk-bar">
    <div class="shell blk-bar__grid">
      <div>
        <h1>Block <span class="blk-name"></span></h1>
        <p class="blk-band">Price band: <span class="blk-band-val"></span></p>
      </div>
      <p class="blk-meta">Mumbai City FC vs Bengaluru FC · Sat 4 Oct, 19:45</p>
      <a class="btn btn--ghost btn--sm blk-bar__back" href="event.html">Back to all blocks</a>
    </div>
  </div>

  <div class="shell">
    <ol class="steps">
      <li class="is-done"><b>1</b> Choose a block</li>
      <li class="is-current"><b>2</b> Pick your seats</li>
      <li><b>3</b> Pay</li>
      <li><b>4</b> Get your tickets</li>
    </ol>
  </div>

  <div class="shell">
    <div class="stand">
      <p class="pitchline">Pitch</p>

{build_zone(ROWS_FRONT, 'front', 'Rows A–F, pitchside', 19100, 'closest to the touchline')}

{build_zone(ROWS_MID, 'mid', 'Rows G–N, middle tier', 12000, 'best all-round view')}

{build_zone(ROWS_REAR, 'rear', 'Rows P–U, back of the block', 6200, 'under cover')}

      <div class="seatlegend">
        <span><i class="i-front"></i> Pitchside ₹19,100</span>
        <span><i class="i-mid"></i> Middle ₹12,000</span>
        <span><i class="i-rear"></i> Back ₹6,200</span>
        <span><i class="i-pick"></i> Your pick</span>
        <span><i class="i-gone"></i> Sold</span>
        <span>♿ Step-free</span>
      </div>
    </div>

    <div class="tally">
      <div class="tally__stat"><span>Seats</span><b class="tally__count"></b></div>
      <div class="tally__stat"><span>Seats subtotal</span><b class="tally__sub"></b></div>
      <div class="tally__stat"><span>Booking fee</span><b class="tally__fees"></b></div>
      <div class="tally__stat"><span>Total</span><b class="tally__total"></b></div>
      <p class="tally__empty">Tap any free seat to add it.</p>
      <a class="btn btn--primary tally__go" href="checkout.html">Continue to payment</a>
    </div>

    <p class="hint" style="margin-top:1rem">
      Counts and totals above are worked out with CSS counters, so they update the moment you select a seat —
      there is no script on this page. Booking fee is ₹150 a seat.
    </p>
  </div>

</main>
"""
seats += FOOTER
(ROOT / "seats.html").write_text(seats)


# ------------------------------------------------------------- checkout.html
co = head("Checkout", "Confirm your seats and pay.")
co += masthead("")
co += """
<main id="main" class="shell section">

  <ol class="steps">
    <li class="is-done"><b>1</b> Choose a block</li>
    <li class="is-done"><b>2</b> Pick your seats</li>
    <li class="is-current"><b>3</b> Pay</li>
    <li><b>4</b> Get your tickets</li>
  </ol>

  <div class="section__head">
    <h1>Checkout</h1>
    <p>Seats are held for 10 minutes.</p>
  </div>

  <form class="checkout" action="confirmation.html" method="get">
    <div>
      <div class="panel">
        <h2>Who are the tickets for?</h2>
        <div class="formgrid">
          <div class="field">
            <label for="fn">First name</label>
            <input id="fn" name="fn" type="text" required>
          </div>
          <div class="field">
            <label for="ln">Last name</label>
            <input id="ln" name="ln" type="text" required>
          </div>
          <div class="field span-2">
            <label for="em">Email</label>
            <input id="em" name="em" type="email" required>
            <p class="hint">Your tickets arrive here 48 hours before kick-off.</p>
          </div>
          <div class="field">
            <label for="ph">Mobile</label>
            <input id="ph" name="ph" type="tel">
          </div>
          <div class="field">
            <label for="cn">Country</label>
            <select id="cn" name="cn">
              <option selected>India</option>
              <option>United States</option>
              <option>United Kingdom</option>
              <option>Germany</option>
            </select>
          </div>
        </div>
      </div>

      <div class="panel">
        <h2>How should we send them?</h2>
        <div class="chips">
          <input type="radio" id="d-mob" name="delivery" checked><label for="d-mob">Mobile tickets</label>
          <input type="radio" id="d-print" name="delivery"><label for="d-print">Print at home</label>
          <input type="radio" id="d-box" name="delivery"><label for="d-box">Collect at the ground</label>
        </div>
        <p class="hint" style="margin-top:0.75rem">Mobile tickets are free. Collection opens three hours before kick-off at the West Terrace box office.</p>
      </div>

      <div class="panel">
        <h2>Payment</h2>
        <p class="hint">This is a demonstration build. The form does not send anything anywhere and no payment is taken.</p>
        <div class="formgrid">
          <div class="field span-2">
            <label for="card">Card number</label>
            <input id="card" name="card" type="text" inputmode="numeric" placeholder="0000 0000 0000 0000" autocomplete="off">
          </div>
          <div class="field">
            <label for="exp">Expires</label>
            <input id="exp" name="exp" type="text" placeholder="MM / YY" autocomplete="off">
          </div>
          <div class="field">
            <label for="cvc">Security code</label>
            <input id="cvc" name="cvc" type="text" autocomplete="off">
          </div>
        </div>
        <p></p>
        <label class="switch"><input type="checkbox" required><i></i> I accept the ticket terms and the ground regulations</label>
      </div>
    </div>

    <aside class="panel summary">
      <h2>Your order</h2>
      <p class="hint">Mumbai City FC vs Bengaluru FC<br>Durand Cup · Sat 4 Oct 2026, 19:45<br>Mumbai Football Arena, Mumbai</p>
      <dl>
        <div><dt>Block 108, row J, seat 12</dt><dd>₹12,000</dd></div>
        <div><dt>Block 108, row J, seat 13</dt><dd>₹12,000</dd></div>
        <div><dt>Booking fee, 2 seats</dt><dd>₹300</dd></div>
        <div class="total"><dt>Total</dt><dd>₹24,300</dd></div>
      </dl>
      <p></p>
      <button class="btn btn--primary btn--wide" type="submit">Pay ₹24,300</button>
      <p class="hint" style="margin-top:0.75rem">Covered by the Full House Guarantee.</p>
    </aside>
  </form>

</main>
"""
co += FOOTER
(ROOT / "checkout.html").write_text(co)


# --------------------------------------------------------- confirmation.html
cf = head("Order confirmed", "Your seats are booked.")
cf += masthead("")
cf += """
<main id="main" class="shell section">

  <ol class="steps">
    <li class="is-done"><b>1</b> Choose a block</li>
    <li class="is-done"><b>2</b> Pick your seats</li>
    <li class="is-done"><b>3</b> Pay</li>
    <li class="is-current"><b>4</b> Get your tickets</li>
  </ol>

  <div class="section__head">
    <h1>Your seats are booked</h1>
    <p>Order VST-4471-092</p>
  </div>

  <p>We have emailed a receipt. Your tickets land in the same inbox on <b>Thursday 2 October</b>, two days before kick-off.</p>

  <div class="stub">
    <div class="stub__main">
      <p class="fixture__comp">Durand Cup · Fourth round</p>
      <h2>Mumbai City FC vs Bengaluru FC</h2>
      <p class="offer__sub">Saturday 4 October 2026, 19:45 · Mumbai Football Arena, Mumbai</p>
      <table class="table">
        <tr><th>Block</th><td>108, Longside Lower</td></tr>
        <tr><th>Row</th><td>J</td></tr>
        <tr><th>Seats</th><td>12 and 13</td></tr>
        <tr><th>Entrance</th><td>Gate 4, West Terrace</td></tr>
        <tr><th>Paid</th><td>₹24,300</td></tr>
      </table>
    </div>
    <div class="stub__tear">
      <div class="code" role="img" aria-label="Entry code, scanned at the turnstile"></div>
      <p class="hint">Scan at Gate 4<br>VST-4471-092</p>
    </div>
  </div>

  <p></p>
  <p><a class="btn btn--dark" href="fixtures.html">Book another fixture</a> <a class="btn btn--ghost" href="track.html">Track this order</a></p>

</main>
"""
cf += FOOTER
(ROOT / "confirmation.html").write_text(cf)


# ---------------------------------------------------------------- track.html
tr = head("Find my order", "Look up an order, check delivery, or read the refund rules.")
tr += masthead("")
tr += """
<main id="main" class="shell section">

  <div class="section__head">
    <h1>Find my order</h1>
    <p>Answers to the three things people ask most.</p>
  </div>

  <div class="checkout">
    <div>
      <div class="panel">
        <h2>Look up an order</h2>
        <form class="formgrid" action="confirmation.html" method="get">
          <div class="field">
            <label for="ord">Order number</label>
            <input id="ord" name="ord" type="text" placeholder="VST-0000-000">
          </div>
          <div class="field">
            <label for="oem">Email on the order</label>
            <input id="oem" name="oem" type="email" placeholder="you@example.com">
          </div>
          <div class="field span-2">
            <button class="btn btn--primary" type="submit">Show my order</button>
          </div>
        </form>
      </div>

      <div class="panel" id="delivery">
        <h2>Ticket delivery</h2>
        <table class="table">
          <tr><th>Mobile tickets</th><td>Emailed 48 hours before kick-off. Free.</td></tr>
          <tr><th>Print at home</th><td>Emailed as a PDF 48 hours before kick-off. Free.</td></tr>
          <tr><th>Collect at the ground</th><td>West Terrace box office, from three hours before kick-off. Bring photo ID. ₹200.</td></tr>
        </table>
      </div>

      <div class="panel" id="refunds">
        <h2>Refunds and resales</h2>
        <p>If a fixture is cancelled outright, we refund the full amount including the booking fee, within five working days.</p>
        <p>If a fixture moves date or kick-off time, your seats move with it. Tell us within seven days if the new date does not work and we will refund you.</p>
        <p>Change of mind is not refundable, but you can list your seats for resale up to four hours before kick-off.</p>
      </div>
    </div>

    <aside class="panel summary">
      <h2>Still stuck?</h2>
      <p class="hint">Our box office answers from 09:00 to 20:00, seven days a week.</p>
      <table class="table">
        <tr><th>Phone</th><td>0800 555 0142</td></tr>
        <tr><th>Email</th><td>help@vistara.example</td></tr>
        <tr><th>Matchdays</th><td>Gate 4 help point</td></tr>
      </table>
    </aside>
  </div>

</main>
"""
tr += FOOTER
(ROOT / "track.html").write_text(tr)

print("pages written:", sorted(p.name for p in ROOT.glob("*.html")))
