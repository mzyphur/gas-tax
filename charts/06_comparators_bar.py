"""Chart 06: Federal revenue heads compared to PRRT (the "hilarious comparators").

Headline: Lots of small Australian taxes raise more than PRRT does.

Data: Budget Paper 1 2025-26 Table 4.7 + dossier 03 (Pocock claims) +
dossier 06 (budget modelling) + Australia Institute / Jericho (HECS).
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
    V = load_values()["australia_2025_26"]
    # All comparator bars in slate; PRRT in accent red as the single
    # emphasised data point. The previous chart had four hues
    # (neutral_dark, neutral_mid, secondary, accent) reading as
    # non-systematic colour-coding; the function of each non-PRRT bar
    # is identical (a "comparator that beats PRRT"), so they all share
    # the comparator colour.
    items = [
        ("Fuel excise (gross, petrol + diesel)",       V["fuel_excise_aud_bn"],         COLORS["neutral_dark"]),
        ("Tobacco excise",                              V["tobacco_excise_aud_bn"],     COLORS["neutral_dark"]),
        ("Alcohol excise (beer + spirits + other)",     V["alcohol_excise_total_aud_bn"], COLORS["neutral_dark"]),
        ("HECS/HELP repayments (2023-24 actual)",       V["hecs_repayments_aud_bn"],    COLORS["neutral_dark"]),
        ("Beer excise alone",                           V["beer_excise_aud_bn"],        COLORS["neutral_dark"]),
        ("Petroleum Resource Rent Tax (PRRT)",          V["prrt_forecast_aud_bn"],      COLORS["accent"]),
        ("Major Bank Levy",                             V["major_bank_levy_aud_bn"],    COLORS["neutral_dark"]),
    ]
    labels  = [t[0] for t in items]
    values  = [t[1] for t in items]
    colours = [t[2] for t in items]

    fig, ax = plt.subplots(figsize=(11, 6.4))
    y = np.arange(len(items))[::-1]
    ax.barh(y, values, color=colours, edgecolor="white", linewidth=0.6)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=10.5)
    ax.set_xlabel("Annual Commonwealth revenue (A$ billion)")
    ax.set_xlim(0, 30)
    set_chart_title(ax, "PRRT raises less than fuel, less than tobacco, less than beer alone, less than HECS.")

    for yi, v in zip(y, values):
        ax.text(v + 0.3, yi, f"A${v:.2f} bn", va="center", fontsize=10,
                color=COLORS["ink"], weight="bold")

    SVG.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / "06_comparators_bar.png")
    fig.savefig(SVG / "06_comparators_bar.svg")
    plt.close(fig)
    print("Wrote", OUT / "06_comparators_bar.png")


if __name__ == "__main__":
    main()
