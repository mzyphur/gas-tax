"""Chart 04: What A$17 billion/year (a 25% LNG export tax) would buy.

    Headline: One year's gas tax revenue funds universal childcare AND universal
    dental AND indicative mental-health expansion AND 90% bulk-billing — with change.

Data: 2025-26 Commonwealth Budget (BP1 25 March 2025) + Productivity
Commission / PBO / Treasury costings. Sourced via dossier 06.
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
    V = load_values()["seventeen_bn_reforms_aud_bn"]
    # row) was previously secondary teal, reading as "noise" rather
    # than "spec-categorised". Set to neutral_mid so the four canonical
    # primary-source-costed bars are consistently slate and the
    # indicative-only items (Better Access, buffer) are neutral_mid.
    # Accent red is the single dashed reference line at the A$17 bn
    # total — the only red element on the chart.
    #
    # Better Access (mental health) is an order-of-magnitude estimate
    # and lives HERE — not in data/values.yml — per v2.4.0 / C.3:
    # the manifest contract is "single source of truth for VERIFIED
    # canonical numbers"; UNVERIFIED estimates sit in chart-local code
    # with an inline comment. The Figure 4 caption + executive summary
    # both carry the "indicatively" / "order-of-magnitude" framing.
    better_access_aud_bn = 1.5  # UNVERIFIED — order-of-magnitude only;
                                # needs Parliamentary Library / PBO costing
                                # before being relied on for program design.
    items = [
        ("Productivity Commission\nuniversal childcare\n(+top-up to current CCS)", V["pc_universal_childcare"],       COLORS["neutral_dark"]),
        ("Universal dental Medicare\n(Greens / PBO costing)",                       V["universal_dental_long_run"],    COLORS["neutral_dark"]),
        ("90% bulk-billing GP\nrollout (Strengthening Medicare)",                   V["bulk_billing_90pct"],           COLORS["neutral_dark"]),
        ("Mental health Better Access (indicative)\nexpansion (10→20 sessions)", better_access_aud_bn,              COLORS["neutral_mid"]),
        ("Buffer / hospital top-ups /\nIndigenous health",                          V["buffer_hospital_indigenous"],   COLORS["neutral_mid"]),
    ]
    labels  = [t[0] for t in items]
    costs   = [t[1] for t in items]
    colours = [t[2] for t in items]
    total = sum(costs)

    fig, ax = plt.subplots(figsize=(11, 5.6))
    y = np.arange(len(items))[::-1]
    ax.barh(y, costs, color=colours, edgecolor="white", linewidth=0.6)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=10)
    ax.set_xlabel("Annual cost (A$ billion)")
    ax.set_xlim(0, 18)
    set_chart_title(ax, "A single year of a 25% LNG export tax (A$17 bn) funds ALL of the below — in one year.")

    for yi, c in zip(y, costs):
        ax.text(c + 0.18, yi, f"A${c:.1f} bn", va="center", fontsize=10,
                color=COLORS["ink"], weight="bold")

    ax.axvline(total, color=COLORS["accent"], linestyle="--", linewidth=1.6)
    ax.text(total + 0.18, len(items) - 0.4,
            f"Total = A${total:.1f} bn\nGas tax revenue = A$17.0 bn/yr",
            fontsize=10, color=COLORS["accent"], weight="bold")

    SVG.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / "04_what_17b_buys.png")
    fig.savefig(SVG / "04_what_17b_buys.svg")
    plt.close(fig)
    print("Wrote", OUT / "04_what_17b_buys.png")


if __name__ == "__main__":
    main()
