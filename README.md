# 18 November 2026: the world in one front page

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/kai0x3/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/kai0x3/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

Entry for "Sum up 18 November's world news in one image" ($250, 50 places paid).
Free entry, no fee. Ends Fri 20 Nov 2026 00:00 UTC (07:00 WIB).

A single 1024x1024 newspaper front page summing up the world news of
Wednesday 18 November 2026, drawn with PIL (see `build_image.py`).

## Headlines

- **Lead — Xi and Putin meet in Shenzhen:** Xi Jinping and Vladimir Putin
  meet ahead of the first-ever three-way summit with Donald Trump on
  Thursday.
- **US–Iran strikes:** the US strikes an Iranian missile site on Qeshm
  Island; Iran fires back at US bases in Kuwait (Ali Al Salem Air Base)
  and Bahrain.
- **Democrats take Senate:** Mary Peltola wins Alaska's Senate race,
  giving Democrats a 56–44 Senate majority.
- **Measles status lost:** the US loses measles-elimination status after
  26 years, with 5,400+ cases in 2026.
- **Nvidia beats forecasts:** Q3 revenue of $115.8 billion.
- **Also in the footer:** Voyager 1 reaches one light-day from Earth;
  the Ebola outbreak in DR Congo passes 11,000 cases; a Russian
  military plane crashes in Siberia, killing 19; Trump announces a
  Philippines trade deal; Houthi drones target a Saudi pipeline; Matan
  Kahana is elected speaker of Israel's Knesset.

## Sources

Headlines were verified against the 18 November 2026 daily briefs of:

- Level Headlines
- Just Security Early Edition
- Zark News
- Open Chronicle
- Horizon

## Files

- `build_image.py` — PIL generator that draws `entry.png`
  (1024x1024, newspaper front page: masthead, lead story with a
  globe-and-flags illustration, 2x2 story grid, footer).
- `entry.png` — the rendered front page.
- `main.py` — deterministic entry point: copies `entry.png` to
  `/output/entry.png`. No network access, same output on every run.
- `README.md` — this file.
- `LICENSE` — MIT license.

## License

MIT — see `LICENSE`.
