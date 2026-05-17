"""Chart 04: A$17 billion/year in the current Budget.

Headline: One year's 25% LNG export levy is a Budget-scale amount.

Data: Budget Paper 1 2026-27 Statement 5 Table 5.7 and Statement 6
program tables + Australia Institute / ACTU 25% LNG export-levy estimate.

# red-clusters: 2
This chart legitimately uses two red-accent clusters by design: the
A$17 bn LNG-levy bar (the dominant comparator) and the matching red
dashed axvline reference line at the same value plus its red "A$17.0
bn/yr reference line" label. The general-repo v0.22.0 red-accent
audit gate reads this directive and tolerates the second cluster.
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
    V = load_values()["budget_2026_27_scale_aud_bn"]
    items = [
        ("Underlying cash deficit\n(2026-27)",                 V["underlying_cash_deficit"], COLORS["neutral_dark"]),
        ("JobSeeker Income Support\n(2026-27)",                V["jobseeker_income_support"], COLORS["neutral_dark"]),
        ("Support for Families\n(2026-27)",                   V["support_for_families"], COLORS["neutral_dark"]),
        ("25% LNG export levy\n(Australia Institute / ACTU est.)", V["twenty_five_pct_lng_levy"], COLORS["accent"]),
        ("Child Care Subsidy\n(2026-27)",                     V["child_care_subsidy"], COLORS["neutral_dark"]),
        ("Beer excise\n(2026-27)",                            V["beer_excise"], COLORS["neutral_dark"]),
        ("Petroleum Resource Rent Tax\n(2026-27)",            V["prrt"], COLORS["neutral_dark"]),
    ]
    labels  = [t[0] for t in items]
    costs   = [t[1] for t in items]
    colours = [t[2] for t in items]

    fig, ax = plt.subplots(figsize=(11, 5.6))
    y = np.arange(len(items))[::-1]
    ax.barh(y, costs, color=colours, edgecolor="white", linewidth=0.6)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlabel("Annual Budget scale (A$ billion)")
    ax.set_xlim(0, 34)
    set_chart_title(ax, "A$17 billion a year is Budget-scale money, not a marginal line item.")

    for yi, c in zip(y, costs):
        offset = 0.42 if abs(c - V["twenty_five_pct_lng_levy"]) < 0.2 else 0.18
        ax.text(c + offset, yi, f"A${c:.1f} bn", va="center", fontsize=10,
                color=COLORS["ink"], weight="bold")

    ax.axvline(V["twenty_five_pct_lng_levy"], color=COLORS["accent"], linestyle="--", linewidth=1.3)
    ax.text(V["twenty_five_pct_lng_levy"] + 0.4, len(items) - 0.55,
            "A$17.0 bn/yr reference line",
            fontsize=10, color=COLORS["accent"], weight="bold")

    SVG.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / "04_what_17b_buys.png")
    fig.savefig(SVG / "04_what_17b_buys.svg")
    plt.close(fig)
    print("Wrote", OUT / "04_what_17b_buys.png")


if __name__ == "__main__":
    main()
