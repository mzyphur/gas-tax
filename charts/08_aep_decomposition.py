"""Chart 08: The industry's "A$21.9 billion" claim — decomposed.

Headline: Industry's headline number is real, but PRRT is only A$1.35 bn
of it — and royalties aren't a tax, they're a purchase price.

Uses grouped vertical bars so each component and value label remains legible.

Data: AEP media release 27 July 2025 (2024-25 figures); Australia Institute
critique (Campbell May 2024).
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
    P = load_values()["aep_2024_25_aud_bn"]["precise"]
    labels = [
        "Company\nincome tax",
        "State royalties,\nexcise & fees",
        "Petroleum Resource\nRent Tax (PRRT)",
        "All other taxes",
    ]
    values = [P["company_income_tax"], P["royalties_excise"],
              P["prrt"], P["all_other"]]
    cols   = [COLORS["neutral_dark"], COLORS["secondary"], COLORS["accent"],
              COLORS["neutral_dark"]]
    total  = sum(values)

    fig, ax = plt.subplots(figsize=(11, 5.6))
    x = np.arange(len(labels))
    bars = ax.bar(x, values, color=cols, edgecolor="white", linewidth=0.6,
                  width=0.65)

    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 0.35,
                f"A${v:.2f} bn",
                ha="center", va="bottom", fontsize=12,
                color=COLORS["ink"], weight="bold")

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=10.5)
    ax.set_ylim(0, max(values) * 1.18)
    ax.set_ylabel("Contribution to government (A$ billion, 2024-25)")
    set_chart_title(ax, f"Of the gas industry's A${total:.2f} bn 'contribution', PRRT is just A${values[2]:.2f} bn.")

    ax.annotate(
        "Australia Institute critique: royalties\n"
        "are 'a purchase price for petroleum\n"
        "resources owned by the community',\n"
        "not a tax (Campbell, May 2024).",
        xy=(1.18, values[1] - 0.7), xytext=(1.70, 9.55),
        arrowprops={"arrowstyle": "-", "lw": 0.6, "color": COLORS["ink_soft"]},
        fontsize=9.5, color=COLORS["ink_soft"], style="italic", ha="left",
        bbox=dict(boxstyle="square,pad=0.5", fc="none", ec=COLORS["ink_soft"], lw=0.5),
    )

    SVG.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / "08_aep_decomposition.png")
    fig.savefig(SVG / "08_aep_decomposition.svg")
    plt.close(fig)
    print("Wrote", OUT / "08_aep_decomposition.png")


if __name__ == "__main__":
    main()
