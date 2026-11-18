[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/gregorionainggolan8-tech/makefun-news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/gregorionainggolan8-tech/makefun-news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

# THE WORLD TODAY — Wednesday, 18 November 2026

A newspaper front page that sums up the world's news of Wednesday
18 November 2026 in a single 1024×1024 image, drawn from scratch with
Python + Pillow (`make_image.py`). The program (`main.ts`) simply copies
the finished image to the output directory; no network, no dependencies,
and the output is byte-identical on every run.

## Stories on the page

**Lead — U.S. jets strike Iran as tankers burn in Hormuz.** Washington
says its jets hit a Revolutionary Guard missile site on Qeshm Island
after Iranian drones targeted a U.S. radar base in Bahrain, and five
Iranian oil tankers were sunk in the Gulf of Oman as the Gulf crisis
deepened overnight.

**Cyclone Akvan bears down on India.** The storm over the Bay of Bengal
is set to become a severe cyclone, with landfall on the Andhra Pradesh
coast expected on Friday.

**Nvidia doubles its revenue.** $115.8 billion in quarterly revenue, up
103% on a year ago, with net profit of $65.3 billion as AI data-centre
demand keeps soaring.

**Ukraine hits Crimea Bridge again.** Kyiv struck the bridge to occupied
Crimea for a second night, collapsing a road section, as Russia hit
bridges of its own ahead of Thursday's summit.

**COP31 enters decisive phase.** Climate negotiators in Antalya work
through a first draft deal with 144 disputed items, calling for a shift
from fossil fuels and at least $120 billion for adaptation.

**Gaza faces a cold winter.** The UN warns of more deaths from exposure:
over 1.7 million people remain displaced and about 1.4 million face
acute hunger.

**Russian plane crash kills 19.** A military transport aircraft crashed
in the Kemerovo region of Siberia, killing all 19 on board.

**Also today (footer ticker):** Robert Pattinson named the new James
Bond; North Korea launches a missile into the Sea of Japan; India and
Japan hold 2+2 talks in Tokyo; a gas tanker sinks off Bulgaria with all
19 crew rescued.

## How to run / rebuild

```sh
# Re-draw the image from scratch (needs Python 3 + Pillow)
python3 make_image.py

# Run the entrypoint (needs Node 22)
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
# -> out/entry.png
```

## License

MIT — see `LICENSE`.
