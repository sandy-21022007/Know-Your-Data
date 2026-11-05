"""
Know-Your-Data — Shared Plotly Theme & Plotting Utilities.
Defines the Executive Dark Cyber 'kyd' theme applied to every chart in the app.
"""

import plotly.graph_objects as go
import plotly.io as pio

# ──────────────────────────────────────────────
# PROFESSIONAL COLOR PALETTE
# ──────────────────────────────────────────────

COLORS = [
    "#6366F1",   # Primary Indigo
    "#06B6D4",   # Secondary Cyan
    "#8B5CF6",   # Violet
    "#22C55E",   # Success Green
    "#F59E0B",   # Warning Amber
    "#EF4444",   # Error Red
    "#3B82F6",   # Blue
    "#A78BFA",   # Light Violet
    "#34D399",   # Mint
    "#F43F5E",   # Rose
    "#0891B2",   # Teal
    "#FBBF24",   # Gold
    "#818CF8",   # Soft Indigo
    "#EC4899",   # Pink
    "#14B8A6",   # Aqua
]

GRADIENT_PAIR = ["#6366F1", "#06B6D4"]

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
    plot_bgcolor="rgba(17,24,39,0.35)",
    font=dict(
        family="Inter, -apple-system, BlinkMacSystemFont, sans-serif",
        color="#F1F5F9",
        size=12,
    ),
    title_font=dict(
        family="Inter, -apple-system, sans-serif",
        size=16,
        color="#6366F1",
    ),
    xaxis=dict(
        gridcolor="rgba(99,102,241,0.07)",
        zerolinecolor="rgba(99,102,241,0.15)",
        tickfont=dict(
            color="#94A3B8",
            family="JetBrains Mono, monospace",
            size=11,
        ),
        title_font=dict(color="#CBD5E1", size=12),
    ),
    yaxis=dict(
        gridcolor="rgba(99,102,241,0.07)",
        zerolinecolor="rgba(99,102,241,0.15)",
        tickfont=dict(
            color="#94A3B8",
            family="JetBrains Mono, monospace",
            size=11,
        ),
        title_font=dict(color="#CBD5E1", size=12),
    ),
    legend=dict(
        bgcolor="rgba(17,24,39,0.7)",
        bordercolor="rgba(99,102,241,0.2)",
        borderwidth=1,
        font=dict(color="#CBD5E1", size=11),
    ),
    margin=dict(l=50, r=30, t=50, b=40),
    hoverlabel=dict(
        bgcolor="#0B1120",
        bordercolor="#6366F1",
        font=dict(
            color="#F1F5F9",
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
            [0, "#0B1120"], [0.25, "#111827"],
            [0.5, "#6366F1"], [0.75, "#06B6D4"], [1, "#8B5CF6"],
        ],
        "diverging": [
            [0, "#EF4444"], [0.25, "#F59E0B"],
            [0.5, "#0B1120"],
            [0.75, "#6366F1"], [1, "#06B6D4"],
        ],
        "sequential": [
            [0, "#0B1120"], [0.33, "#1C293B"],
            [0.66, "#6366F1"], [1, "#06B6D4"],
        ],
        "correlation": [
            [0, "#EF4444"], [0.5, "#0B1120"], [1, "#6366F1"],
        ],
        "nulls": [
            [0, "#0B1120"], [1, "#EF4444"],
        ],
        "heatmap": [
            [0, "#0B1120"], [0.25, "#151F30"], [0.5, "#6366F1"],
            [0.75, "#8B5CF6"], [1, "#EC4899"],
        ],
    }
    return scales.get(name, scales["primary"])


# ──────────────────────────────────────────────
# Initialise on import
# ──────────────────────────────────────────────
setup_plotly_theme()
