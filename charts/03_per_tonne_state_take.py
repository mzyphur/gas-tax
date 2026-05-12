"""Chart 03: Government revenue per tonne of LNG-equivalent exported.

Headline: Australia is the rich-world outlier — by an order of magnitude.

Data from dossier 04_international_comparison.md (per-tonne calculations
from 2024 government petroleum revenue / 2024 LNG-equivalent export volume,
USD per tonne).
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
    # FX rates per data/values.yml.fx_rates (RBA F11.1 daily fix).
    # Gas-only attribution: each country's total petroleum revenue is
    # apportioned by gas's share of production volume.
    #
    # Norway 2024: 50% gas share x NOK 702 bn (actual, Statsbudsjettet
    #              2026) x 0.130 / 93 Mt LNG-eq = A$491/t
    # Qatar 2024:  85% gas share x USD 47.5 bn x 1.384 / 77 Mt = A$725/t
    # Malaysia 2024: 95% gas share x A$25.6 bn / 35.7 Mt LNG = A$682/t
    # USA FY2024:  55% gas share x USD 7.0 bn x 1.384 / 88 Mt = A$61/t
    # Australia FY2024-25: A$4 bn (PRRT + state royalties + NWS)
    #              / 82 Mt = A$49/t
    #
    # Bar order from largest take-rate (top) to smallest (bottom).
    V = load_values()["per_tonne_state_take_aud"]
    #   Norway       → primary blue (the benchmark referenced throughout)
    #   Australia    → accent red (the outlier the chart is about)
    #   Every other  → slate (neutral_dark)
    # The previous "rainbow" encoding (Qatar teal / Malaysia slate /
    # USA light grey) read as non-systematic — a different non-meaningful
    # hue per country with no purpose beyond differentiation.
    countries = ["Qatar", "Malaysia", "Norway", "USA\n(offshore)", "Australia"]
    take_aud  = [V["Qatar"], V["Malaysia"], V["Norway"], V["USA_offshore"], V["Australia"]]
    cols      = [COLORS["neutral_dark"], COLORS["neutral_dark"], COLORS["primary"],
                 COLORS["neutral_dark"], COLORS["accent"]]

    fig, ax = plt.subplots(figsize=(10, 5.8))
    bars = ax.barh(countries, take_aud, color=cols, edgecolor="white", linewidth=0.5)
    ax.invert_yaxis()
    ax.set_xlim(0, max(take_aud) * 1.22)  # not-fx; axis padding multiplier
    ax.set_xlabel("AUD per tonne of LNG-equivalent gas exported, 2024 (gas-only attribution)")
    set_chart_title(ax, "Per tonne of gas, Norway extracts ~10× Australia. Qatar ~15×. (Gas-only attribution.)")

    for bar, v in zip(bars, take_aud):
        ax.text(v + 14, bar.get_y() + bar.get_height() / 2,
                f"A${v:,}/t",
                va="center", ha="left", fontsize=11,
                color=COLORS["ink"], weight="bold")

    norway_x = V["Norway"]
    qatar_x  = V["Qatar"]
    norway_mult = round(V["Norway"] / V["Australia"])
    qatar_mult  = round(V["Qatar"]  / V["Australia"])
    ax.annotate(
        f"{norway_mult}× Australia",
        xy=(norway_x, 2), xytext=(norway_x + 34, 2.35),  # not-fx; annotation y-position
        fontsize=10, color=COLORS["ink"], style="italic",
    )
    ax.annotate(
        f"{qatar_mult}× Australia",
        xy=(qatar_x, 0), xytext=(qatar_x + 35, 0.35),
        fontsize=10, color=COLORS["ink"], style="italic",
    )

    SVG.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / "03_per_tonne_state_take.png")
    fig.savefig(SVG / "03_per_tonne_state_take.svg")
    plt.close(fig)
    print("Wrote", OUT / "03_per_tonne_state_take.png")


if __name__ == "__main__":
    main()
