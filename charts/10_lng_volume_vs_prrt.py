"""Chart 10: LNG export volume vs PRRT receipts — the divergence.

Headline: LNG production quadrupled. PRRT did not move.

Data: DISR Resources and Energy Quarterly (LNG volume) + Treasury FBO cash receipts (PRRT).
"""

from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt

from style import apply_style, COLORS, set_chart_title
from values import load_values

apply_style()
OUT = Path(__file__).parent / "png"
SVG = Path(__file__).parent / "svg"


def main() -> None:
    # Approximate Australian LNG export volumes in Mt/yr (financial year).
    # 2010-11 ~ 19 Mt; 2014-15 ~ 24 Mt; 2018-19 ~ 76 Mt;
    # 2020-21 ~ 78 Mt; 2022-23 ~ 80 Mt; 2024-25 ~ 82 Mt.
    # PRRT receipts are sourced from data/values.yml.prrt_history_cash_receipts_aud_million
    # — the same canonical series Chart 01 uses.
    H = load_values()["prrt_history_cash_receipts_aud_million"]["by_fy"]
    fy = ["10-11", "12-13", "14-15", "16-17", "18-19", "20-21", "22-23", "24-25"]
    volume_mt = [19, 22, 24, 50, 76, 78, 80, 82]
    prrt_bn = [H[k] / 1000 for k in fy]  # manifest is in A$ million; chart shows A$ bn
    # not accent red. Accent red was previously applied to every bar
    # (8 elements) which inverted public style guide §13 ("one element on
    # the page, not five"). A single red callout at the FY 14-15
    # inflection — where LNG quadrupled and PRRT didn't move — carries
    # the rhetorical centre.
    fig, ax1 = plt.subplots(figsize=(11, 5.6))
    color_v = COLORS["primary"]
    ax1.plot(fy, volume_mt, color=color_v, marker="o", linewidth=2.4,
             markersize=9, label="LNG exports (Mt/yr)")
    ax1.set_ylabel("LNG exports (million tonnes / year)", color=color_v)
    ax1.set_ylim(0, 100)
    ax1.set_yticks([0, 20, 40, 60, 80, 100])   # 5 gridline tiers
    ax1.tick_params(axis="y", labelcolor=color_v)

    ax2 = ax1.twinx()
    color_p = COLORS["neutral_dark"]
    ax2.bar(fy, prrt_bn, color=color_p, alpha=0.85, width=0.55,
            label="PRRT receipts (A$ bn)")
    ax2.set_ylabel("PRRT receipts (A$ billion / year)",
                   color=COLORS["ink_soft"])
    # ─── Lock the right-axis ticks to the SAME 5 tiers as the left axis.
    # Without this, matplotlib lays gridlines on the right-axis (10-tier)
    # grid while the left-axis labels (6-tier) sit at different
    # positions — so the horizontal lines appear to pass through
    # arbitrary places in the chart.
    ax2.set_ylim(0, 4.5)
    ax2.set_yticks([0, 0.9, 1.8, 2.7, 3.6, 4.5])  # 5 tiers, matching left axis
    ax2.tick_params(axis="y", labelcolor=COLORS["ink_soft"])
    # And turn off the right-axis gridlines entirely so the only
    # horizontal rules are the (now-aligned) primary gridlines.
    ax2.grid(False)

    set_chart_title(ax1, "LNG volume quadrupled (19 → 82 Mt). PRRT did not.")

    # Single red callout at the FY 14-15 inflection — the rhetorical
    ax1.annotate(
        "FY14-15: LNG quadruples\n"
        f"({volume_mt[0]} → {volume_mt[-1]} Mt over the\n"
        "decade) — PRRT does not",
        xy=(2, 24), xytext=(0.3, 60),
        arrowprops={"arrowstyle": "->", "lw": 0.8, "color": COLORS["accent"]},
        fontsize=9.5, color=COLORS["accent"], style="italic", weight="bold",
    )

    SVG.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / "10_lng_volume_vs_prrt.png")
    fig.savefig(SVG / "10_lng_volume_vs_prrt.svg")
    plt.close(fig)
    print("Wrote", OUT / "10_lng_volume_vs_prrt.png")


if __name__ == "__main__":
    main()
