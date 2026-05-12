"""Chart 02: PRRT as a share of LNG export value, FY2013-14 to FY2024-25.

Headline: PRRT used to capture 8 cents of every dollar of LNG exports.
Now it captures 2 cents.

Data:
- PRRT receipts from Treasury Final Budget Outcomes (dossier 01).
- LNG export value from DISR Resources and Energy Quarterly.
"""

from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt

from style import apply_style, COLORS, set_chart_title

apply_style()
OUT = Path(__file__).parent / "png"
SVG = Path(__file__).parent / "svg"


def main() -> None:
    years   = ["2013-14", "2017-18", "2019-20", "2021-22", "2022-23", "2023-24", "2024-25"]
    pct     = [8.4, 3.6, 2.2, 2.3, 2.5, 1.7, 2.2]
    # Accent red reserved for the FY 2023-24 nadir marker — the single
    # data point the chart's headline calls out ("now captures 2"). All
    # other markers and the line itself are primary blue. Per v2.2.0
    NADIR_IDX = pct.index(min(pct))

    fig, ax = plt.subplots(figsize=(10, 5.6))
    ax.plot(years, pct, marker="o", markersize=10, linewidth=2.4,
            color=COLORS["primary"], markerfacecolor=COLORS["primary"],
            markeredgecolor=COLORS["primary"])
    # Highlight the nadir with an accent-red ring around the marker
    ax.plot([years[NADIR_IDX]], [pct[NADIR_IDX]], marker="o",
            markersize=15, markerfacecolor="none",
            markeredgecolor=COLORS["accent"], markeredgewidth=2.0)
    for i, (y, p) in enumerate(zip(years, pct)):
        ax.annotate(f"{p}%", (y, p), textcoords="offset points",
                    xytext=(0, 12), ha="center", fontsize=10,
                    color=COLORS["accent"] if i == NADIR_IDX else COLORS["ink"],
                    weight="bold")

    ax.set_ylim(0, 12)
    ax.set_ylabel("PRRT receipts as % of LNG export value")
    set_chart_title(ax, "PRRT used to capture 8 cents per LNG dollar. Now it captures 2.")

    # Sub-3% zone band — slate tint instead of accent red, per §13.
    ax.axhspan(0, 3, color=COLORS["neutral_mid"], alpha=0.10, zorder=0)
    ax.text(0.02, 1.5, "Sub-3% zone\n(post-LNG-boom)",
            fontsize=9, color=COLORS["ink_soft"], style="italic",
            transform=ax.get_yaxis_transform())

    # public style guide §8.2: source line moved to markdown caption.
    # Original add_footer call retained as a comment:
    #   add_footer(fig,
    #       "Sources: PRRT — Treasury Final Budget Outcomes; LNG export "
    #       "value — DISR Resources and Energy Quarterly, Dec 2024 Table "
    #       "6.1 / Sept 2025.")
    SVG.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / "02_prrt_share_of_lng_value.png")
    fig.savefig(SVG / "02_prrt_share_of_lng_value.svg")
    plt.close(fig)
    print("Wrote", OUT / "02_prrt_share_of_lng_value.png")


if __name__ == "__main__":
    main()
