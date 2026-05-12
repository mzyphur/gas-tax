"""Shared chart style for Instats policy documents.

Hard-codes public style guide §8.1 and §8.4 — the matplotlib stylesheet
the design team agreed on, in the order it appears in the spec:

  font.family       Inter (with Helvetica Neue / Arial Narrow fallbacks)
                    Note: public style guide §3.1 codifies Inter as the
                    chart-annotation typeface; this differs from the
                    HTML body which uses Source Serif 4. Charts use the
                    metadata family because axis labels / annotations
                    are small-size metadata, not body prose.
  font.size         10
  axes.titlesize    14
  axes.titleweight  600
  axes.spines.top   False
  axes.spines.right False
  axes.edgecolor    #525560 (ink-soft)
  axes.grid         True (y-axis only)
  grid.color        #E8E7E6 (rule-soft)
  grid.linewidth    0.5
  xtick.direction   out
  ytick.direction   out
  xtick.major.size  3
  ytick.major.size  0
  legend.frameon    False
  figure.facecolor  white
  savefig.dpi       300

Chart titles are NOT rendered in the PNG (§8.3) — they live in the
in-document caption frame. Use `set_chart_title(ax, text)` instead
of `ax.set_title(text)`; the helper stores the title in CHART_TITLES
for any tooling that wants to enumerate them but does not draw on
the figure.

Source lines are NOT rendered in the PNG (§8.2) — the markdown
caption supplies them. The legacy `add_footer()` is kept as a no-op
shim for backwards compatibility with chart scripts that still call
it; remove the calls when each script is touched next.
"""

from __future__ import annotations

import matplotlib as mpl
import matplotlib.pyplot as plt


# public style guide §8.1 — strict 5-colour policy palette.
# Use these in order, never substituted. Greys are for non-focal data.
COLORS = {
    # Primary policy-doc palette
    "primary":       "#00547B",  # Instats primary  (deep teal-navy)
    "secondary":     "#3092B1",  # Instats secondary (mid teal)
    "neutral_dark":  "#525560",  # neutral dark grey
    "neutral_mid":   "#A8AAB1",  # neutral mid grey
    "accent":        "#C5283D",  # emphasis only — one element per chart

    # Page chrome / text colour tokens
    "ink":           "#1F2024",  # body / annotations
    "ink_soft":      "#525560",  # axis labels, captions, source lines
    "ink_faint":     "#8E8F94",  # page numbers, fine print
    "rule":          "#D5D5D7",
    "rule_soft":     "#E8E7E6",  # chart gridlines
    "paper":         "#FFFFFF",
    "paper_tint":    "#F5F5F7",
}


# Title-text registry. Populated by set_chart_title() for any tooling
# that wants to enumerate chart titles (e.g. caption auto-population).
CHART_TITLES: dict[str, str] = {}


def apply_style() -> None:
    """Apply the Instats chart style globally — public style guide §8.4."""
    mpl.rcParams.update({
        # Layout
        "figure.figsize":       (10, 5.5),
        "figure.dpi":           140,
        "savefig.dpi":          300,           # §8.4: 300dpi for print
        "savefig.bbox":         "tight",
        "savefig.facecolor":    COLORS["paper"],
        "figure.facecolor":     COLORS["paper"],
        "axes.facecolor":       COLORS["paper"],

        # Spines — no top or right per §8.1
        "axes.spines.top":      False,
        "axes.spines.right":    False,
        "axes.edgecolor":       COLORS["ink_soft"],
        "axes.linewidth":       1.0,

        # Grid — y-axis only, 0.5px in rule-soft per §8.1
        "axes.grid":            True,
        "axes.grid.axis":       "y",
        "grid.color":           COLORS["rule_soft"],
        "grid.linewidth":       0.5,

        # Title — kept stylable for any chart that still calls
        # ax.set_title, but the convention is to put titles in the
        # markdown caption (§8.3). 14pt Montserrat 600.
        "axes.titleweight":     "semibold",
        "axes.titlesize":       14,
        "axes.titlepad":        16,
        "axes.titlecolor":      COLORS["ink"],

        # Axis labels — Montserrat 500, 10pt, ink-soft per §8.1
        "axes.labelsize":       10,
        "axes.labelweight":     "medium",
        "axes.labelcolor":      COLORS["ink_soft"],

        # Tick labels — Inter 400, 9pt, ink-soft per §8.1
        # (matplotlib uses font.family globally, so we set it here to
        # the metadata stack; chart axis labels are also Montserrat
        # via font.family[0], so axis labels and ticks share the font
        # family — the size + weight differentiation does the work.)
        "xtick.labelsize":      9,
        "ytick.labelsize":      9,
        "xtick.color":          COLORS["ink_soft"],
        "ytick.color":          COLORS["ink_soft"],

        # Tick marks — 3px outside on x, none on y (§8.4)
        "xtick.direction":      "out",
        "ytick.direction":      "out",
        "xtick.major.size":     3,
        "ytick.major.size":     0,
        "xtick.minor.visible":  False,
        "ytick.minor.visible":  False,

        # Legend — no frame, no fill per §8.1
        "legend.fontsize":      10,
        "legend.frameon":       False,
        "legend.borderaxespad": 0,

        # Typography — Inter first for annotations and tick labels per
        # public style guide §3.1 (metadata family). Display sans
        # (Montserrat) follows so axis labels rendered via the chart's
        # own font-family override still resolve correctly. The change
        # finding — every chart was previously rendering all annotation
        # text in DejaVu Sans (the matplotlib system default) when
        # Montserrat wasn't available on the build machine. Inter is
        # with macOS Sonoma+, Windows 11 with the optional WebUI font
        # pack, and most Linux distros via fonts-inter) and the
        # fallback chain after Inter is the spec metadata stack.
        "font.family":          ["Inter", "Helvetica Neue",
                                 "Helvetica", "Arial", "DejaVu Sans"],
        "font.size":            10,
        "font.weight":          "regular",

        # PDF/PS — embed TrueType for high-quality vector export
        "pdf.fonttype":         42,
        "ps.fonttype":          42,
        "svg.fonttype":         "none",
        "text.parse_math":      False,
    })


def set_chart_title(ax, text: str) -> None:
    """Register a chart title without drawing it on the figure.

    Chart titles belong in the markdown caption frame, not in the PNG
    (public style guide §8.3). Use this in chart scripts in place of
    ax.set_title(text); the title text is stored in CHART_TITLES under
    a key derived from the calling script's basename so any tooling
    that wants to surface it can.
    """
    import inspect
    import os
    frame = inspect.stack()[1]
    key = os.path.basename(frame.filename).replace(".py", "")
    CHART_TITLES[key] = text
    # Intentionally do NOT call ax.set_title(text). The chart PNG must
    # be reusable across the Word doc, the HTML edition, the GitHub
    # README, and any future re-typesetting — title text in-PNG would
    # have to be re-rendered on every restyle.


def aud(n: float, decimals: int = 1) -> str:
    """Format a number as AUD, picking sensible units."""
    if abs(n) >= 1e9:
        return f"A${n/1e9:.{decimals}f}b"
    if abs(n) >= 1e6:
        return f"A${n/1e6:.{decimals}f}m"
    if abs(n) >= 1e3:
        return f"A${n/1e3:.{decimals}f}k"
    return f"A${n:.{decimals}f}"
