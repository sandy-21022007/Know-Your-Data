"""
Know-Your-Data — Shared Plotly Theme & Plotting Utilities.
Defines the Enterprise Data Lab 'kyd' chart theme (dark, with light counterpart).
"""

import plotly.graph_objects as go
import plotly.io as pio

# ──────────────────────────────────────────────
# ENTERPRISE ACCENT PALETTE
# ──────────────────────────────────────────────

COLORS = [
    "#38BDF8",   # Sky blue
    "#6366F1",   # Indigo
    "#8B5CF6",   # Violet
    "#06B6D4",   # Cyan
    "#14B8A6",   # Teal
    "#818CF8",   # Soft indigo
    "#22C55E",   # Success green
    "#F59E0B",   # Warning amber
    "#EF4444",   # Error red
    "#A78BFA",   # Light violet
    "#2DD4BF",   # Aqua
    "#0EA5E9",   # Blue
    "#94A3B8",   # Slate
    "#F472B6",   # Rose
    "#FBBF24",   # Gold
]

GRADIENT_PAIR = ["#6366F1", "#38BDF8"]

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
# DEFAULT (DARK) LAYOUT
# ──────────────────────────────────────────────

DEFAULT_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(
        family="Inter, -apple-system, BlinkMacSystemFont, sans-serif",
        color="#E2E8F0",
        size=12,
    ),
    title_font=dict(
        family="Inter, -apple-system, sans-serif",
        size=15,
        color="#E2E8F0",
    ),
    xaxis=dict(
        gridcolor="rgba(38,50,68,0.9)",
        zerolinecolor="rgba(38,50,68,0.9)",
        linecolor="#263244",
        tickfont=dict(
            color="#94A3B8",
            family="JetBrains Mono, monospace",
            size=11,
        ),
        title_font=dict(color="#94A3B8", size=12),
    ),
    yaxis=dict(
        gridcolor="rgba(38,50,68,0.9)",
        zerolinecolor="rgba(38,50,68,0.9)",
        linecolor="#263244",
        tickfont=dict(
            color="#94A3B8",
            family="JetBrains Mono, monospace",
            size=11,
        ),
        title_font=dict(color="#94A3B8", size=12),
    ),
    legend=dict(
        bgcolor="rgba(21,29,44,0.92)",
        bordercolor="#263244",
        borderwidth=1,
        font=dict(color="#94A3B8", size=11),
    ),
    margin=dict(l=50, r=30, t=50, b=40),
    hoverlabel=dict(
        bgcolor="#1B2638",
        bordercolor="#283448",
        font=dict(
            color="#F1F5F9",
            family="JetBrains Mono, monospace",
            size=12,
        ),
    ),
    colorway=COLORS,
)

# ──────────────────────────────────────────────
# LIGHT LAYOUT
# ──────────────────────────────────────────────

LIGHT_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="#FFFFFF",
    font=dict(
        family="Inter, -apple-system, BlinkMacSystemFont, sans-serif",
        color="#17243A",
        size=12,
    ),
    title_font=dict(
        family="Inter, -apple-system, sans-serif",
        size=15,
        color="#17243A",
    ),
    xaxis=dict(
        gridcolor="rgba(100,116,139,0.18)",
        zerolinecolor="rgba(100,116,139,0.30)",
        linecolor="#E2E8F0",
        tickfont=dict(
            color="#64748B",
            family="JetBrains Mono, monospace",
            size=11,
        ),
        title_font=dict(color="#475569", size=12),
    ),
    yaxis=dict(
        gridcolor="rgba(100,116,139,0.18)",
        zerolinecolor="rgba(100,116,139,0.30)",
        linecolor="#E2E8F0",
        tickfont=dict(
            color="#64748B",
            family="JetBrains Mono, monospace",
            size=11,
        ),
        title_font=dict(color="#475569", size=12),
    ),
    legend=dict(
        bgcolor="rgba(255,255,255,0.96)",
        bordercolor="#E2E8F0",
        borderwidth=1,
        font=dict(color="#475569", size=11),
    ),
    margin=dict(l=50, r=30, t=50, b=40),
    hoverlabel=dict(
        bgcolor="#FFFFFF",
        bordercolor="#CBD5E1",
        font=dict(
            color="#17243A",
            family="JetBrains Mono, monospace",
            size=12,
        ),
    ),
    colorway=COLORS,
)

# Active styling state (populated by setup_plotly_theme).
_ACTIVE_THEME = "dark"
_ACTIVE_LAYOUT = DEFAULT_LAYOUT


