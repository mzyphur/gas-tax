"""Chart 09: Major LNG exporters — Australian income vs Australian income tax,
seven years 2014-2020.

Headline: A$216 billion of revenue, A$6 million of income tax. From Santos.

Data: ATO Corporate Tax Transparency Reports compiled by the Australia
Institute ("APPEA members pay no income tax on income of A$138 bn").
"""

from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from style import apply_style, COLORS, set_chart_title

apply_style()
OUT = Path(__file__).parent / "png"
SVG = Path(__file__).parent / "svg"


def main() -> None:
    entities = ["ExxonMobil",  "Chevron",  "Santos",   "APLNG",    "Arrow",   "Senex"]
    revenue  = [71.248,        43.695,     28.771,     50.2,       1.894,     0.906]
    inc_tax  = [0,             0,          0.006,      0,          0,         0]
    # APLNG and revenue rounded to dossier 02 figures (2014-15 to 2022-23
    # cumulative); Arrow / Senex / etc are 2014-2020 per AI Institute.

    n = len(entities)
    x = np.arange(n)
    w = 0.40
    # Revenue bars in slate (neutral_dark) — these are volume bars, not
    # the rhetorical centre. The tax bars (every one zero or near-zero)
    # are the actual story; their "A$0" labels render in accent red so
    # the "zero across the board" reading is the visual punchline.
    fig, ax = plt.subplots(figsize=(11, 5.6))
    rev_bars = ax.bar(x - w/2, revenue, width=w,
                      color=COLORS["neutral_dark"], label="Australian revenue (A$ bn)")
    tax_bars = ax.bar(x + w/2, inc_tax, width=w,
                      color=COLORS["neutral_mid"], label="Australian income tax paid (A$ bn)")

    ax.set_xticks(x)
    ax.set_xticklabels(entities, fontsize=10)
    ax.set_ylabel("A$ billions")
    ax.set_ylim(0, max(revenue) * 1.18)
    set_chart_title(ax, "ExxonMobil: A$71 bn revenue, A$0 income tax. Chevron: A$44 bn revenue, A$0 income tax.")
    ax.legend(loc="upper right", frameon=False, fontsize=10)

    for xi, r in zip(x, revenue):
        ax.text(xi - w/2, r + 1.2, f"A${r:.1f} bn", ha="center", fontsize=9,
                color=COLORS["ink"])
    for xi, t in zip(x, inc_tax):
        label = f"A${t:.0f} bn" if t > 0 else "A$0"
        if t > 0 and t < 0.5:
            label = "A$6 m"
        # Tax labels render in accent red to make "zero across the
        # board" the chart's visual punchline (§13 — one element /
        # consistent purpose per chart).
        ax.text(xi + w/2, max(t, 0) + 1.2, label, ha="center", fontsize=10,
                color=COLORS["accent"], weight="bold")

    ax.annotate(
        "Six APPEA members combined:\n"
        "A$196 bn revenue\n"
        "A$6 million income tax",
        xy=(2, 60), xytext=(2.2, 61.5),
        fontsize=10, color=COLORS["ink"], style="italic",
        bbox=dict(boxstyle="square,pad=0.5", fc="none", ec=COLORS["ink_soft"], lw=0.5),
    )

    SVG.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / "09_entity_level_zeros.png")
    fig.savefig(SVG / "09_entity_level_zeros.svg")
    plt.close(fig)
    print("Wrote", OUT / "09_entity_level_zeros.png")


if __name__ == "__main__":
    main()
