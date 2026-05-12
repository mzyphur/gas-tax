"""Template for a single chart in the report.

Each chart lives in its own script in this directory, named NN_<slug>.py
(e.g. 01_prrt_revenue.py). Scripts write a PNG into charts/png/ AND an
SVG into charts/svg/ per public style guide §8.4.

Per public style guide §8.2 / §8.3, neither the chart title nor the source
line is rendered into the PNG — both live in the markdown caption.
`set_chart_title` is a no-op title registry kept here for tooling.

Usage:
    cp _template.py 01_prrt_revenue.py
    # ... fill in DATA and the plotting block ...
    python 01_prrt_revenue.py
"""

from __future__ import annotations

from pathlib import Path
import matplotlib.pyplot as plt

from style import apply_style, COLORS, set_chart_title

apply_style()

OUT = Path(__file__).parent / "png"
SVG = Path(__file__).parent / "svg"
OUT.mkdir(parents=True, exist_ok=True)
SVG.mkdir(parents=True, exist_ok=True)


def main() -> None:
    fig, ax = plt.subplots()

    # === DATA AND PLOT GO HERE ===

    set_chart_title(ax, "Chart title")
    ax.set_xlabel("x axis")
    ax.set_ylabel("y axis")

    # Emit both PNG (raster) and SVG (vector) per public style guide §8.4.
    # Source line lives in the markdown caption (§8.2), not on the PNG.
    fig.savefig(OUT / "00_template.png")
    fig.savefig(SVG / "00_template.svg")
    plt.close(fig)
    print("Wrote", OUT / "00_template.png")


if __name__ == "__main__":
    main()
