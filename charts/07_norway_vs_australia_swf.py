"""Chart 07: Per-citizen sovereign wealth — Norway vs Australia, in AUD.

Headline: A Norwegian's share of the petroleum fund is worth A$494,000.
An Australian's share of the (main) Future Fund is worth A$10,050.

Data (FX per data/values.yml.fx_rates, RBA F11.1 daily fix):
- Norway GPFG end-2025: NOK 21,268 bn x 0.130 AUD/NOK.
  Output: A$2.76 trillion; population 5.59 m.  # not-fx
- Australia main Future Fund 31 Dec 2025: A$267.4 bn (native AUD). Pop 26.6 m.
  (v3.0.4 Bucket C correction: previously used A$335.3 bn, which is the Future
  Fund Board's total managed funds — Medical Research Future Fund, DisabilityCare
  Australia Fund, Future Drought Fund, etc., combined. The headline "Australia's
  Future Fund" in prose refers to the main Fund only.)
- Per-resident in AUD: Norway A$494,000 (NOK 21,268 bn x 0.130 / 5.59m);
  Australia A$10,050 (A$267.4 bn / 26.6m).
- (Per-resident in USD: see dossier 08.)
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
    V = load_values()["swf_aud_per_resident"]
    countries = ["Norway\n(Government Pension Fund Global,\nentirely from petroleum)",
                 "Australia\n(Future Fund — general purpose,\nnot a resource fund)"]
    per_resident_aud = [V["Norway"], V["Australia_Future"]]
    cols = [COLORS["primary"], COLORS["accent"]]

    fig, ax = plt.subplots(figsize=(10, 5.8))
    bars = ax.bar(countries, per_resident_aud, color=cols, edgecolor="white",
                  linewidth=0.6, width=0.55)  # not-fx; bar width
    for bar, v in zip(bars, per_resident_aud):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 12_000,
                f"A${v:,}",
                ha="center", fontsize=12, color=COLORS["ink"],
                weight="bold")

    ax.set_ylim(0, max(per_resident_aud) * 1.13)  # not-fx; axis padding multiplier
    ax.set_ylabel("Sovereign wealth fund AUM per resident (AUD)")
    set_chart_title(ax,
        f"Norway's petroleum fund per resident: A${per_resident_aud[0]:,}. "
        f"Australia's Future Fund: A${per_resident_aud[1]:,}.")
    ax.ticklabel_format(axis="y", style="plain")
    ax.set_yticks([0, 100_000, 200_000, 300_000, 400_000, 500_000])
    ax.set_yticklabels(["A$0", "A$100k", "A$200k", "A$300k", "A$400k", "A$500k"])

    multiplier = round(per_resident_aud[0] / per_resident_aud[1])
    ax.annotate(f"≈ {multiplier}× Australia",
                xy=(0, per_resident_aud[0]), xytext=(0.35, per_resident_aud[0] - 54_000),  # not-fx; annotation x-position
                fontsize=11, color=COLORS["ink"], style="italic")
    fig.text(0.5, 0.06,  # not-fx; figure text position
            "Note: Australia's Future Fund is general-purpose (Telstra IPO + budget surpluses), not a resource fund.\n"
            "A counterfactual gas-rent fund built at Qatar take-rates since 2010 would be of order A$700-900 bn "
            "(~A$26k–A$34k per resident).",
            fontsize=8.5, color=COLORS["ink"], style="italic",
            ha="center", parse_math=False)
    fig.subplots_adjust(bottom=0.22)  # not-fx; layout margin

    SVG.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / "07_norway_vs_australia_swf.png")
    fig.savefig(SVG / "07_norway_vs_australia_swf.svg")
    plt.close(fig)
    print("Wrote", OUT / "07_norway_vs_australia_swf.png")


if __name__ == "__main__":
    main()
