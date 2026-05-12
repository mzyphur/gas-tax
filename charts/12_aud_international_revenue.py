"""Chart 12: Annual government revenue from petroleum/gas, AUD billions.

Headline: Norway A$91 bn/yr from petroleum. Qatar A$66 bn/yr. Australia
A$4 bn/yr from rent + royalty instruments alone (A$17.5 bn including
LNG-attributable company income tax).

Data (FX per colophon / sources/fx_rates.md, RBA F11.1 2026-05-11):
- Norway 2024 state petroleum net cash flow: NOK 702 bn x 0.130 = A$91.3 bn
- Qatar 2024 hydrocarbon revenue:            USD 47.5 bn x 1.384 = A$65.7 bn
- Malaysia 2024 Petronas total contribution: RM 72.4 bn x 0.353 = A$25.6 bn
- USA FY2024 federal energy revenue:         USD 16.45 bn  # not-fx
  x 1.384 = A$22.8 bn (all fuels)
- UK 2024-25 petroleum receipts:             GBP 4.5 bn x 1.879 = A$8.5 bn
- Australia 2024-25 all heads incl. LNG-attributable CIT (AEP):       A$17.5 bn
- Australia 2024-25 rent + royalty instruments only:                  A$4.0 bn
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
    V = load_values()
    R = V["international_revenue_aud_bn"]
    N = V["international_revenue_native"]
    # Norway → primary blue (benchmark); every other comparator country
    # → slate (neutral_dark); Australia → accent (single emphasis bar).
    # The two Australia bars previously rendered as a double-accent
    # smudge; here the rent-only bar (the rhetorical headline) keeps
    # accent red and the all-heads bar drops to slate with an explicit
    # "+CIT" annotation so the two are read as a hierarchy, not a duet.
    countries = [
        (f"Norway\n(state petroleum net cash flow 2024, NOK {N['Norway_NOK_bn']:.0f} bn)",      R["Norway"],                COLORS["primary"]),
        (f"Qatar\n(hydrocarbon revenue 2024, USD {N['Qatar_USD_bn']:.1f} bn)",                  R["Qatar"],                 COLORS["neutral_dark"]),
        (f"Malaysia\n(Petronas to gov't 2024, RM {N['Malaysia_RM_bn']:.1f} bn)",                R["Malaysia"],              COLORS["neutral_dark"]),
        (f"USA\n(federal energy revenue FY2024, USD {N['USA_USD_bn']:.2f} bn — all fuels)",     R["USA"],                   COLORS["neutral_dark"]),
        (f"UK\n(petroleum receipts 2024-25, GBP {N['UK_GBP_bn']:.1f} bn)",                      R["UK"],                    COLORS["neutral_dark"]),
        ("Australia — all heads incl. LNG-attributable CIT",                                    R["Australia_all_heads"],    COLORS["neutral_dark"]),
        ("Australia — rent + royalty instruments only",                                         R["Australia_rent_royalty"], COLORS["accent"]),
    ]
    labels  = [c[0] for c in countries]
    values  = [c[1] for c in countries]
    cols    = [c[2] for c in countries]

    fig, ax = plt.subplots(figsize=(11, 6.4))
    y = np.arange(len(countries))[::-1]
    bars = ax.barh(y, values, color=cols, edgecolor="white", linewidth=0.6)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlabel("Annual government petroleum/gas revenue (A$ billion)")
    ax.set_xlim(0, 110)
    set_chart_title(ax, "Norway's annual gas/oil revenue: A$91 bn. Qatar: A$66 bn. Australia: A$4 bn (rent + royalty) / A$17.5 bn (all heads).")

    for yi, v in zip(y, values):
        ax.text(v + 1.5, yi, f"A${v:.1f} bn",
                va="center", fontsize=11, color=COLORS["ink"], weight="bold")

    SVG.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / "12_aud_international_revenue.png")
    fig.savefig(SVG / "12_aud_international_revenue.svg")
    plt.close(fig)
    print("Wrote", OUT / "12_aud_international_revenue.png")


if __name__ == "__main__":
    main()
