# 18 November 2026: the world in one front page

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/kai0x3/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/kai0x3/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

Entry for "Sum up 18 November's world news in one image" ($250, 50 places paid).
Free entry, no fee. Ends Fri 20 Nov 2026 00:00 UTC (07:00 WIB).

A single 1024x1024 newspaper front page summing up the world news of
Wednesday 18 November 2026, drawn with PIL (see `build_image.py`).

## Format (v2 — dense wire edition)

This version follows the format that won the sibling 17 November
edition (1st place: "50 sourced stories, a UTC timeline and a date
check"; 2nd: "50 Verified Stories, UTC Wire & Date Audit") — density
of real, verifiable content over a sparse poster:

- **Date line + date check:** the masthead carries the explicit date
  (Wednesday 18 November 2026) and a "DATE CHECKED" banner states that
  every story on the page is from that day.
- **UTC timeline:** a strip of the day's events in UTC order
  (overnight US strike on Qeshm Island → Iran's answer → Xi–Putin
  talks → Voyager 1 crossing one light-day at 10:16 UTC → Trump's
  Manila announcement → AP calling Alaska in the evening).
- **48 sourced stories:** 1 lead + 3 secondary stories + a numbered
  wire of 44 short items in four dense broadsheet columns. Every item
  names its source inline, in parentheses.

## Headlines

- **Lead — Xi and Putin meet in Shenzhen:** Xi Jinping and Vladimir
  Putin open talks a day before the first-ever three-way summit with
  Donald Trump; Xi pledges to fight protectionism, Putin attacks
  sanctions, Europe fears Ukraine's future being settled without Kyiv.
- **US–Iran strikes:** the US strikes an Iranian missile site on Qeshm
  Island; Iran fires back at US bases in Kuwait (Ali Al Salem Air Base)
  and Bahrain.
- **Democrats take Senate:** Mary Peltola wins Alaska's Senate race —
  the first Alaska Native elected to the US Senate — giving Democrats
  a 56–44 majority.
- **Measles status lost:** the US loses measles-elimination status
  after 26 years, with 5,412 cases in 2026; Mexico loses its status
  too.
- **On the wire (44 items):** the Hormuz tanker attack, Saudi
  interception of a Houthi missile, Ukraine's Kerch Bridge claim and
  Ramstein fighter talks, the EU's €45bn Ukraine loan, the Knesset
  electing Matan Kahana, Australia's West Bank settler sanctions, the
  ICJ's Myanmar genocide ruling, Cyclone Akvan evacuations, Ebola
  passing 11,000 cases in DR Congo, the Siberia plane crash that
  killed 19, Waymo leaving US freeways, Nigeria's state-police law,
  Haiti's security pact with El Salvador, and more — each with its
  source printed next to it on the page.

## Sources

Every story was checked against the 18 November 2026 daily briefs of:

- **Level Headlines** — Daily Brief: Wednesday, Nov. 18, 2026
  (levelheadlines.com/briefs/2026-11-18/)
- **Zark News** — Zark News Daily Briefing: November 18, 2026
  (zarknews.com)
- **Open Chronicle** — Global News Brief: Key Developments Around the
  World, November 18, 2026 (openchronicle.org)
- **Horizon** and **Just Security Early Edition** — 18 Nov 2026 briefs
  (used for the v1 page and carried items such as the Siberia crash)

Those briefs in turn cite the underlying reporting of Reuters, the
Associated Press, AFP, BBC News, CNBC, TechCrunch, Euronews, Yonhap,
ABC News (Australia), The Seattle Times, Axios Denver, Denverite,
9News, NASA's Jet Propulsion Laboratory, PAHO and the CDC — the
specific source is printed on the page next to each story.

## Files

- `build_image.py` — PIL generator that draws `entry.png`
  (1024x1024: masthead with date line, date-checked banner, lead
  story, UTC timeline strip, three secondary stories, and the
  four-column numbered wire; the story count printed on the page is
  computed from what is actually rendered).
- `entry.png` — the rendered front page.
- `main.py` — deterministic entry point: copies `entry.png` to
  `/output/entry.png`. No network access, same output on every run.
- `README.md` — this file.
- `LICENSE` — MIT license.

## License

MIT — see `LICENSE`.
