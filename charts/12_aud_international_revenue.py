"""Chart 12: Annual government revenue from petroleum/gas, AUD billions.

Headline: Norway A$91 bn/yr from petroleum. Qatar A$66 bn/yr. Australia
A$4 bn/yr from rent + royalty instruments alone.

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

from style import apply_style, COLORS, set_chart_title, save_chart
from values import load_values

apply_style()
OUT = Path(__file__).parent / "png"
SVG = Path(__file__).parent / "svg"


def main() -> None:
    V = load_values()
    R = V["international_revenue_aud_bn"]
    N = V["international_revenue_native"]
    # Norway is the benchmark; Australia is the single focal bar.
    # The broader Australia all-heads figure is retained as an annotation
    # so the chart does not ask readers to compare two Australia rows.
    countries = [
        (f"Norway\nNOK {N['Norway_NOK_bn']:.0f} bn, 2024",       R["Norway"],                COLORS["primary"]),
        (f"Qatar\nUSD {N['Qatar_USD_bn']:.1f} bn, 2024",         R["Qatar"],                 COLORS["neutral_dark"]),
        (f"Malaysia\nRM {N['Malaysia_RM_bn']:.1f} bn, 2024",     R["Malaysia"],              COLORS["neutral_dark"]),
        (f"USA\nUSD {N['USA_USD_bn']:.2f} bn, FY2024",           R["USA"],                   COLORS["neutral_dark"]),
        (f"UK\nGBP {N['UK_GBP_bn']:.1f} bn, 2024-25",            R["UK"],                    COLORS["neutral_dark"]),
        ("Australia\nrent + royalty only",                       R["Australia_rent_royalty"], COLORS["accent"]),
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
    set_chart_title(ax, "Norway's annual gas/oil revenue: A$91 bn. Qatar: A$66 bn. Australia: A$4 bn from rent + royalty instruments.")

    for yi, v in zip(y, values):
        ax.text(v + 1.5, yi, f"A${v:.1f} bn",
                va="center", fontsize=11, color=COLORS["ink"], weight="bold")

    aus_y = y[-1]
    ax.annotate(
        f"A${R['Australia_all_heads']:.1f} bn if LNG-attributable\ncompany income tax is included",
        xy=(R["Australia_rent_royalty"], aus_y),
        xytext=(30.0, aus_y + 0.6),
        arrowprops={"arrowstyle": "-", "lw": 0.6, "color": COLORS["ink_soft"]},
        fontsize=9.5, color=COLORS["ink_soft"], ha="left", va="bottom",
        bbox=dict(boxstyle="square,pad=0.35", fc="none", ec=COLORS["ink_soft"], lw=0.5),
    )

    SVG.mkdir(parents=True, exist_ok=True)
    save_chart(fig,
               OUT / "12_aud_international_revenue.png",
               SVG / "12_aud_international_revenue.svg")
    plt.close(fig)
    print("Wrote", OUT / "12_aud_international_revenue.png")


if __name__ == "__main__":
    main()
