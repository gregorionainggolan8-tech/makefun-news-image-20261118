# Build notes — news-image-20261118

Front page "THE WORLD TODAY", drawn from scratch with Python 3 + Pillow
(`make_image.py`, DejaVu fonts). `main.ts` (Node 22, stdlib only) copies
`entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`. No network at run time.

## News stories on the page (Wednesday 18 November 2026)

1. **Lead — U.S. jets strike Iran as tankers burn in Hormuz:** U.S. jets
   hit a Revolutionary Guard missile site on Qeshm Island after Iranian
   drones targeted a U.S. radar base in Bahrain; five Iranian oil tankers
   sunk in the Gulf of Oman.
2. **Cyclone Akvan bears down on India** — severe cyclone forming over
   the Bay of Bengal; Andhra Pradesh landfall expected Friday.
3. **Nvidia doubles its revenue** — $115.8bn quarterly revenue (+103%),
   net profit $65.3bn.
4. **Ukraine hits Crimea Bridge again** — second night of strikes,
   road section collapsed; Russia hit bridges ahead of Thursday's summit.
5. **COP31 enters decisive phase** — Antalya draft deal, 144 disputed
   items, fossil-fuel shift and $120bn adaptation.
6. **Gaza faces a cold winter** — UN warns of more deaths from exposure;
   1.7m displaced, ~1.4m face acute hunger.
7. **Russian plane crash kills 19** — military transport down in
   Kemerovo, Siberia.
8. **Ticker:** Robert Pattinson named the new James Bond; North Korea
   missile launch into the Sea of Japan; India–Japan 2+2 talks in Tokyo;
   gas tanker sinks off Bulgaria, all 19 crew rescued.

## Verification

- `entry.png`: valid PNG, 1024×1024, RGB, 133,871 bytes (< 1 MiB).
- sha256: `0fa6634fb8302b5b50898f447023bba672d2d92f272e9a6671465cfbd8cd565a`
- Determinism: `main.ts` run twice into separate dirs, both outputs
  byte-identical to each other and to `entry.png` (same sha256, `cmp`
  clean), no stderr warnings.
- Revisions during the build: smoke art clamped inside the scene frame
  (was overlapping the headline), layout tightened so the footer ticker
  fits inside the page, ticker shortened to two lines that fit the band.
