"""
Know-Your-Data — Common Helper Functions & Futuristic UI Components.
Formatting utilities, column classification, and interactive cyber-HUD elements.
"""

import pandas as pd
import numpy as np


# ──────────────────────────────────────────────
# NUMBER / STRING FORMATTING
# ──────────────────────────────────────────────

def clean_html(html_str: str) -> str:
    """
    Remove leading/trailing indentation from every line and eliminate empty lines.
    This prevents CommonMark markdown parsers from misinterpreting indented HTML as a code block.
    """
    lines = [line.strip() for line in html_str.strip().split("\n") if line.strip()]
    return "".join(lines)


def format_number(n: float) -> str:
    """Format a number with K / M / B suffixes for compact display."""
    if n is None or (isinstance(n, float) and np.isnan(n)):
        return "N/A"
    if abs(n) >= 1_000_000_000:
        return f"{n / 1_000_000_000:.2f}B"
    elif abs(n) >= 1_000_000:
        return f"{n / 1_000_000:.2f}M"
    elif abs(n) >= 1_000:
        return f"{n / 1_000:.1f}K"
    elif isinstance(n, float):
        return f"{n:,.2f}"
    return f"{n:,}"


def format_percentage(value: float, decimals: int = 1) -> str:
    """Format a float as a percentage string."""
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return "N/A"
    return f"{value:.{decimals}f}%"


def format_bytes(size_bytes: int) -> str:
    """Format bytes into human-readable KB / MB / GB."""
    if size_bytes == 0:
        return "0 B"
    units = ["B", "KB", "MB", "GB", "TB"]
    i = 0
    size = float(size_bytes)
    while size >= 1024 and i < len(units) - 1:
        size /= 1024
        i += 1
    return f"{size:.2f} {units[i]}"


# ──────────────────────────────────────────────
# COLUMN CLASSIFICATION
# ──────────────────────────────────────────────

def classify_column(series: pd.Series) -> str:
    """Classify a pandas Series into a semantic type category."""
    if pd.api.types.is_bool_dtype(series):
        return "Boolean"
    elif pd.api.types.is_numeric_dtype(series):
        if pd.api.types.is_integer_dtype(series):
            return "Integer"
        return "Float"
    elif pd.api.types.is_datetime64_any_dtype(series):
        return "Datetime"
    elif isinstance(series.dtype, pd.CategoricalDtype):
        return "Categorical"
    else:
        if series.dropna().empty:
            return "Empty"
        # Probe for potential datetime
        sample = series.dropna().head(50)
        try:
            pd.to_datetime(sample, format="mixed")
            return "Potential Datetime"
        except Exception:
            pass
        # Low-cardinality string → categorical
        nunique = series.nunique()
        total = len(series)
        if total > 0 and (nunique / total < 0.05 or nunique <= 20):
            return "Categorical"
        return "Text"


def get_numeric_columns(df: pd.DataFrame) -> list:
    """Return list of numeric column names."""
    return df.select_dtypes(include=[np.number]).columns.tolist()


def get_categorical_columns(df: pd.DataFrame) -> list:
    """Return list of object / categorical column names."""
    return df.select_dtypes(include=["object", "category", "bool"]).columns.tolist()


def get_datetime_columns(df: pd.DataFrame) -> list:
    """Return list of datetime column names."""
    return df.select_dtypes(include=["datetime64", "datetimetz"]).columns.tolist()


def get_column_icon(dtype_str: str) -> str:
    """Return an emoji icon for a given dtype category."""
    icons = {
        "Integer": "🔢",
        "Float": "🔢",
        "Boolean": "☑️",
        "Datetime": "📅",
        "Categorical": "🏷️",
        "Text": "📝",
        "Potential Datetime": "📅",
        "Empty": "⬜",
    }
    return icons.get(dtype_str, "📄")


# ──────────────────────────────────────────────
# REUSABLE HTML / CYBER COMPONENTS
# ──────────────────────────────────────────────

def metric_card_html(icon: str, value: str, label: str, stagger: int = 1, delta: str = None) -> str:
    """Return HTML for a 3D perspective cyber metric card with HUD badge."""
    delta_html = f'<span class="metric-delta-tag">{delta}</span>' if delta else ""
    return clean_html(f"""
    <div class="metric-card stagger-{stagger}">
        <div class="metric-header-row">
            <div class="metric-icon-badge">{icon}</div>
            {delta_html}
        </div>
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
    </div>
    """)


def progress_bar_html(percentage: float, color: str = None) -> str:
    """Return HTML for an animated cyber progress bar with light shimmer."""
    _color_map = {
        "error": "var(--crimson-error)",
        "warning": "var(--amber-warning)",
        "success": "var(--emerald-success)",
        "primary": "var(--cyber-cyan)",
        "accent": "var(--electric-indigo)",
        "info": "var(--cyber-cyan)",
    }
    if color is None:
        if percentage > 50:
            color = "var(--crimson-error)"
        elif percentage > 20:
            color = "var(--amber-warning)"
        elif percentage > 5:
            color = "var(--cyber-cyan)"
        else:
            color = "var(--emerald-success)"
    else:
        color = _color_map.get(color, color)

    pct = max(0, min(percentage, 100))
    return clean_html(f"""
    <div class="progress-bar-container">
        <div class="progress-bar-fill" style="width: {pct}%; background: {color};"></div>
    </div>
    """)


