"""
Know-Your-Data — Shared Plotly Theme & Plotting Utilities.
Defines the Executive Dark Cyber 'kyd' theme applied to every chart in the app.
"""

import plotly.graph_objects as go
import plotly.io as pio

# ──────────────────────────────────────────────
# CYBER COLOR PALETTE
# ──────────────────────────────────────────────

COLORS = [
    "#00F2FE",   # Cyber Cyan
    "#4FACFE",   # Electric Indigo
    "#8B5CF6",   # Neon Violet
    "#10B981",   # Emerald Success
    "#F59E0B",   # Cyber Amber
    "#EF4444",   # Crimson
    "#38BDF8",   # Sky Cyber
    "#A78BFA",   # Light Violet
    "#34D399",   # Neon Mint
    "#F43F5E",   # Neon Rose
    "#06B6D4",   # Electric Teal
    "#FBBF24",   # Neon Gold
    "#818CF8",   # Soft Indigo
    "#EC4899",   # Hot Pink
    "#2DD4BF",   # Aqua
]

GRADIENT_PAIR = ["#00F2FE", "#4FACFE"]

# ──────────────────────────────────────────────
# PLOTLY CHART CONFIG (toolbar settings)
# ──────────────────────────────────────────────

CHART_CONFIG = {
    "displayModeBar": True,
    "modeBarButtonsToRemove": ["lasso2d", "select2d"],
    "displaylogo": False,
    "toImageButtonOptions": {
        "format": "png",
        "filename": "know_your_data_chart",
        "height": 600,
        "width": 1000,
        "scale": 2,
    },
}

# ──────────────────────────────────────────────
# DEFAULT LAYOUT
# ──────────────────────────────────────────────

DEFAULT_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(12,16,26,0.35)",
    font=dict(
        family="Inter, -apple-system, BlinkMacSystemFont, sans-serif",
        color="#F8FAFC",
        size=12,
    ),
    title_font=dict(
        family="Inter, -apple-system, sans-serif",
        size=16,
        color="#00F2FE",
    ),
    xaxis=dict(
        gridcolor="rgba(0,242,254,0.07)",
        zerolinecolor="rgba(0,242,254,0.15)",
        tickfont=dict(
            color="#94A3B8",
            family="JetBrains Mono, monospace",
            size=11,
        ),
        title_font=dict(color="#CBD5E1", size=12),
    ),
    yaxis=dict(
        gridcolor="rgba(0,242,254,0.07)",
        zerolinecolor="rgba(0,242,254,0.15)",
        tickfont=dict(
            color="#94A3B8",
            family="JetBrains Mono, monospace",
            size=11,
        ),
        title_font=dict(color="#CBD5E1", size=12),
    ),
    legend=dict(
        bgcolor="rgba(12,16,26,0.7)",
        bordercolor="rgba(0,242,254,0.2)",
        borderwidth=1,
        font=dict(color="#CBD5E1", size=11),
    ),
    margin=dict(l=50, r=30, t=50, b=40),
    hoverlabel=dict(
        bgcolor="#07090E",
        bordercolor="#00F2FE",
        font=dict(
            color="#F8FAFC",
            family="JetBrains Mono, monospace",
            size=12,
        ),
    ),
    colorway=COLORS,
)


# ──────────────────────────────────────────────
# THEME SETUP
# ──────────────────────────────────────────────

def setup_plotly_theme():
    """Register and activate the 'kyd' Plotly template."""
    kyd_template = go.layout.Template(layout=go.Layout(**DEFAULT_LAYOUT))
    pio.templates["kyd"] = kyd_template
    pio.templates.default = "kyd"


def create_figure(**layout_overrides) -> go.Figure:
    """Create a new go.Figure with KYD theme pre-applied."""
    layout = {**DEFAULT_LAYOUT, **layout_overrides}
    fig = go.Figure()
    fig.update_layout(**layout)
    return fig


def style_figure(fig: go.Figure, **layout_overrides) -> go.Figure:
    """Apply KYD theme to an existing figure (e.g. one from px.*)."""
    layout = {**DEFAULT_LAYOUT, **layout_overrides}
    fig.update_layout(**layout)
    return fig


def get_color(index: int) -> str:
    """Get a color from the palette by index (wraps around)."""
    return COLORS[index % len(COLORS)]


def get_colorscale(name: str = "primary") -> list:
    """
    Return a Plotly-compatible colorscale.
    Options: primary, diverging, sequential, correlation, nulls, heatmap.
    """
    scales = {
        "primary": [
            [0, "#07090E"], [0.25, "#0D1B2A"],
            [0.5, "#00F2FE"], [0.75, "#4FACFE"], [1, "#8B5CF6"],
        ],
        "diverging": [
            [0, "#EF4444"], [0.25, "#F59E0B"],
            [0.5, "#07090E"],
            [0.75, "#00F2FE"], [1, "#4FACFE"],
        ],
        "sequential": [
            [0, "#07090E"], [0.33, "#0E243A"],
            [0.66, "#00F2FE"], [1, "#4FACFE"],
        ],
        "correlation": [
            [0, "#EF4444"], [0.5, "#07090E"], [1, "#00F2FE"],
        ],
        "nulls": [
            [0, "#07090E"], [1, "#EF4444"],
        ],
        "heatmap": [
            [0, "#07090E"], [0.25, "#0C1F38"], [0.5, "#00F2FE"],
            [0.75, "#8B5CF6"], [1, "#EC4899"],
        ],
    }
    return scales.get(name, scales["primary"])


# ──────────────────────────────────────────────
# Initialise on import
# ──────────────────────────────────────────────
setup_plotly_theme()
