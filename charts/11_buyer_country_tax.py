"""Chart 11: Per-tonne tax extraction by Australia's major LNG buyers.

Headline: At the downstream / import end, Japan extracts ~A$16/t. China,
Taiwan extract nothing. Australia extracts ~A$0/t of PRRT from the
offshore LNG projects that produced the gas.

Data: Japan PCT JPY 1,860/t x 0.00883.
This equals A$16.42/t (RBA F11.1 2026-05-11).  # not-fx
South Korea KRW 12/kg excise + KRW 3,800/t import surcharge = A$14.80/t  # not-fx
at 1 KRW = A$0.0009365 (RBA F11.1 2026-05-11); KAFTA customs duty is 0%.  # not-fx
China + Taiwan zero. From dossier 07.
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
    V = load_values()["buyer_country_per_tonne_aud"]
    buyers      = ["Japan",  "South Korea",  "Taiwan",  "China",  "Australia\n(PRRT from offshore\nLNG projects)"]
    take_aud_t  = [V["Japan"], V["South_Korea"], V["Taiwan"], V["China"], V["Australia_offshore"]]
    cols        = [COLORS["primary"], COLORS["neutral_dark"], COLORS["neutral_mid"],
                   COLORS["neutral_mid"], COLORS["accent"]]

    fig, ax = plt.subplots(figsize=(11, 5.4))
    x = np.arange(len(buyers))
    bars = ax.bar(x, take_aud_t, color=cols, edgecolor="white",
                  linewidth=0.6, width=0.6)
    ax.set_xticks(x)
    ax.set_xticklabels(buyers, fontsize=10)
    ax.set_ylabel("Fuel-specific tax extracted, AUD per tonne LNG")
    ax.set_ylim(0, 22)
    set_chart_title(ax, "Australia's own offshore LNG projects pay less PRRT per tonne than Japan extracts at import.")

    for xi, v in zip(x, take_aud_t):
        ax.text(xi, max(v, 0.5) + 0.6,
                f"A${v:.2f}/t" if v > 0 else "A$0",
                ha="center", fontsize=11, color=COLORS["ink"],
                weight="bold")

    ax.annotate(
        "Australia's offshore LNG projects\nhave paid effectively zero PRRT in\ntheir entire production history",
        xy=(4, 0.15), xytext=(4.0, 15.2),
        arrowprops={"arrowstyle": "-", "lw": 0.6, "color": COLORS["ink_soft"]},
        fontsize=9.5, color=COLORS["ink_soft"], ha="center", va="top",
        bbox=dict(boxstyle="square,pad=0.5", fc="none", ec=COLORS["ink_soft"], lw=0.5),
    )

    SVG.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / "11_buyer_country_tax.png")
    fig.savefig(SVG / "11_buyer_country_tax.svg")
    plt.close(fig)
    print("Wrote", OUT / "11_buyer_country_tax.png")


if __name__ == "__main__":
    main()
