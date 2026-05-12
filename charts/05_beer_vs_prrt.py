"""Chart 05: Beer excise vs PRRT - the Pocock comparison.

Headline: Australians pay more tax on their beer than the gas industry pays
under the PRRT - every year, including this one.

Data: Treasury Final Budget Outcomes + Budget Paper 1 2025-26 + Senate
Estimates Feb 2026 testimony confirmation (Treasury officials).
"""

from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np

from style import apply_style, COLORS, set_chart_title
from values import load_values

apply_style()
OUT = Path(__file__).parent / "png"
SVG = Path(__file__).parent / "svg"


def main() -> None:
    V = load_values()["beer_vs_prrt_aud_bn"]
    fy_keys = ["20-21", "21-22", "22-23", "23-24", "24-25", "25-26"]
    years = ["2020-21", "2021-22", "2022-23", "2023-24", "2024-25", "2025-26f"]
    beer = [V["beer"][k] for k in fy_keys]
    prrt = [V["prrt"][k] for k in fy_keys]
    # Accent red reserved for the single emphasised bar (the 2025-26 PRRT
    # forecast - the year named in the headline) per public style guide
    # Section 13. Other PRRT bars use primary blue; beer bars use neutral
    # mid grey throughout.
    EMPHASIS_IDX = len(years) - 1

    x = np.arange(len(years))
    w = 0.38
    fig, ax = plt.subplots(figsize=(11, 5.6))
    ax.bar(x - w/2, beer, width=w, color=COLORS["neutral_mid"])
    prrt_cols = [COLORS["accent"] if i == EMPHASIS_IDX else COLORS["primary"]
                 for i in range(len(years))]
    ax.bar(x + w/2, prrt, width=w, color=prrt_cols)

    for xi, b, p in zip(x, beer, prrt):
        ax.text(xi - w/2, b + 0.05, f"A${b:.2f} bn", ha="center", fontsize=9,
                color=COLORS["ink"])
        ax.text(xi + w/2, p + 0.05, f"A${p:.2f} bn", ha="center", fontsize=9,
                color=COLORS["ink"])

    ax.set_xticks(x)
    ax.set_xticklabels(years, fontsize=10)
    ax.set_ylabel("Revenue (A$ billion)")
    ax.set_ylim(0, 3.4)
    set_chart_title(ax, "Australians pay more tax on beer than the gas industry pays in PRRT - every year.")

    # Direct labels at the FIRST bar of each series (left edge), not
    # the last — the previous right-edge placement collided with the
    # layout-defect fix.
    ax.text(x[0] - w/2, beer[0] + 0.18, "Beer excise",
            ha="center", va="bottom", fontsize=10, fontweight="semibold",
            color=COLORS["neutral_dark"])
    ax.text(x[0] + w/2, prrt[0] + 0.18, "PRRT (oil + gas)",
            ha="center", va="bottom", fontsize=10, fontweight="semibold",
            color=COLORS["accent"])

    # Pull-quote box moved up and right-edge-aligned so it sits above
    # the last-year bars (where the headline year is) rather than
    # collide with the series labels at the chart's left edge.
    ax.annotate(
        'Senator Pocock to Treasury, Senate Estimates Feb 2026:\n'
        '"How do we live in a country, one of the biggest gas exporters\n'
        ' in the world, and we\'re getting more tax from beer than PRRT?"',
        xy=(5, 2.7), xytext=(2.7, 3.05),
        fontsize=9, color=COLORS["ink"], style="italic", ha="left",
        bbox=dict(boxstyle="square,pad=0.5", fc="none", ec=COLORS["ink_soft"], lw=0.5),
    )

    SVG.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / "05_beer_vs_prrt.png")
    fig.savefig(SVG / "05_beer_vs_prrt.svg")
    plt.close(fig)
    print("Wrote", OUT / "05_beer_vs_prrt.png")


if __name__ == "__main__":
    main()
