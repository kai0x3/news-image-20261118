#!/usr/bin/env python3
"""Build the 18 Nov 2026 world-news front page (1024x1024 PNG) for the
make.fun news-image-20261118 bounty. Headlines verified against the
18 Nov 2026 daily briefs of Level Headlines, Just Security Early Edition,
Zark News, Open Chronicle and Horizon (checked 2026-11-19 ~00:30 UTC)."""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (247, 243, 234)      # newsprint cream
INK = (24, 24, 28)
NAVY = (18, 38, 66)
RED = (178, 34, 34)
GOLD = (198, 148, 44)
GREY = (90, 90, 92)
RULE = (180, 172, 158)
SKY = (206, 224, 234)

F = "/usr/share/fonts/truetype/dejavu/"
serif_b = lambda s: ImageFont.truetype(F + "DejaVuSerif-Bold.ttf", s)
serif = lambda s: ImageFont.truetype(F + "DejaVuSerif.ttf", s)
sans_b = lambda s: ImageFont.truetype(F + "DejaVuSans-Bold.ttf", s)
sans = lambda s: ImageFont.truetype(F + "DejaVuSans.ttf", s)

img = Image.new("RGB", (W, H), BG)
d = ImageDraw.Draw(img)

def text(x, y, s, font, fill=INK, anchor="la"):
    d.text((x, y), s, font=font, fill=fill, anchor=anchor)

def wrap(s, font, max_w):
    words, lines, cur = s.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=font) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

# ---- masthead ----
d.rectangle([0, 0, W, 118], fill=NAVY)
text(512, 14, "WEDNESDAY  •  18 NOVEMBER 2026", sans_b(30),
     fill=(232, 222, 190), anchor="ma")
text(512, 52, "THE WORLD IN ONE IMAGE", serif_b(52),
     fill=(255, 255, 255), anchor="ma")
d.rectangle([0, 118, W, 124], fill=GOLD)

# ---- lead story: Xi–Putin summit ----
lead_head = "XI AND PUTIN MEET IN SHENZHEN"
for i, ln in enumerate(wrap(lead_head, serif_b(44), 928)):
    text(48, 146 + i * 54, ln, serif_b(44), fill=RED)
standfirst = ("A day before the first-ever three-way summit with Donald Trump "
              "\u2014 as the US and Iran trade blows across the Gulf.")
for i, ln in enumerate(wrap(standfirst, serif(25), 928)):
    text(48, 214 + i * 32, ln, serif(25))

# ---- illustration: globe with the three leaders' flags ----
bx0, by0, bx1, by1 = 48, 292, 976, 462
d.rectangle([bx0, by0, bx1, by1], fill=SKY)
d.rectangle([bx0, by0, bx1, by0 + 4], fill=NAVY)
# globe
cx, cy, r = 512, 402, 56
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(150, 190, 215),
          outline=NAVY, width=3)
d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=NAVY, width=3)
d.ellipse([cx - r // 2, cy - r, cx + r // 2, cy + r], outline=NAVY, width=2)
d.line([cx - r, cy, cx + r, cy], fill=NAVY, width=2)
d.arc([cx - r, cy - r // 2, cx + r, cy + r // 2], 0, 360, fill=NAVY, width=2)
# land blobs (abstract)
d.ellipse([cx - 42, cy - 40, cx - 8, cy - 12], fill=(96, 150, 96))
d.ellipse([cx + 6, cy + 8, cx + 44, cy + 38], fill=(96, 150, 96))
d.ellipse([cx + 18, cy - 44, cx + 46, cy - 18], fill=(120, 165, 110))
# three flags on poles above the globe
def flag(x, y, w, h, kind):
    d.line([x, y - 46, x, y], fill=INK, width=3)
    if kind == "china":
        d.rectangle([x, y - 46, x + w, y - 46 + h], fill=(222, 41, 16))
        for sx, sy in [(x + 10, y - 38), (x + 22, y - 34), (x + 10, y - 26)]:
            d.ellipse([sx, sy, sx + 5, sy + 5], fill=(255, 222, 0))
    elif kind == "russia":
        d.rectangle([x, y - 46, x + w, y - 46 + h // 3], fill=(255, 255, 255))
        d.rectangle([x, y - 46 + h // 3, x + w, y - 46 + 2 * h // 3],
                    fill=(0, 60, 160))
        d.rectangle([x, y - 46 + 2 * h // 3, x + w, y - 46 + h],
                    fill=(210, 30, 30))
    else:  # usa
        for i in range(7):
            d.rectangle([x, y - 46 + i * h // 7, x + w,
                         y - 46 + (i + 1) * h // 7],
                        fill=(178, 34, 34) if i % 2 == 0 else (255, 255, 255))
        d.rectangle([x, y - 46, x + w // 2, y - 46 + 4 * h // 7],
                    fill=(18, 38, 66))
flag(330, 330, 64, 36, "china")
flag(480, 318, 64, 36, "russia")
flag(630, 330, 64, 36, "usa")
text(330, 324, "CHINA", sans_b(17), fill=INK)
text(478, 312, "RUSSIA", sans_b(17), fill=INK)
text(640, 324, "USA", sans_b(17), fill=INK)
text(48, 470, "Xi Jinping and Vladimir Putin meet in Shenzhen ahead of "
              "Thursday's summit with Donald Trump.",
     sans(20), fill=GREY)

# ---- rule ----
d.line([48, 508, 976, 508], fill=RULE, width=2)

# ---- four stories in a 2x2 grid ----
stories = [
    ("US\u2013IRAN STRIKES", RED,
     "US strikes an Iranian missile site on Qeshm Island; Iran fires back "
     "at US bases in Kuwait and Bahrain."),
    ("DEMOCRATS TAKE SENATE", NAVY,
     "Mary Peltola wins Alaska's Senate race, giving Democrats a "
     "56\u201344 majority in the chamber."),
    ("MEASLES STATUS LOST", NAVY,
     "The US loses measles-elimination status after 26 years, with "
     "5,400+ cases recorded in 2026."),
    ("NVIDIA BEATS FORECASTS", NAVY,
     "Nvidia tops expectations with third-quarter revenue of "
     "$115.8 billion."),
]
gx, gy = 48, 528
cw, ch = 452, 180
for i, (head, col, body) in enumerate(stories):
    x = gx + (i % 2) * (cw + 24)
    y = gy + (i // 2) * (ch + 14)
    d.rectangle([x, y, x + cw, y + ch], outline=RULE, width=2)
    d.rectangle([x, y, x + cw, y + 44], fill=col)
    text(x + 14, y + 8, head, sans_b(24), fill=(255, 255, 255))
    lines = wrap(body, sans(21), cw - 28)[:4]
    for j, ln in enumerate(lines):
        text(x + 14, y + 56 + j * 26, ln, sans(21))

# ---- footer ----
d.line([48, 918, 976, 918], fill=RULE, width=2)
text(512, 926, "Also: Voyager 1 reaches one light-day from Earth  \u2022  "
     "Ebola passes 11,000 cases in DR Congo",
     sans(18), fill=GREY, anchor="ma")
text(512, 950, "Siberia plane crash kills 19  \u2022  Trump announces "
     "Philippines trade deal",
     sans(18), fill=GREY, anchor="ma")
text(512, 974, "Houthi drones target Saudi pipeline  \u2022  Matan Kahana "
     "elected speaker of Israel's Knesset",
     sans(18), fill=GREY, anchor="ma")

img.save("/home/hatch/workspace/makefun/news-image-20261118/entry.png",
         "PNG", optimize=True)
print("saved")
