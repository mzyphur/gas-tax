"""Chart 01: PRRT cash receipts FY2010-11 → FY2028-29.

Headline: PRRT did not rise with the LNG boom. The 2022-23 spike was
an oil-price event, not a structural lift.

Data: FY2010-11 to FY2024-25 from Treasury Final Budget Outcomes
(sourced via dossier 01_prrt_history.md).  FY2025-26 → FY2028-29 are
forward estimates from Budget Paper 1 2025-26, Table 4.7.
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
OUT.mkdir(exist_ok=True)


def main() -> None:
    H = load_values()["prrt_history_cash_receipts_aud_million"]
    fy = list(H["by_fy"].keys())
    receipts = [H["by_fy"][k] for k in fy]
    # Forecast bars are everything from last_outcome_fy + 1 onwards.
    last_outcome = H["last_outcome_fy"]
    last_outcome_idx = fy.index(last_outcome)
    is_forecast = [i > last_outcome_idx for i in range(len(fy))]
    # Accent red reserved for the single emphasised bar (FY24-25 outcome
    # — the "below forecast" data point the chart's annotation calls out)
    # per public style guide §13. Historical bars use primary; forecast bars
    # use neutral mid grey.
    EMPHASIS_IDX = last_outcome_idx

    fig, ax = plt.subplots(figsize=(11, 5.6))
    x = np.arange(len(fy))
    colours = []
    for i, f in enumerate(is_forecast):
        if i == EMPHASIS_IDX:
            colours.append(COLORS["accent"])
        elif f:
            colours.append(COLORS["neutral_mid"])
        else:
            colours.append(COLORS["primary"])
    ax.bar(x, receipts, color=colours, width=0.78, edgecolor="white", linewidth=0.4)

    ax.set_xticks(x)
    ax.set_xticklabels(fy, fontsize=9)
    ax.set_ylabel("PRRT cash receipts (A$ million)")
    ax.set_ylim(0, 2600)
    set_chart_title(ax, "PRRT cash receipts did not rise with the LNG boom")

    ax.axvspan(14.5, 18.5, color=COLORS["neutral_mid"], alpha=0.08, zorder=0)
    ax.text(16.5, 2450, "Forward estimates\n(Budget 2025-26 BP1)",
            ha="center", va="top", fontsize=9, color=COLORS["ink_soft"],
            style="italic")

    ax.annotate(
        "2022-23 spike was an\noil-price event, not a\nstructural lift",
        xy=(12, 2287), xytext=(8.2, 2400),
        arrowprops={"arrowstyle": "-", "lw": 0.6, "color": COLORS["ink"]},
        fontsize=9, color=COLORS["ink"], ha="left",
    )
    last_v_bn = receipts[last_outcome_idx] / 1000
    below_fc  = H["last_outcome_below_forecast_aud_bn"]
    may_fc    = H["may2024_budget_forecast_for_2425_aud_bn"]
    ax.annotate(
        f"FY{last_outcome} outcome: A${last_v_bn:.2f} bn —\n"
        f"A${below_fc:.2f} bn BELOW May 2024\n"
        f"Budget forecast of A${may_fc:.2f} bn",
        xy=(last_outcome_idx, receipts[last_outcome_idx]),
        xytext=(last_outcome_idx - 0.5, 2300),
        arrowprops={"arrowstyle": "-", "lw": 0.6, "color": COLORS["ink"]},
        fontsize=9, color=COLORS["ink"], ha="left", va="top",
    )

    SVG.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUT / "01_prrt_revenue_history.png")
    fig.savefig(SVG / "01_prrt_revenue_history.svg")
    plt.close(fig)
    print("Wrote", OUT / "01_prrt_revenue_history.png")


if __name__ == "__main__":
    main()
