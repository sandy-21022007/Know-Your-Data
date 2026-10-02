"""
Know-Your-Data — Common Helper Functions.
Formatting utilities, column classification, and reusable HTML components.
"""

import pandas as pd
import numpy as np


# ──────────────────────────────────────────────
# NUMBER / STRING FORMATTING
# ──────────────────────────────────────────────

def format_number(n: float) -> str:
    """Format a number with K / M / B suffixes for compact display."""
    if n is None or (isinstance(n, float) and np.isnan(n)):
        return "N/A"
    if abs(n) >= 1_000_000_000:
        return f"{n / 1_000_000_000:.1f}B"
    elif abs(n) >= 1_000_000:
        return f"{n / 1_000_000:.1f}M"
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
            pd.to_datetime(sample, infer_datetime_format=True)
            return "Potential Datetime"
        except (ValueError, TypeError):
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
# REUSABLE HTML COMPONENTS
# ──────────────────────────────────────────────

def metric_card_html(icon: str, value: str, label: str, stagger: int = 1) -> str:
    """Return HTML for an animated metric card."""
    return f"""
    <div class="metric-card stagger-{stagger}">
        <div class="metric-icon">{icon}</div>
        <div class="metric-value">{value}</div>
        <div class="metric-label">{label}</div>
    </div>
    """


def progress_bar_html(percentage: float, color: str = None) -> str:
    """Return HTML for an animated progress bar."""
    _color_map = {
        "error": "var(--error)",
        "warning": "var(--warning)",
        "success": "var(--success)",
        "primary": "var(--primary)",
        "accent": "var(--accent)",
        "info": "var(--primary)",
    }
    if color is None:
        if percentage > 50:
            color = "var(--error)"
        elif percentage > 20:
            color = "var(--warning)"
        elif percentage > 5:
            color = "var(--primary)"
        else:
            color = "var(--success)"
    else:
        color = _color_map.get(color, color)
    return f"""
    <div class="progress-bar-container">
        <div class="progress-bar-fill" style="width: {min(percentage, 100)}%; background: {color};"></div>
    </div>
    """


def badge_html(text: str, value: str = None, badge_type: str = "info") -> str:
    """Return HTML for a styled badge. Optionally show 'text: value' format."""
    if value is not None:
        return f'<span class="badge badge-{badge_type}">{text}: {value}</span>'
    return f'<span class="badge badge-{badge_type}">{text}</span>'


def section_header_html(title: str, subtitle: str = "") -> str:
    """Return HTML for a section header with gradient text."""
    html = f'<div class="section-header">{title}</div>'
    if subtitle:
        html += f'<div class="section-subheader">{subtitle}</div>'
    return html


def divider_html() -> str:
    """Return HTML for a gradient divider."""
    return '<div class="gradient-divider"></div>'


def info_box_html(text: str) -> str:
    """Return HTML for an info callout box."""
    return f'<div class="info-box"><p>{text}</p></div>'


def warning_box_html(text: str) -> str:
    """Return HTML for a warning callout box."""
    return f'<div class="warning-box"><p>{text}</p></div>'


def success_box_html(text: str) -> str:
    """Return HTML for a success callout box."""
    return f'<div class="success-box"><p>{text}</p></div>'


def glass_container_start() -> str:
    """Return opening tag for a glass-morphism container."""
    return '<div class="glass-container">'


def glass_container_end() -> str:
    """Return closing tag for a glass-morphism container."""
    return '</div>'
