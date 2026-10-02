"""
Know-Your-Data — Shared Plotly Theme & Plotting Utilities.
Defines the custom 'kyd' theme applied to every chart in the app.
"""

import plotly.graph_objects as go
import plotly.io as pio

# ──────────────────────────────────────────────
# COLOR PALETTE
# ──────────────────────────────────────────────

COLORS = [
    "#667eea",   # Primary purple-blue
    "#764ba2",   # Secondary purple
    "#00d2ff",   # Cyan accent
    "#00c853",   # Green
    "#ff6d00",   # Orange
    "#ff1744",   # Red
    "#aa00ff",   # Deep purple
    "#2979ff",   # Blue
    "#00e5ff",   # Light cyan
    "#76ff03",   # Light green
    "#f50057",   # Pink
    "#651fff",   # Violet
    "#00b0ff",   # Light blue
    "#ffab00",   # Amber
    "#69f0ae",   # Mint
]

GRADIENT_PAIR = ["#667eea", "#764ba2"]

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
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(
        family="Inter, -apple-system, BlinkMacSystemFont, sans-serif",
        color="#fafafa",
        size=12,
    ),
    title_font=dict(size=16, color="#fafafa"),
    xaxis=dict(
        gridcolor="rgba(255,255,255,0.06)",
        zerolinecolor="rgba(255,255,255,0.1)",
        tickfont=dict(color="#a0aec0"),
        title_font=dict(color="#a0aec0"),
    ),
    yaxis=dict(
        gridcolor="rgba(255,255,255,0.06)",
        zerolinecolor="rgba(255,255,255,0.1)",
        tickfont=dict(color="#a0aec0"),
        title_font=dict(color="#a0aec0"),
    ),
    legend=dict(
        bgcolor="rgba(0,0,0,0)",
        bordercolor="rgba(255,255,255,0.1)",
        font=dict(color="#a0aec0"),
    ),
    margin=dict(l=50, r=30, t=50, b=40),
    hoverlabel=dict(
        bgcolor="#1a1f2e",
        bordercolor="rgba(102,126,234,0.5)",
        font=dict(color="#fafafa", family="Inter, sans-serif"),
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
            [0, "#0e1117"], [0.25, "#1a1f2e"],
            [0.5, "#667eea"], [0.75, "#764ba2"], [1, "#aa00ff"],
        ],
        "diverging": [
            [0, "#ff1744"], [0.25, "#ff6d00"],
            [0.5, "#1a1f2e"],
            [0.75, "#667eea"], [1, "#764ba2"],
        ],
        "sequential": [
            [0, "#0e1117"], [0.33, "#2d3448"],
            [0.66, "#667eea"], [1, "#00d2ff"],
        ],
        "correlation": [
            [0, "#ff1744"], [0.5, "#1a1f2e"], [1, "#667eea"],
        ],
        "nulls": [
            [0, "#1a1f2e"], [1, "#ff1744"],
        ],
        "heatmap": [
            [0, "#0e1117"], [0.2, "#1a1f2e"], [0.4, "#2d3448"],
            [0.6, "#667eea"], [0.8, "#764ba2"], [1, "#ff1744"],
        ],
    }
    return scales.get(name, scales["primary"])


# ──────────────────────────────────────────────
# Initialise on import
# ──────────────────────────────────────────────
setup_plotly_theme()
