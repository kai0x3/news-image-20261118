#!/usr/bin/env python3
"""Build the 18 Nov 2026 world-news front page (1024x1024 PNG) for the
make.fun news-image-20261118 bounty — v2, dense wire style.

Modelled on what won the sibling 17 Nov edition (1st: "50 sourced
stories, a UTC timeline and a date check"; 2nd: "50 Verified Stories,
UTC Wire & Date Audit"): this page packs 50+ real, sourced stories from
Wednesday 18 November 2026 onto one broadsheet front page — a lead, a
UTC timeline strip, three secondary stories and a dense numbered wire
of short items, every item attributed to its source inline, under an
explicit date line with a date-checked banner.

Stories were verified against the 18 Nov 2026 daily briefs of Level
Headlines, Zark News and Open Chronicle, which in turn cite Reuters,
AP, AFP, BBC, CNBC, TechCrunch, Euronews, Yonhap, ABC News and others
(full source list in README.md; checked 2026-11-19 ~16:40 UTC).
"""
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
BG = (247, 243, 234)      # newsprint cream
INK = (24, 24, 28)
NAVY = (18, 38, 66)
RED = (178, 34, 34)
DARKRED = (120, 22, 22)
GOLD = (198, 148, 44)
GREY = (90, 90, 92)
RULE = (180, 172, 158)
SKY = (206, 224, 234)

F = "/usr/share/fonts/truetype/dejavu/"
serif_b = lambda s: ImageFont.truetype(F + "DejaVuSerif-Bold.ttf", s)
serif = lambda s: ImageFont.truetype(F + "DejaVuSerif.ttf", s)
sans_b = lambda s: ImageFont.truetype(F + "DejaVuSans-Bold.ttf", s)
sans = lambda s: ImageFont.truetype(F + "DejaVuSans.ttf", s)

# ---------------------------------------------------------------- stories
LEAD_HEAD = "XI AND PUTIN MEET IN SHENZHEN"
LEAD_BODY = ("Chinese and Russian leaders open talks in Shenzhen a day before "
             "their first-ever three-way summit with Donald Trump. Xi pledges "
             "to fight protectionism, Putin attacks Western sanctions, and "
             "Europe fears Ukraine's future being settled without Kyiv. "
             "(Reuters / AFP)")

# (when, text, source) — the day in UTC, as reported by the day's briefs
TIMELINE = [
    ("OVERNIGHT", "US jets strike IRGC site on Qeshm Island", "Reuters"),
    ("OVERNIGHT", "Iran hits US bases in Kuwait & Bahrain", "BBC"),
    ("MORNING", "Xi & Putin open talks in Shenzhen", "AFP"),
    ("10:16 UTC", "Voyager 1 crosses one light-day", "NASA JPL"),
    ("MIDDAY", "Trump hails Philippines deal in Manila", "Reuters"),
    ("EVENING", "AP calls Alaska for Peltola; 56-44", "AP"),
]

# (headline, body) — three secondary stories under the lead
SECONDARY = [
    ("US-IRAN STRIKES",
     "US strikes an Iranian missile site on Qeshm Island; Iran fires back "
     "at US bases in Kuwait (Ali Al Salem) and Bahrain. Kuwait repels the "
     "attack; Bahrain intercepts for a third time in a week. (Reuters)"),
    ("DEMOCRATS TAKE SENATE",
     "Mary Peltola beats Sen. Dan Sullivan in Alaska — the first Alaska "
     "Native elected to the US Senate — giving Democrats a 56-44 majority "
     "after nine flips. (AP)"),
    ("MEASLES STATUS LOST",
     "The US loses measles-elimination status after 26 years: 5,412 cases "
     "in 2026 and 10 deaths as one chain spreads for over a year. Mexico "
     "loses its status too. (PAHO / CDC)"),
]

