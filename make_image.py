#!/usr/bin/env python3
"""Draw the front page of THE WORLD TODAY for Wednesday 18 November 2026.

A single 1024x1024 newspaper front page: masthead, lead story on the
US-Iran clash in the Strait of Hormuz with a drawn illustration, six
secondary stories in a grid, and a footer ticker with four more items.
Everything is drawn with Pillow shapes and DejaVu text; no external
images are used.
"""

import math
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (247, 243, 234)
INK = (20, 20, 24)
NAVY = (18, 33, 61)
RED = (178, 34, 34)
TEAL = (14, 110, 110)
GREY = (90, 90, 92)
RULE = (60, 60, 64)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap; returns a list of lines that fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, color=INK, align="left"):
    lines = wrap(draw, text, fnt, max_w)
    for ln in lines:
        if align == "center":
            lx = x + (max_w - draw.textlength(ln, font=fnt)) // 2
        else:
            lx = x
        draw.text((lx, y), ln, font=fnt, fill=color)
        y += leading
    return y


def hline(draw, x0, x1, y, color=RULE, width=2):
    draw.line([(x0, y), (x1, y)], fill=color, width=width)


# ---------------------------------------------------------------- scene art

def draw_lead_scene(draw, x0, y0, x1, y1):
    """Strait of Hormuz at dusk: sky, sea, burning tankers, jets."""
    sky_top = (244, 196, 130)
    sky_bot = (214, 138, 96)
    sea_top = (52, 84, 110)
    sea_bot = (24, 48, 70)
    horizon = y0 + int((y1 - y0) * 0.52)
    # sky gradient
    for yy in range(y0, horizon):
        t = (yy - y0) / max(1, horizon - y0)
        c = tuple(int(sky_top[i] + (sky_bot[i] - sky_top[i]) * t) for i in range(3))
        draw.line([(x0, yy), (x1, yy)], fill=c)
    # low sun
    cx, cy, r = x0 + 130, horizon - 55, 42
    draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 214, 120))
    draw.ellipse([cx - r + 8, cy - r + 8, cx + r - 8, cy + r - 8],
                 fill=(255, 232, 160))
    # sea gradient
    for yy in range(horizon, y1):
        t = (yy - horizon) / max(1, y1 - horizon)
        c = tuple(int(sea_top[i] + (sea_bot[i] - sea_top[i]) * t) for i in range(3))
        draw.line([(x0, yy), (x1, yy)], fill=c)
    # sun reflection
    for i in range(6):
        yy = horizon + 12 + i * 9
        wdt = 90 - i * 9
        draw.line([(cx - wdt // 2, yy), (cx + wdt // 2, yy)],
                  fill=(255, 214, 120), width=3)
    # distant tanker silhouette (left)
    tx, ty = x0 + 300, horizon + 26
    draw.rectangle([tx, ty - 26, tx + 210, ty + 6], fill=(12, 22, 30))
    draw.rectangle([tx + 40, ty - 52, tx + 70, ty - 26], fill=(12, 22, 30))
    draw.rectangle([tx + 130, ty - 44, tx + 150, ty - 26], fill=(12, 22, 30))
    # burning tanker (right), flames + smoke
    bx, by = x0 + 640, horizon + 30
    draw.rectangle([bx, by - 24, bx + 230, by + 8], fill=(16, 26, 34))
    draw.rectangle([bx + 60, by - 48, bx + 88, by - 24], fill=(16, 26, 34))
    for fx, fh, col in [(bx + 30, 46, (255, 120, 20)),
                        (bx + 70, 60, (255, 170, 40)),
                        (bx + 120, 52, (255, 120, 20)),
                        (bx + 170, 40, (255, 170, 40))]:
        draw.polygon([(fx, by - 24), (fx + 14, by - 24 - fh),
                      (fx + 28, by - 24)], fill=col)
    for sx, sy, sr in [(bx + 55, by - 70, 18), (bx + 90, by - 95, 22),
                       (bx + 125, by - 104, 22), (bx + 100, by - 118, 18)]:
        draw.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(70, 70, 74))
    # smoke from distant tanker
    for sx, sy, sr in [(tx + 55, ty - 55, 13), (tx + 78, ty - 72, 16),
                       (tx + 100, ty - 88, 18)]:
        draw.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(96, 96, 100))
    # two jets in the sky
    for jx, jy, s in [(x0 + 560, y0 + 42, 1.0), (x0 + 700, y0 + 78, 0.8)]:
        pts = [(jx, jy), (jx + int(46 * s), jy + int(8 * s)),
               (jx + int(20 * s), jy + int(10 * s)),
               (jx + int(30 * s), jy + int(20 * s)),
               (jx + int(6 * s), jy + int(12 * s)),
               (jx - int(6 * s), jy + int(22 * s)),
               (jx - int(14 * s), jy + int(8 * s))]
        draw.polygon(pts, fill=(30, 30, 34))
        draw.line([(jx - int(10 * s), jy + int(6 * s)),
                   (jx - int(52 * s), jy - int(2 * s))],
                  fill=(255, 255, 255), width=2)
    # thin frame
    draw.rectangle([x0, y0, x1, y1], outline=INK, width=2)