def _active_theme() -> str:
    """Return the active Streamlit theme type ('dark' or 'light'), defaulting to dark."""
    try:
        import streamlit as st

        theme = getattr(st.context, "theme", None)
        theme_type = getattr(theme, "type", None)
        if theme_type is None and isinstance(theme, dict):
            theme_type = theme.get("type")
        if str(theme_type).strip().lower() == "light":
            return "light"
    except Exception:
        pass
    return "dark"


# ──────────────────────────────────────────────
# THEME SETUP
# ──────────────────────────────────────────────

def setup_plotly_theme(theme: str = None):
    """Register and activate the 'kyd' Plotly template for the requested theme."""
    global _ACTIVE_THEME, _ACTIVE_LAYOUT

    if theme is None:
        theme = _active_theme()
    _ACTIVE_THEME = "light" if str(theme).strip().lower() == "light" else "dark"
    _ACTIVE_LAYOUT = LIGHT_LAYOUT if _ACTIVE_THEME == "light" else DEFAULT_LAYOUT

    kyd_template = go.layout.Template(layout=go.Layout(**_ACTIVE_LAYOUT))
    pio.templates["kyd"] = kyd_template
    pio.templates.default = "kyd"


def create_figure(**layout_overrides) -> go.Figure:
    """Create a new go.Figure with KYD theme pre-applied."""
    layout = {**_ACTIVE_LAYOUT, **layout_overrides}
    fig = go.Figure()
    fig.update_layout(**layout)
    return fig


def style_figure(fig: go.Figure, **layout_overrides) -> go.Figure:
    """Apply KYD theme to an existing figure (e.g. one from px.*)."""
    layout = {**_ACTIVE_LAYOUT, **layout_overrides}
    fig.update_layout(**layout)
    return fig


def get_color(index: int) -> str:
    """Get a color from the palette by index (wraps around)."""
    return COLORS[index % len(COLORS)]


def get_colorscale(name: str = "primary") -> list:
    """
    Return a Plotly-compatible colorscale for the active theme.
    Options: primary, diverging, sequential, correlation, nulls, heatmap.
    """
    if _ACTIVE_THEME == "light":
        scales = {
            "primary": [
                [0, "#F8FAFC"], [0.25, "#E0E7FF"],
                [0.5, "#4F46E5"], [0.75, "#0891B2"], [1, "#7C3AED"],
            ],
            "diverging": [
                [0, "#DC2626"], [0.25, "#D97706"],
                [0.5, "#F8FAFC"],
                [0.75, "#4F46E5"], [1, "#0891B2"],
            ],
            "sequential": [
                [0, "#F8FAFC"], [0.33, "#E0E7FF"],
                [0.66, "#4F46E5"], [1, "#0891B2"],
            ],
            "correlation": [
                [0, "#DC2626"], [0.5, "#F8FAFC"], [1, "#4F46E5"],
            ],
            "nulls": [
                [0, "#F8FAFC"], [1, "#DC2626"],
            ],
            "heatmap": [
                [0, "#F8FAFC"], [0.25, "#E0E7FF"], [0.5, "#4F46E5"],
                [0.75, "#0891B2"], [1, "#7C3AED"],
            ],
        }
    else:
        scales = {
            "primary": [
                [0, "#0B0F19"], [0.25, "#1B2638"],
                [0.5, "#6366F1"], [0.75, "#38BDF8"], [1, "#06B6D4"],
            ],
            "diverging": [
                [0, "#EF4444"], [0.25, "#F59E0B"],
                [0.5, "#111827"],
                [0.75, "#38BDF8"], [1, "#6366F1"],
            ],
            "sequential": [
                [0, "#0B0F19"], [0.33, "#1B2638"],
                [0.66, "#6366F1"], [1, "#38BDF8"],
            ],
            "correlation": [
                [0, "#EF4444"], [0.5, "#111827"], [1, "#38BDF8"],
            ],
            "nulls": [
                [0, "#151D2C"], [1, "#38BDF8"],
            ],
            "heatmap": [
                [0, "#0B0F19"], [0.25, "#1B2638"], [0.5, "#6366F1"],
                [0.75, "#8B5CF6"], [1, "#06B6D4"],
            ],
        }
    return scales.get(name, scales["primary"])


# ──────────────────────────────────────────────
# Initialise on import
# ──────────────────────────────────────────────
setup_plotly_theme()