# (headline, body) — the numbered wire; body ends with its source in parens
WIRE = [
    ("HORMUZ TANKER ATTACKED",
     "ADNOC-linked vessel hit in the Strait of Hormuz: one crew member "
     "missing, 11 injured, the rest evacuated. (Reuters)"),
    ("SAUDIS DOWN HOUTHI MISSILE",
     "Saudi air defences intercept a Houthi cruise missile launched "
     "toward the Riyadh region. (Open Chronicle)"),
    ("UKRAINE: KERCH BRIDGE HIT",
     "Kyiv claims a strike badly damaged the Crimean Bridge, Russia's "
     "key supply link to occupied Crimea. (Open Chronicle)"),
    ("KYIV SEEKS JETS AT RAMSTEIN",
     "Ukraine presses allies for fighters and air defence; France may "
     "add Mirage 2000-5F jets. (Open Chronicle)"),
    ("DRONES HIT RUSSIAN REFINERIES",
     "Ukrainian drones strike oil refineries in southern Russia in "
     "Kyiv's campaign on energy sites. (Open Chronicle)"),
    ("RUSSIAN DRONES OVER KYIV",
     "Ukraine reports a renewed Russian drone attack on the capital on "
     "Wednesday morning. (Open Chronicle)"),
    ("EU LOAN FOR UKRAINE",
     "Brussels proposes a 45bn-euro loan to Kyiv, repayable only once "
     "Russia pays war reparations. (Reuters)"),
    ("CANADA BACKS KYIV",
     "Ottawa keeps sanctions pressure on Moscow and adds air-defence "
     "kit, ammunition and winter supplies. (Open Chronicle)"),
    ("SLOVAKS PROTEST FICO",
     "Thousands march against PM Robert Fico's government and its "
     "stance toward Russia. (Open Chronicle)"),
    ("ITALY ANTISEMITISM LAW",
     "Rome approves antisemitism legislation; critics warn of risks to "
     "free expression. (Open Chronicle)"),
    ("EU ACTS AGAINST TEMU",
     "Brussels takes enforcement action over illegal products sold on "
     "the online marketplace. (Open Chronicle)"),
    ("NATO COMMS STRATEGY",
     "NATO unveils an alliance-wide plan for next-generation military "
     "communications networks. (Open Chronicle)"),
    ("XI CHAMPIONS OPEN TRADE",
     "At APEC, Xi calls for lower trade barriers and market access as "
     "Putin slams sanctions on Russia. (AP)"),
    ("SEOUL COURTS BEIJING",
     "President Lee Jae Myung ties closer China ties to peace and "
     "stability on the Korean Peninsula. (Yonhap)"),
    ("BOMBERS NEAR JAPAN, TAIWAN",
     "Unusual Russian bomber flights reported near Japan and Taiwan; "
     "airspace violations unconfirmed. (Open Chronicle)"),
    ("SOUTH CHINA SEA TALKS",
     "ASEAN states keep negotiating a code of conduct for the disputed "
     "South China Sea. (Open Chronicle)"),
    ("ARSENIC FEARS ON THAI BORDER",
     "Villages near the Myanmar border seek safe water amid arsenic "
     "contamination concerns. (Open Chronicle)"),
    ("KNESSET ELECTS KAHANA",
     "Israel's parliament picks Netanyahu critic Matan Kahana as "
     "speaker, by 66 votes to 52. (Reuters)"),
    ("AUSTRALIA SANCTIONS SETTLERS",
     "Canberra sanctions three people and four groups over West Bank "
     "settlement expansion. (ABC News)"),
    ("GAZA AID WARNING",
     "WHO urges unobstructed humanitarian aid as the Gaza ceasefire "
     "strains ahead of winter. (Open Chronicle)"),
    ("TURKIYE WARNS ISRAEL",
     "Ankara urges Israel to end policies it says are damaging ties "
     "with neighbouring countries. (Open Chronicle)"),
    ("IRAQ MILITIA STANDOFF",
     "Baghdad orders Kata'ib Hezbollah out of Jurf al-Sakhar; the "
     "armed group refuses to withdraw. (Open Chronicle)"),
    ("LEBANON-SYRIA THAW",
     "President Aoun says Lebanon's relations with Syria are "
     "developing positively. (Open Chronicle)"),
    ("LIBYA DRUG SEIZURES",
     "Eastern Libya announces major cocaine and pill seizures in "
     "anti-trafficking operations. (Open Chronicle)"),
    ("TUNISIA MIGRANT RETURNS",
     "Tunisia reports a rise in voluntary returns among irregular "
     "migrants. (Open Chronicle)"),
    ("ICJ: MYANMAR GENOCIDE",
     "The World Court rules Myanmar committed genocide against the "
     "Rohingya during the 2017 crackdown. (Daily News Wrap)"),
    ("CYCLONE AKVAN EVACUATIONS",
     "Cyclone Akvan triggers large-scale evacuations along India's "
     "Odisha coast. (Daily News Wrap)"),
    ("BANGLADESH FORCES DEPLOY",
     "Paramilitary forces deploy as Bangladesh prepares for the "
     "ousted prime minister's return. (Breitbart)"),
    ("MULLIN FACES HOUSE HEARING",
     "Homeland Security chief Markwayne Mullin testifies after the "
     "flight grounding and outage chaos. (AP)"),
    ("RUBIO: NO CYBERATTACK LINK",
     "Rubio sees 'zero' evidence tying US outages to a malign actor; "
     "an NSA network went down. (AP)"),
    ("27 YEARS IN TRUMP PLOT",
     "A Pakistani national is sentenced to 27+ years in an Iran-linked "
     "plot to assassinate Trump. (Open Chronicle)"),
    ("WAYMO LEAVES THE FREEWAYS",
     "Waymo suspends driverless freeway rides across the US after "
     "California's DMV ban. (TechCrunch)"),
    ("WASHINGTON TAX SWAP PLAN",
     "Senate leader Pedersen floats a corporate income tax to replace "
     "the state's B&O tax. (Seattle Times)"),
    ("SEWAGE CLOSES PORT LUDLOW",
     "A 50,000-gallon sewage spill closes Port Ludlow Bay on the "
     "Olympic Peninsula indefinitely. (Seattle Times)"),
    ("EBOLA PASSES 11,000 CASES",
     "Congo's outbreak doubles in three months: 11,000+ cases across "
     "67 health zones in eight provinces. (Zark News)"),
    ("EBOLA VACCINE TRIALS",
     "Two Ebola vaccine candidates are set to enter Phase 2 clinical "
     "trials in DR Congo. (Open Chronicle)"),
    ("SIBERIA CRASH KILLS 19",
     "A Russian military plane crashes in Siberia, killing 19 people. "
     "(Horizon)"),
    ("SUDAN ARMY GAINS",
     "Sudanese army forces advance in West Kordofan as the RSF faces "
     "pressure in the region. (Open Chronicle)"),
    ("NIGERIA STATE POLICE LAW",
     "Nigeria approves letting states set up their own police forces "
     "in a major security overhaul. (Open Chronicle)"),
    ("GHANA PRESIDENTIAL JET ROW",
     "A new presidential aircraft stirs controversy over government "
     "spending in Ghana. (Open Chronicle)"),
    ("HAITI-EL SALVADOR PACT",
     "Haiti formalises a security agreement with El Salvador to help "
     "confront armed gangs. (Euronews)"),
    ("AMAZON CONTACT ALARM",
     "Contact with an isolated Indigenous people in Brazil's Amazon "
     "raises disease and protection fears. (Open Chronicle)"),
    ("CARNEY COURTS ASIA TRADE",
     "Canada's PM Mark Carney seeks Asian trade deals to cut reliance "
     "on the United States. (Open Chronicle)"),
    ("AUSTRALIA PAY GAP RECORD",
     "Australia's gender pay gap falls to its lowest level on record. "
     "(Open Chronicle)"),
    ("NZ TSUNAMI ALERT LIFTED",
     "New Zealand withdraws a tsunami warning after offshore activity "
     "near the North Island. (Open Chronicle)"),
    ("JAVA FLAW WARNING",
     "The US and South Korea issue urgent advisories over "
     "vulnerabilities in Java software. (Open Chronicle)"),
    ("EUROPE WILDFIRE SEASON",
     "An exceptional wildfire season and rising drug-resistant "
     "infections strain Europe. (Open Chronicle)"),
    ("COLORADO TAX RANKING FALLS",
     "Amendment 87 would drop Colorado to No. 44 in tax "
     "competitiveness, a Tax Foundation analysis finds. (Axios Denver)"),
    ("DENVER N LINE EXTENSION",
     "RTD begins planning a 5.5-mile N Line commuter rail extension "
     "in Adams County. (Denverite)"),
    ("BRONCOS HOST RAIDERS",
     "Denver returns from its bye week to host Las Vegas on Sunday, "
     "coach Sean Payton says. (9News)"),
]

