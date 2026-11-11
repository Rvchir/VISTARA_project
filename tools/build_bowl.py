import math, json, pathlib

CX, CY = 600.0, 420.0

def pt(a, rx, ry):
    return (CX + rx * math.cos(a), CY + ry * math.sin(a))

def seg(a0, a1, rx_in, ry_in, rx_out, ry_out, steps=14):
    """Annulus segment between two ellipses, as a polygon path with smooth sampling."""
    pts = []
    for i in range(steps + 1):
        a = a0 + (a1 - a0) * i / steps
        pts.append(pt(a, rx_out, ry_out))
    for i in range(steps + 1):
        a = a1 + (a0 - a1) * i / steps
        pts.append(pt(a, rx_in, ry_in))
    d = "M " + " L ".join(f"{x:.1f} {y:.1f}" for x, y in pts) + " Z"
    return d

def label_pos(a0, a1, rx_in, ry_in, rx_out, ry_out):
    a = (a0 + a1) / 2
    return pt(a, (rx_in + rx_out) / 2, (ry_in + ry_out) / 2), math.degrees(a)

rings = []

# ---- Lower tier: 1xx, 24 blocks -------------------------------------------
n = 24
gap = math.radians(1.6)
blocks = []
start = math.radians(-90)  # start at top (north = East Stand in our plan)
for i in range(n):
    a0 = start + 2 * math.pi * i / n + gap / 2
    a1 = start + 2 * math.pi * (i + 1) / n - gap / 2
    num = 101 + i
    tier = "gold" if i in (0, 1, 11, 12, 13, 23) else ("silver" if i in (2, 3, 10, 14, 21, 22) else "bronze")
    blocks.append((f"{num}", a0, a1, tier))
rings.append(dict(name="lower", rx_in=300, ry_in=196, rx_out=386, ry_out=258, blocks=blocks, fs=17))

# ---- Boxes: M01..M16 ------------------------------------------------------
n = 16
gap = math.radians(2.2)
blocks = []
for i in range(n):
    a0 = start + 2 * math.pi * i / n + gap / 2
    a1 = start + 2 * math.pi * (i + 1) / n - gap / 2
    blocks.append((f"M{i+1:02d}", a0, a1, "box"))
rings.append(dict(name="boxes", rx_in=394, ry_in=266, rx_out=436, ry_out=300, blocks=blocks, fs=12))

# ---- Upper tier: 2xx, 28 blocks -------------------------------------------
n = 28
gap = math.radians(1.3)
blocks = []
for i in range(n):
    a0 = start + 2 * math.pi * i / n + gap / 2
    a1 = start + 2 * math.pi * (i + 1) / n - gap / 2
    num = 201 + i
    tier = "silver" if i in (0, 1, 13, 14, 15, 27) else "bronze"
    blocks.append((f"{num}", a0, a1, tier))
rings.append(dict(name="upper", rx_in=444, ry_in=308, rx_out=548, ry_out=384, blocks=blocks, fs=16))

PRICES = {"gold": 19100, "silver": 12000, "bronze": 6200, "box": 30000}

out = []
out.append('<svg class="bowl" viewBox="0 0 1200 840" role="img" xmlns="http://www.w3.org/2000/svg" aria-labelledby="bowl-title">')
out.append('<title id="bowl-title">Seating plan. Blocks are grouped into four price bands.</title>')

# pitch
out.append('<g class="bowl-pitch">')
out.append('<rect x="432" y="300" width="336" height="240" rx="4"/>')
out.append('<line x1="600" y1="300" x2="600" y2="540"/>')
out.append('<circle cx="600" cy="420" r="34" fill="none"/>')
out.append('<rect x="432" y="360" width="46" height="120" fill="none"/>')
out.append('<rect x="722" y="360" width="46" height="120" fill="none"/>')
out.append('</g>')

css_rules = []
for ring in rings:
    out.append(f'<g class="ring ring--{ring["name"]}">')
    for code, a0, a1, tier in ring["blocks"]:
        d = seg(a0, a1, ring["rx_in"], ring["ry_in"], ring["rx_out"], ring["ry_out"])
        (lx, ly), deg = label_pos(a0, a1, ring["rx_in"], ring["ry_in"], ring["rx_out"], ring["ry_out"])
        rot = deg + 90
        while rot > 90:
            rot -= 180
        while rot <= -90:
            rot += 180
        price = PRICES[tier]
        out.append(
            f'<a class="blk blk--{tier}" href="seats.html#b{code}" '
            f'aria-label="Block {code}, from ₹{price:,}">'
            f'<path d="{d}"/>'
            f'<text x="{lx:.1f}" y="{ly:.1f}" font-size="{ring["fs"]}" '
            f'transform="rotate({rot:.1f} {lx:.1f} {ly:.1f})">{code}</text>'
            f'</a>'
        )
        css_rules.append((code, tier, price))
    out.append('</g>')

# stand names
out.append('<g class="bowl-stand">')
out.append('<text x="600" y="34" text-anchor="middle">North Bank</text>')
out.append('<text x="600" y="818" text-anchor="middle">Kop End</text>')
out.append('<text x="30" y="420" text-anchor="middle" transform="rotate(-90 30 420)">West Terrace</text>')
out.append('<text x="1170" y="420" text-anchor="middle" transform="rotate(90 1170 420)">East Terrace</text>')
out.append('</g>')
out.append('</svg>')

pathlib.Path("../assets/bowl.svg.html").write_text("\n".join(out))

# -------- per-block CSS so :target swaps the block name + price on seats.html
lines = []
for code, tier, price in css_rules:
    lines.append(
        f'#b{code}:target ~ .seatwrap .blk-name::after{{content:"{code}"}}\n'
        f'#b{code}:target ~ .seatwrap .blk-band-val::after{{content:"{tier.title()}"}}\n'
        f'#b{code}:target ~ .seatwrap{{--seat-price:{price}}}'
    )
pathlib.Path("../css/_blocks.css").write_text(
    "/* Generated: each block anchor on the bowl retargets the seat grid header. */\n"
    + "\n".join(lines) + "\n"
)
print("blocks:", len(css_rules))