# ------------------------------------------------------------- small icons

def icon_cyclone(d, x, y, s, col):
    for i, r in enumerate([8, 15, 22, 29]):
        d.arc([x + s // 2 - r, y + s // 2 - r, x + s // 2 + r, y + s // 2 + r],
              start=200 + i * 40, end=380 + i * 40, fill=col, width=4)
    d.ellipse([x + s // 2 - 4, y + s // 2 - 4, x + s // 2 + 4, y + s // 2 + 4],
              fill=col)


def icon_chip(d, x, y, s, col):
    m = 14
    d.rectangle([x + m, y + m, x + s - m, y + s - m], fill=col)
    d.rectangle([x + m + 8, y + m + 8, x + s - m - 8, y + s - m - 8],
                fill=(247, 243, 234))
    d.rectangle([x + m + 15, y + m + 15, x + s - m - 15, y + s - m - 15],
                fill=col)
    for i in range(4):
        px = x + m + 8 + i * 13
        d.line([(px, y + 4), (px, y + m)], fill=col, width=3)
        d.line([(px, y + s - m), (px, y + s - 4)], fill=col, width=3)
        py = y + m + 8 + i * 13
        d.line([(x + 4, py), (x + m, py)], fill=col, width=3)
        d.line([(x + s - m, py), (x + s - 4, py)], fill=col, width=3)


def icon_bridge(d, x, y, s, col):
    d.line([(x + 8, y + s - 20), (x + s - 8, y + s - 20)], fill=col, width=5)
    d.arc([x + 10, y + 14, x + s - 10, y + s - 6], start=180, end=360,
          fill=col, width=5)
    d.line([(x + s // 2, y + 16), (x + s // 2, y + s - 20)], fill=col, width=4)
    for fx in (x + 18, x + s - 26):
        d.line([(fx, y + s - 34), (fx, y + s - 20)], fill=col, width=4)
    # cracked deck
    d.line([(x + s // 2 - 4, y + s - 20), (x + s // 2 + 8, y + s - 12)],
           fill=RED, width=3)


def icon_globe_leaf(d, x, y, s, col):
    cx, cy, r = x + s // 2, y + s // 2, s // 2 - 8
    d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=col, width=4)
    d.ellipse([cx - r + 7, cy - r + 7, cx + r - 7, cy + r - 7],
              outline=col, width=2)
    d.line([(cx - r, cy), (cx + r, cy)], fill=col, width=2)
    d.line([(cx, cy - r), (cx, cy + r)], fill=col, width=2)
    # leaf
    d.pieslice([cx + 2, cy - r - 6, cx + 26, cy - 2], start=270, end=90,
               fill=(34, 139, 34))
    d.line([(cx + 2, cy - 2), (cx + 24, cy - 16)], fill=(34, 139, 34), width=2)


def icon_tent(d, x, y, s, col):
    d.polygon([(x + s // 2, y + 12), (x + 12, y + s - 14),
               (x + s - 12, y + s - 14)], outline=col, width=4)
    d.polygon([(x + s // 2 - 9, y + s - 14), (x + s // 2, y + s - 34),
               (x + s // 2 + 9, y + s - 14)], fill=col)
    for sx, sy in [(x + 16, y + 16), (x + s - 20, y + 20), (x + s - 16, y + 40)]:
        d.line([(sx - 6, sy), (sx + 6, sy)], fill=(120, 160, 200), width=3)
        d.line([(sx, sy - 6), (sx, sy + 6)], fill=(120, 160, 200), width=3)


def icon_plane(d, x, y, s, col):
    pts = [(x + 8, y + s // 2 + 6), (x + s - 10, y + s // 2 - 8),
           (x + s - 26, y + s // 2 - 2), (x + s - 18, y + s // 2 + 10),
           (x + s - 34, y + s // 2 + 12), (x + s - 40, y + s // 2 + 22),
           (x + s - 48, y + s // 2 + 12), (x + 22, y + s // 2 + 12)]
    d.polygon(pts, fill=col)
    for sx, sy, sr in [(x + 16, y + 14, 7), (x + 26, y + 24, 9),
                       (x + 38, y + 32, 6)]:
        d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(120, 120, 124))


# ------------------------------------------------------------------- page

def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 42  # margin

    # outer double border
    d.rectangle([10, 10, W - 11, H - 11], outline=INK, width=2)
    d.rectangle([16, 16, W - 17, H - 17], outline=INK, width=1)

    # ---- masthead
    y = 30
    title = "THE WORLD TODAY"
    tf = SERIF_B(74)
    d.text(((W - d.textlength(title, font=tf)) // 2, y), title, font=tf,
           fill=NAVY)
    y += 92
    hline(d, M, W - M, y, color=NAVY, width=4)
    y += 10
    date_txt = "WEDNESDAY, 18 NOVEMBER 2026"
    tag_txt = "ONE DAY'S NEWS  •  IN ONE PAGE"
    df = SANS_B(22)
    d.text((M, y), date_txt, font=df, fill=RED)
    d.text((W - M - d.textlength(tag_txt, font=df), y), tag_txt, font=df,
           fill=NAVY)
    y += 34
    hline(d, M, W - M, y, color=NAVY, width=2)

    # ---- lead headline
    y += 16
    lead1 = "U.S. JETS STRIKE IRAN AS"
    lead2 = "TANKERS BURN IN HORMUZ"
    lf = SERIF_B(52)
    for ln in (lead1, lead2):
        d.text(((W - d.textlength(ln, font=lf)) // 2, y), ln, font=lf, fill=INK)
        y += 60
    y += 4

    # ---- lead illustration
    scene_h = 200
    draw_lead_scene(d, M, y, W - M, y + scene_h)
    y += scene_h + 8
    cap = ("Washington says its jets hit a Revolutionary Guard missile site on "
           "Qeshm Island after Iranian drones targeted a U.S. radar base in "
           "Bahrain — and five Iranian oil tankers were sunk in the Gulf of "
           "Oman as the Gulf crisis deepened overnight.")
    y = para(d, M + 6, y, cap, SERIF(21), W - 2 * M - 12, 27, color=INK)
    y += 6
    hline(d, M, W - M, y, color=RULE, width=2)
    y += 12

    # ---- secondary stories, 2 columns x 3 rows
    stories = [
        ("CYCLONE AKVAN BEARS DOWN ON INDIA",
         "The storm over the Bay of Bengal is set to become a severe cyclone "
         "today, with landfall on the Andhra Pradesh coast on Friday.",
         icon_cyclone, TEAL),
        ("NVIDIA DOUBLES ITS REVENUE",
         "The chipmaker reported $115.8 billion in quarterly revenue, up "
         "103% on a year ago, with net profit of $65.3 billion as demand "
         "for AI data-centre chips keeps soaring.",
         icon_chip, (34, 139, 34)),
        ("UKRAINE HITS CRIMEA BRIDGE AGAIN",
         "Kyiv struck the bridge to occupied Crimea for a second night, "
         "collapsing a road section, as Russia hit bridges of its own "
         "ahead of Thursday's summit.",
         icon_bridge, (120, 40, 40)),
        ("COP31 ENTERS DECISIVE PHASE",
         "Climate negotiators in Antalya are working through a first draft "
         "deal with 144 disputed items, calling for a shift from fossil "
         "fuels and at least $120 billion for adaptation.",
         icon_globe_leaf, (34, 120, 34)),
        ("GAZA FACES A COLD WINTER",
         "The UN warns of more deaths from exposure as winter sets in: "
         "over 1.7 million people remain displaced and about 1.4 million "
         "face acute hunger.",
         icon_tent, (40, 90, 140)),
        ("RUSSIAN PLANE CRASH KILLS 19",
         "A military transport aircraft crashed in the Kemerovo region of "
         "Siberia, killing all 19 people on board, the Russian defence "
         "ministry said.",
         icon_plane, (60, 60, 66)),
    ]
    col_w = (W - 2 * M - 24) // 2
    row_h = 104
    for i, (head, body, icon, col) in enumerate(stories):
        cx = M + (i % 2) * (col_w + 24)
        cy = y + (i // 2) * row_h
        # icon tile
        d.rectangle([cx, cy, cx + 64, cy + 64], outline=col, width=2)
        icon(d, cx, cy, 64, col)
        tx = cx + 76
        tw = col_w - 76
        yy = para(d, tx, cy, head, SANS_B(19), tw, 23, color=INK)
        para(d, tx, yy + 1, body, SANS(15), tw, 19, color=(52, 52, 56))
    y += 3 * row_h + 6

    # ---- footer ticker (two lines inside a navy band)
    hline(d, M, W - M, y, color=RULE, width=2)
    y += 8
    band_h = 54
    d.rectangle([M, y, W - M, y + band_h], fill=NAVY)
    tick1 = ("ALSO TODAY:  Pattinson named the new James Bond  •  "
             "North Korea missile launch")
    tick2 = ("India and Japan hold 2+2 talks in Tokyo  •  Gas tanker sinks "
             "off Bulgaria — all 19 crew rescued")
    tf2 = SANS_B(15)
    for i, tl in enumerate((tick1, tick2)):
        tw = d.textlength(tl, font=tf2)
        d.text((M + (W - 2 * M - tw) // 2, y + 8 + i * 22), tl, font=tf2,
               fill=(247, 243, 234))

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out, "PNG", optimize=True)
    print("saved", out, os.path.getsize(out), "bytes")


if __name__ == "__main__":
    main()