# (the on-page story count is computed after layout, as STORY_COUNT)

# ---------------------------------------------------------------- drawing
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

MX = 32                      # side margin
CW = W - 2 * MX              # content width = 960

# ---- wire layout: decide which items fit the four columns up front,
# so the banner can print the true on-page story count ----
WY = 446
WBOT = 976
GAP = 16
COLW = (CW - 3 * GAP) // 4
HF, BF = sans_b(10), sans(9)
def _item_h(head, body):
    hl = len(wrap(head, HF, COLW - 19))
    bl = len(wrap(body, BF, COLW - 19))
    return hl * 11 + bl * 10 + 5

COLS = [[] for _ in range(4)]
_heights = [0] * 4
for _n, (_head, _body) in enumerate(WIRE, start=1):
    _h = _item_h(_head, _body)
    _c = min(range(4), key=lambda k: _heights[k])
    if _heights[_c] + _h > WBOT - WY and all(
            _heights[k] + _h > WBOT - WY for k in range(4)):
        break
    COLS[_c].append((_n, _head, _body))
    _heights[_c] += _h
RENDERED = sum(len(c) for c in COLS)
STORY_COUNT = 1 + len(SECONDARY) + RENDERED

# ---- masthead ----
d.rectangle([0, 0, W, 92], fill=NAVY)
text(512, 8, "WEDNESDAY  \u2022  18 NOVEMBER 2026  \u2022  THE DAILY WORLD EDITION",
     sans_b(17), fill=(232, 222, 190), anchor="ma")