def badge_html(text: str, value: str = None, badge_type: str = "info") -> str:
    """Return HTML for a styled cyber badge. Optionally show 'text: value' format."""
    if value is not None:
        return f'<span class="badge badge-{badge_type}">{text}: {value}</span>'
    return f'<span class="badge badge-{badge_type}">{text}</span>'


def section_header_html(title: str, subtitle: str = "") -> str:
    """Return HTML for a section header with cyber gradient text and HUD subtitle."""
    sub_html = f'<div class="section-subheader">// {subtitle}</div>' if subtitle else ""
    return clean_html(f"""
    <div class="section-header">
        <span>{title}</span>
    </div>
    {sub_html}
    """)


def divider_html() -> str:
    """Return HTML for a luminous cyber gradient divider."""
    return '<div class="gradient-divider"></div>'


def info_box_html(text: str) -> str:
    """Return HTML for a cyber-cyan info callout box."""
    return f'<div class="info-box"><p>{text}</p></div>'


def warning_box_html(text: str) -> str:
    """Return HTML for an amber warning callout box."""
    return f'<div class="warning-box"><p>{text}</p></div>'


def success_box_html(text: str) -> str:
    """Return HTML for an emerald success callout box."""
    return f'<div class="success-box"><p>{text}</p></div>'


def glass_container_start() -> str:
    """Return opening tag for a frosted glass container."""
    return '<div class="glass-container">'


def glass_container_end() -> str:
    """Return closing tag for a frosted glass container."""
    return '</div>'


def skeleton_loader_html(cards_count: int = 4) -> str:
    """Return HTML for glowing skeleton loaders with gradient light sweeps."""
    cols_html = "".join(
        f'<div style="flex: 1; min-width: 180px;"><div class="skeleton-metric"></div></div>'
        for _ in range(cards_count)
    )
    return clean_html(f"""
    <div style="display: flex; gap: 16px; margin: 16px 0; width: 100%;">
        {cols_html}
    </div>
    """)


def neural_core_html(progress_pct: int = 85, phase_title: str = "NEURAL ANALYSIS IN PROGRESS") -> str:
    """Return HTML for the mesmerizing Neural Core animation with concentric spinning vector rings."""
    return clean_html(f"""
    <div class="neural-core-wrapper">
        <div class="neural-rings-container">
            <div class="neural-ring-outer"></div>
            <div class="neural-ring-middle"></div>
            <div class="neural-ring-inner"></div>
            <div class="neural-core-center"></div>
        </div>
        <div class="hero-hud-pill">
            <div class="hero-hud-dot"></div>
            <span>{phase_title} · {progress_pct}%</span>
        </div>
    </div>
    """)


def terminal_log_box_html(logs: list = None) -> str:
    """Return HTML for the hacker/analyst real-time terminal telemetry log box."""
    if logs is None:
        logs = [
            ("10:42:01.012", "INIT", "Neural EDA Core initialized on runtime thread"),
            ("10:42:01.124", "STREAM", "Binary stream ingestion buffer: 1,000 records allocated"),
            ("10:42:01.350", "SCHEMA", "Column taxonomy mapped: 12 features, 0 null pointers"),
            ("10:42:01.780", "MATRIX", "Spearman rank correlation tensor computed (12x12)"),
            ("10:42:02.105", "ANOMALY", "Multivariate density estimation & IQR outlier bounds locked"),
            ("10:42:02.410", "READY", "Telemetry compiled · Interactive HUD active"),
        ]

    lines_html = ""
    for timestamp, tag, message in logs:
        lines_html += f"""
        <div class="terminal-line">
            <span class="terminal-time">[{timestamp}]</span>
            <span class="terminal-tag">[{tag}]</span>
            <span>{message}</span>
        </div>
        """

    return clean_html(f"""
    <div class="terminal-box">
        <div class="terminal-header">
            <div class="terminal-dots">
                <div class="terminal-dot red"></div>
                <div class="terminal-dot yellow"></div>
                <div class="terminal-dot green"></div>
            </div>
            <div class="terminal-title">KYD-OS // TELEMETRY TERMINAL &bull; ACTIVE</div>
            <div style="font-family: var(--font-mono); font-size: 0.68rem; color: #10B981;">ONLINE &bull; 60 FPS</div>
        </div>
        <div class="terminal-body">
            {lines_html}
            <div class="terminal-line" style="margin-top: 8px;">
                <span style="color: #64748B;">root@kyd-core:~#</span>
                <span class="cursor-blink"></span>
            </div>
        </div>
    </div>
    """)