text(512, 32, "THE WORLD IN ONE IMAGE", serif_b(44),
     fill=(255, 255, 255), anchor="ma")
d.rectangle([0, 92, W, 96], fill=GOLD)

# ---- date-check banner ----
d.rectangle([0, 96, W, 124], fill=DARKRED)
text(512, 103, "\u2713 DATE CHECKED \u2014 ALL STORIES FROM WEDNESDAY 18 NOVEMBER 2026 "
               f"\u2022 {STORY_COUNT} SOURCED STORIES \u2022 SOURCES NAMED INLINE",
     sans_b(13), fill=(255, 255, 255), anchor="ma")

# ---- lead story ----
ly = 138
text(MX, ly, LEAD_HEAD, serif_b(40), fill=RED)
# compact flags at the right of the lead block
def flag(x, y, w, h, kind):
    d.line([x, y, x, y + 46], fill=INK, width=3)
    if kind == "china":
        d.rectangle([x, y, x + w, y + h], fill=(222, 41, 16))
        for sx, sy in [(x + 8, y + 6), (x + 18, y + 10), (x + 8, y + 16)]:
            d.ellipse([sx, sy, sx + 4, sy + 4], fill=(255, 222, 0))
    elif kind == "russia":
        d.rectangle([x, y, x + w, y + h // 3], fill=(255, 255, 255))
        d.rectangle([x, y + h // 3, x + w, y + 2 * h // 3], fill=(0, 60, 160))
        d.rectangle([x, y + 2 * h // 3, x + w, y + h], fill=(210, 30, 30))
    else:
        for i in range(7):
            d.rectangle([x, y + i * h // 7, x + w, y + (i + 1) * h // 7],
                        fill=(178, 34, 34) if i % 2 == 0 else (255, 255, 255))
        d.rectangle([x, y, x + w // 2, y + 4 * h // 7], fill=NAVY)
fx, fy = 856, 200
d.rectangle([fx - 10, fy - 8, W - MX, fy + 64], fill=SKY, outline=NAVY, width=2)
flag(fx, fy, 34, 20, "china")
flag(fx + 44, fy, 34, 20, "russia")
flag(fx + 88, fy, 34, 20, "usa")
text(fx + 61, fy + 50, "SHENZHEN \u2022 APEC", sans_b(10), fill=NAVY, anchor="ma")
for i, ln in enumerate(wrap(LEAD_BODY, serif(16), 800)):
    text(MX, ly + 52 + i * 21, ln, serif(16))
d.line([MX, 266, W - MX, 266], fill=RULE, width=2)

# ---- UTC timeline strip ----
ty = 272
d.rectangle([MX, ty, W - MX, ty + 64], fill=NAVY)
text(MX + 12, ty + 5, "THE DAY IN UTC \u2014 WEDNESDAY 18 NOVEMBER 2026",
     sans_b(13), fill=GOLD)
col_w = (CW - 24) // 3
for i, (when, txt, src) in enumerate(TIMELINE):
    cx = MX + 12 + (i % 3) * col_w
    cy = ty + 25 + (i // 3) * 19
    text(cx, cy, when + "  ", sans_b(9), fill=(255, 255, 255))
    off = d.textlength(when + "  ", font=sans_b(9))
    text(cx + off, cy, txt + f" ({src})", sans(9), fill=(214, 222, 235))

# ---- secondary stories: three boxes ----
sy = 344
box_w = (CW - 2 * 14) // 3
for i, (head, body) in enumerate(SECONDARY):
    x = MX + i * (box_w + 14)
    d.rectangle([x, sy, x + box_w, sy + 96], outline=RULE, width=2)
    d.rectangle([x, sy, x + box_w, sy + 26], fill=NAVY if i != 0 else RED)
    text(x + 10, sy + 5, head, sans_b(14), fill=(255, 255, 255))
    for j, ln in enumerate(wrap(body, sans(11), box_w - 20)[:4]):
        text(x + 10, sy + 32 + j * 15, ln, sans(11))

# ---- the wire: draw the precomputed columns ----
for c in range(4):
    x = MX + c * (COLW + GAP)
    if c:
        d.line([x - GAP // 2, WY, x - GAP // 2, WBOT], fill=RULE, width=1)
    y = WY
    for n, head, body in COLS[c]:
        text(x, y, f"{n}.", sans_b(10), fill=RED)
        for j, ln in enumerate(wrap(head, HF, COLW - 19)):
            text(x + 19, y + j * 11, ln, HF)
        y += len(wrap(head, HF, COLW - 19)) * 11
        for ln in wrap(body, BF, COLW - 19):
            text(x + 19, y, ln, BF, fill=(52, 52, 56))
            y += 10
        y += 4

# ---- footer ----
d.line([MX, 980, W - MX, 980], fill=RULE, width=2)
text(512, 986, "Sources: Level Headlines \u2022 Zark News \u2022 Open Chronicle \u2022 Horizon \u2022 "
               "Reuters \u2022 AP \u2022 AFP \u2022 BBC \u2022 CNBC \u2022 TechCrunch \u2022 Euronews \u2022 Yonhap \u2022 "
               "ABC News \u2022 Seattle Times \u2022 Axios \u2022 NASA JPL \u2014 full citations in README.md",
     sans(9), fill=GREY, anchor="ma")
text(512, 1002, f"One day, one page: {STORY_COUNT} stories from 18 November 2026, "
                "each checked against the day's briefs. Drawn with PIL \u2014 see build_image.py.",
     sans(9), fill=GREY, anchor="ma")

img.save("/home/hatch/workspace/makefun/news-image-20261118/entry.png",
         "PNG", optimize=True)
print(f"saved; wire items rendered: {RENDERED} of {len(WIRE)}; "
      f"total stories on page: {STORY_COUNT}")
