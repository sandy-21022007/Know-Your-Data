"""
Know-Your-Data — Enterprise Data Lab Theme.
Dark-first enterprise analytics styling with an equivalent light palette.
This module is presentation-only: it injects design tokens and CSS chrome.
"""

import streamlit as st


def _active_theme() -> str:
    """Return the active Streamlit theme type ('dark' or 'light'), defaulting to dark."""
    try:
        theme = getattr(st.context, "theme", None)
        theme_type = getattr(theme, "type", None)
        if theme_type is None and isinstance(theme, dict):
            theme_type = theme.get("type")
        if str(theme_type).strip().lower() == "light":
            return "light"
    except Exception:
        pass
    return "dark"


def inject_custom_css(theme: str = None):
    """Inject the theme CSS for the requested theme ('dark' or 'light')."""
    if theme is None:
        theme = _active_theme()
    palette = LIGHT_PALETTE if str(theme).strip().lower() == "light" else DARK_PALETTE
    st.markdown(BASE_CSS.replace("__PALETTE__", palette), unsafe_allow_html=True)


# ==================== DESIGN TOKENS ====================

DARK_PALETTE = """
    :root {
        /* Surfaces */
        --bg-void: #0B0F19;
        --bg-darker: #0B0F19;
        --bg-sidebar: #0E1421;
        --bg-secondary: #111827;
        --bg-surface: #151D2C;
        --bg-surface-card: #151D2C;
        --bg-surface-elevated: #1B2638;
        --bg-glass-heavy: rgba(11, 15, 25, 0.95);
        --bg-input: #111827;
        --bg-hover: rgba(99, 102, 241, 0.10);
        --bg-row-hover: rgba(99, 102, 241, 0.06);
        --bg-table-header: #1B2638;
        --surface-tint: rgba(99, 102, 241, 0.10);
        --btn-secondary-bg: #1B2638;
        --btn-secondary-hover: rgba(99, 102, 241, 0.18);
        --page-wash:
            radial-gradient(1100px 520px at 80% -10%, rgba(99, 102, 241, 0.10), transparent 60%),
            radial-gradient(900px 480px at 8% -12%, rgba(56, 189, 248, 0.06), transparent 60%);

        /* Typography */
        --text-primary: #F1F5F9;
        --text-secondary: #94A3B8;
        --text-muted: #718096;
        --text-disabled: #64748B;

        /* Accents */
        --primary: #6366F1;
        --primary-dark: #4F46E5;
        --secondary: #38BDF8;
        --accent: #8B5CF6;
        --highlight: #06B6D4;
        --success: #22C55E;
        --warning: #F59E0B;
        --error: #EF4444;

        /* Backward-compatible aliases (used by HTML component helpers) */
        --cyber-cyan: #6366F1;
        --electric-indigo: #38BDF8;
        --neon-violet: #8B5CF6;
        --emerald-success: #22C55E;
        --amber-warning: #F59E0B;
        --crimson-error: #EF4444;

        /* Borders */
        --border: #263244;
        --border-glass: #263244;
        --border-subtle: rgba(38, 50, 68, 0.70);
        --border-luminous: rgba(99, 102, 241, 0.45);

        /* Accent tints */
        --accent-soft: rgba(99, 102, 241, 0.12);
        --accent-soft-strong: rgba(99, 102, 241, 0.18);
        --accent-line: linear-gradient(90deg, #6366F1 0%, #38BDF8 100%);
        --gradient-cyber: linear-gradient(135deg, #6366F1 0%, #38BDF8 100%);
        --gradient-neural: linear-gradient(135deg, #6366F1 0%, #8B5CF6 50%, #38BDF8 100%);
        --gradient-emerald: linear-gradient(135deg, #22C55E 0%, #16A34A 100%);
        --gradient-amber: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);

        /* Elevation */
        --shadow-card: 0 1px 2px rgba(0, 0, 0, 0.35);
        --shadow-elevation: 0 1px 2px rgba(0, 0, 0, 0.40), 0 8px 24px rgba(0, 0, 0, 0.28);
        --shadow-hover: 0 4px 16px rgba(0, 0, 0, 0.35);
        --focus-ring: 0 0 0 2px rgba(99, 102, 241, 0.35);

        /* Type */
        --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Emoji', sans-serif;
        --font-mono: 'JetBrains Mono', 'SFMono-Regular', 'Fira Code', monospace;

        --radius-xl: 10px;
        --radius-lg: 8px;
        --radius-md: 6px;
        --radius-sm: 4px;
    }
"""

LIGHT_PALETTE = """
    :root {
        /* Surfaces */
        --bg-void: #F5F7FA;
        --bg-darker: #F5F7FA;
        --bg-sidebar: #FFFFFF;
        --bg-secondary: #F8FAFC;
        --bg-surface: #FFFFFF;
        --bg-surface-card: #FFFFFF;
        --bg-surface-elevated: #FFFFFF;
        --bg-glass-heavy: rgba(255, 255, 255, 0.95);
        --bg-input: #FFFFFF;
        --bg-hover: rgba(79, 70, 229, 0.07);
        --bg-row-hover: rgba(79, 70, 229, 0.04);
        --bg-table-header: #EEF2FF;
        --surface-tint: #EEF2FF;
        --btn-secondary-bg: #F3F6FD;
        --btn-secondary-hover: #E7ECFB;
        --page-wash:
            radial-gradient(1100px 520px at 82% -10%, rgba(79, 70, 229, 0.10), transparent 62%),
            radial-gradient(900px 480px at 6% -12%, rgba(8, 145, 178, 0.08), transparent 60%);

        /* Typography */
        --text-primary: #17243A;
        --text-secondary: #64748B;
        --text-muted: #94A3B8;
        --text-disabled: #94A3B8;

        /* Accents */
        --primary: #4F46E5;
        --primary-dark: #4338CA;
        --secondary: #0891B2;
        --accent: #7C3AED;
        --highlight: #0891B2;
        --success: #16A34A;
        --warning: #D97706;
        --error: #DC2626;

        /* Backward-compatible aliases (used by HTML component helpers) */
        --cyber-cyan: #4F46E5;
        --electric-indigo: #0891B2;
        --neon-violet: #7C3AED;
        --emerald-success: #16A34A;
        --amber-warning: #D97706;
        --crimson-error: #DC2626;

        /* Borders */
        --border: #E2E8F0;
        --border-glass: #E2E8F0;
        --border-subtle: #EDF1F7;
        --border-luminous: rgba(79, 70, 229, 0.35);

        /* Accent tints */
        --accent-soft: rgba(79, 70, 229, 0.08);
        --accent-soft-strong: rgba(79, 70, 229, 0.12);
        --accent-line: linear-gradient(90deg, #4F46E5 0%, #0891B2 100%);
        --gradient-cyber: linear-gradient(135deg, #4F46E5 0%, #0891B2 100%);
        --gradient-neural: linear-gradient(135deg, #4F46E5 0%, #7C3AED 50%, #0891B2 100%);
        --gradient-emerald: linear-gradient(135deg, #16A34A 0%, #15803D 100%);
        --gradient-amber: linear-gradient(135deg, #D97706 0%, #B45309 100%);

        /* Elevation */
        --shadow-card: 0 1px 2px rgba(15, 23, 42, 0.05);
        --shadow-elevation: 0 1px 2px rgba(15, 23, 42, 0.06), 0 6px 16px rgba(15, 23, 42, 0.06);
        --shadow-hover: 0 6px 18px rgba(15, 23, 42, 0.08);
        --focus-ring: 0 0 0 2px rgba(79, 70, 229, 0.25);

        /* Type */
        --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Emoji', sans-serif;
        --font-mono: 'JetBrains Mono', 'SFMono-Regular', 'Fira Code', monospace;

        --radius-xl: 10px;
        --radius-lg: 8px;
        --radius-md: 6px;
        --radius-sm: 4px;
    }
"""


# ==================== BASE STYLESHEET ====================

BASE_CSS = """
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&family=Noto+Emoji:wght@300..700&display=swap');

    /* ==================== TOKENS ==================== */
__PALETTE__

    /* ==================== APP CANVAS ==================== */
    html, body, [class*="css"], .stApp {
        font-family: var(--font-sans);
        color: var(--text-primary);
        background-color: var(--bg-void) !important;
    }

    .stApp {
        background-color: var(--bg-void) !important;
        background-image: var(--page-wash) !important;
        background-repeat: no-repeat !important;
        background-attachment: fixed !important;
    }

    .main .block-container,
    [data-testid="stMainBlockContainer"] {
        padding-top: 1.75rem;
        padding-bottom: 3rem;
        max-width: 1320px;
    }

    /* ==================== TYPOGRAPHY ==================== */
    h1 {
        font-size: 1.875rem !important;
        font-weight: 600 !important;
        line-height: 1.25 !important;
        letter-spacing: -0.025em !important;
        color: var(--text-primary) !important;
    }
    h2 {
        font-size: 1.5rem !important;
        font-weight: 600 !important;
        line-height: 1.3 !important;
        letter-spacing: -0.02em !important;
        color: var(--text-primary) !important;
    }
    h3, [data-testid="stHeading"] h3 {
        font-size: 1.25rem !important;
        font-weight: 600 !important;
        line-height: 1.35 !important;
        letter-spacing: -0.015em !important;
        color: var(--text-primary) !important;
        margin-bottom: 0.6rem !important;
    }
    h4, h5, h6 {
        font-weight: 600 !important;
        color: var(--text-primary) !important;
    }

    p, li, .stMarkdown, .stMarkdown p {
        color: var(--text-secondary);
        font-size: 0.9375rem;
        line-height: 1.65;
    }
    strong, b { color: var(--text-primary); font-weight: 600; }
    a { color: var(--secondary) !important; text-decoration: none; }
    a:hover { text-decoration: underline; }

    hr {
        border: 0;
        border-top: 1px solid var(--border);
        margin: 1.5rem 0;
    }

    code, pre, .font-mono, [data-testid="stMetricValue"] {
        font-family: var(--font-mono) !important;
    }
    code {
        background: var(--bg-secondary) !important;
        border: 1px solid var(--border);
        border-radius: var(--radius-sm);
        color: var(--secondary) !important;
        font-size: 0.8125rem !important;
        padding: 1px 5px;
    }
    pre {
        background: var(--bg-secondary) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
    }

    [data-testid="stCaptionContainer"], .stCaption, small {
        color: var(--text-muted) !important;
        font-size: 0.75rem !important;
    }

    /* ==================== SECTION HEADERS ==================== */
    .section-header {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 1.375rem;
        font-weight: 600;
        letter-spacing: -0.02em;
        color: var(--text-primary);
        padding-left: 12px;
        border-left: 2px solid var(--primary);
        line-height: 1.3;
        margin-bottom: 0.35rem;
    }
    .section-subheader {
        font-size: 0.8125rem;
        font-weight: 400;
        color: var(--text-muted);
        letter-spacing: 0.01em;
        margin: 0 0 1.4rem 14px;
    }

    .gradient-text, .cyber-gradient-text, .gradient-text-neural, .gradient-text-accent {
        background: none !important;
        -webkit-text-fill-color: currentColor !important;
        color: var(--text-primary) !important;
        font-weight: 600;
    }

    /* ==================== PANELS ==================== */
    .glass-container, .cyber-panel {
        background: var(--bg-surface);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 20px;
        margin: 14px 0;
        box-shadow: var(--shadow-card);
        transition: border-color 0.18s ease, background-color 0.18s ease;
        position: relative;
    }
    .glass-container:hover, .cyber-panel:hover {
        border-color: var(--border-luminous);
    }

    /* ==================== METRIC CARDS ==================== */
    .metric-card {
        background: var(--bg-surface-card);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 18px;
        text-align: left;
        position: relative;
        overflow: hidden;
        box-shadow: var(--shadow-card);
        transition: border-color 0.18s ease, box-shadow 0.18s ease, background-color 0.18s ease;
    }
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: var(--accent-line);
        opacity: 0.75;
    }
    .metric-card:hover {
        border-color: var(--border-luminous);
        box-shadow: var(--shadow-hover);
    }
    .metric-card .metric-header-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 10px;
    }
    .metric-card .metric-icon-badge {
        width: 28px;
        height: 28px;
        border-radius: var(--radius-sm);
        background: var(--surface-tint);
        border: 1px solid var(--border-luminous);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 0.9rem;
        line-height: 1;
        color: var(--primary);
    }
    .metric-card .metric-delta-tag {
        font-family: var(--font-mono);
        font-size: 0.625rem;
        font-weight: 500;
        letter-spacing: 0.04em;
        padding: 2px 6px;
        border-radius: var(--radius-sm);
        background: rgba(34, 197, 94, 0.10);
        color: var(--success);
        border: 1px solid rgba(34, 197, 94, 0.28);
        white-space: nowrap;
    }
    .metric-card .metric-value {
        font-family: var(--font-mono);
        font-size: 1.625rem;
        font-weight: 600;
        color: var(--text-primary);
        line-height: 1.2;
        letter-spacing: -0.02em;
        word-break: break-word;
    }
    .metric-card .metric-label {
        font-size: 0.6875rem;
        font-weight: 500;
        color: var(--text-muted);
        margin-top: 6px;
        text-transform: uppercase;
        letter-spacing: 0.07em;
    }

    /* ==================== HERO ==================== */
    .hero-container {
        text-align: center;
        padding: 28px 16px 10px;
    }
    .hero-hud-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 4px 12px;
        border-radius: var(--radius-sm);
        background: var(--bg-secondary);
        border: 1px solid var(--border);
        color: var(--text-muted);
        font-family: var(--font-mono);
        font-size: 0.6875rem;
        font-weight: 500;
        letter-spacing: 0.05em;
        margin-bottom: 18px;
    }
    .hero-hud-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: var(--success);
    }
    .hero-title {
        font-size: 2rem;
        font-weight: 600;
        color: var(--text-primary);
        letter-spacing: -0.03em;
        line-height: 1.2;
        margin-bottom: 12px;
    }
    .hero-subtitle {
        font-size: 0.9375rem;
        color: var(--text-secondary);
        max-width: 640px;
        margin: 0 auto 24px;
        line-height: 1.65;
    }

    /* ==================== INGESTION DROPZONE ==================== */
    .dropzone-cyber {
        position: relative;
        background: var(--bg-surface);
        border: 1px dashed var(--border);
        border-radius: var(--radius-lg);
        padding: 34px 28px;
        text-align: center;
        box-shadow: var(--shadow-card);
        transition: border-color 0.18s ease, background-color 0.18s ease;
    }
    .dropzone-cyber:hover {
        border-color: var(--border-luminous);
        background: var(--bg-surface-elevated);
    }
    .hud-corner {
        position: absolute;
        width: 12px;
        height: 12px;
        border: 1px solid var(--border-luminous);
        opacity: 0.8;
        pointer-events: none;
    }
    .hud-corner-tl { top: 10px; left: 10px; border-right: 0; border-bottom: 0; }
    .hud-corner-tr { top: 10px; right: 10px; border-left: 0; border-bottom: 0; }
    .hud-corner-bl { bottom: 10px; left: 10px; border-right: 0; border-top: 0; }
    .hud-corner-br { bottom: 10px; right: 10px; border-left: 0; border-top: 0; }
    .laser-scanner { display: none; }

    .dropzone-icon {
        font-size: 1.5rem;
        margin-bottom: 12px;
        display: inline-block;
        color: var(--primary);
    }
    .dropzone-title {
        color: var(--text-primary);
        font-size: 0.9375rem;
        font-weight: 600;
        letter-spacing: 0.02em;
        margin-bottom: 6px;
    }
    .dropzone-subtitle {
        color: var(--text-secondary);
        font-size: 0.8125rem;
        margin-bottom: 16px;
    }
    .dropzone-chips {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 6px;
        margin-top: 12px;
    }
    .dropzone-chip {
        font-family: var(--font-mono);
        font-size: 0.625rem;
        font-weight: 500;
        letter-spacing: 0.03em;
        padding: 3px 8px;
        border-radius: var(--radius-sm);
        background: var(--bg-secondary);
        color: var(--text-muted);
        border: 1px solid var(--border);
    }

    /* ==================== STREAMLIT FILE UPLOADER ==================== */
    [data-testid="stFileUploader"] {
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
    }
    [data-testid="stFileUploader"] section,
    [data-testid="stFileUploaderDropzone"] {
        background: var(--bg-surface) !important;
        border: 1px dashed var(--border) !important;
        border-radius: var(--radius-lg) !important;
        padding: 18px !important;
        transition: border-color 0.18s ease, background-color 0.18s ease !important;
    }
    [data-testid="stFileUploader"] section:hover,
    [data-testid="stFileUploaderDropzone"]:hover {
        border-color: var(--border-luminous) !important;
        background: var(--bg-surface-elevated) !important;
    }
    [data-testid="stFileUploader"] small,
    [data-testid="stFileUploaderDropzoneInstructions"] span {
        color: var(--text-muted) !important;
    }

    /* ==================== LOADING STATE ==================== */
    .neural-core-wrapper {
        text-align: center;
        padding: 28px 20px 12px;
    }
    .neural-rings-container {
        position: relative;
        width: 76px;
        height: 76px;
        margin: 0 auto 22px;
    }
    .neural-ring-outer {
        position: absolute;
        inset: 0;
        border: 2px solid var(--border);
        border-top-color: var(--primary);
        border-radius: 50%;
        animation: kydSpin 1.4s linear infinite;
    }
    .neural-ring-middle {
        position: absolute;
        inset: 14px;
        border: 2px solid var(--border-subtle);
        border-bottom-color: var(--secondary);
        border-radius: 50%;
        animation: kydSpinReverse 2s linear infinite;
    }
    .neural-ring-inner {
        position: absolute;
        inset: 28px;
        border-radius: 50%;
        background: var(--accent-soft-strong);
        border: 1px solid var(--border-luminous);
    }
    .neural-core-center {
        position: absolute;
        inset: 34px;
        border-radius: 50%;
        background: var(--primary);
    }
    @keyframes kydSpin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    @keyframes kydSpinReverse {
        from { transform: rotate(0deg); }
        to { transform: rotate(-360deg); }
    }

    /* ==================== TERMINAL TELEMETRY ==================== */
    .terminal-box {
        background: var(--bg-secondary);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 0;
        max-width: 680px;
        margin: 0 auto;
        box-shadow: var(--shadow-card);
        overflow: hidden;
        text-align: left;
    }
    .terminal-header {
        background: var(--bg-surface-elevated);
        border-bottom: 1px solid var(--border);
        padding: 8px 14px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .terminal-dots { display: flex; gap: 6px; }
    .terminal-dot { width: 8px; height: 8px; border-radius: 50%; opacity: 0.55; }
    .terminal-dot.red { background: var(--error); }
    .terminal-dot.yellow { background: var(--warning); }
    .terminal-dot.green { background: var(--success); }
    .terminal-title {
        font-family: var(--font-mono);
        font-size: 0.6875rem;
        color: var(--text-muted);
        font-weight: 500;
        letter-spacing: 0.05em;
    }
    .terminal-body {
        padding: 14px 16px;
        font-family: var(--font-mono);
        font-size: 0.75rem;
        color: var(--text-secondary);
        line-height: 1.75;
        min-height: 130px;
    }
    .terminal-line {
        margin-bottom: 3px;
        display: flex;
        align-items: baseline;
        gap: 8px;
        flex-wrap: wrap;
    }
    .terminal-time {
        color: var(--text-muted);
        font-size: 0.6875rem;
    }
    .terminal-tag {
        color: var(--secondary);
        font-weight: 600;
    }
    .cursor-blink {
        display: inline-block;
        width: 7px;
        height: 13px;
        background: var(--primary);
        vertical-align: middle;
        margin-left: 4px;
        animation: kydBlink 1.1s steps(1, end) infinite;
    }
    @keyframes kydBlink {
        0%, 49% { opacity: 1; }
        50%, 100% { opacity: 0; }
    }

    /* ==================== SKELETON LOADERS ==================== */
    .skeleton-box {
        background: var(--bg-surface-elevated);
        border-radius: var(--radius-md);
    }
    .skeleton-metric {
        height: 84px;
        border-radius: var(--radius-lg);
        background: var(--bg-surface);
        border: 1px solid var(--border);
    }

    /* ==================== FEATURE CARDS ==================== */
    .feature-card {
        background: var(--bg-surface);
        border: 1px solid var(--border);
        border-radius: var(--radius-lg);
        padding: 16px;
        min-height: 132px;
        text-align: left;
        box-shadow: var(--shadow-card);
        transition: border-color 0.18s ease, box-shadow 0.18s ease, transform 0.18s ease;
    }
    .feature-card:hover {
        border-color: var(--border-luminous);
        box-shadow: var(--shadow-hover);
        transform: translateY(-2px);
    }
    .feature-card .feature-icon {
        font-size: 1rem;
        line-height: 1;
        margin-bottom: 10px;
        display: inline-block;
        color: var(--primary);
    }
    .feature-card .feature-title {
        font-size: 0.875rem;
        font-weight: 600;
        color: var(--text-primary);
        letter-spacing: -0.01em;
        margin-bottom: 4px;
    }
    .feature-card .feature-desc {
        font-size: 0.75rem;
        color: var(--text-muted);
        line-height: 1.5;
    }

    /* ==================== BUTTONS ==================== */
    .stButton > button,
    .stDownloadButton > button,
    [data-testid="stFormSubmitButton"] > button {
        background: var(--btn-secondary-bg) !important;
        color: var(--text-primary) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        font-family: var(--font-sans) !important;
        font-weight: 500 !important;
        font-size: 0.8125rem !important;
        letter-spacing: 0.005em !important;
        padding: 0.5rem 0.9rem !important;
        box-shadow: none !important;
        transition: background-color 0.18s ease, border-color 0.18s ease, color 0.18s ease !important;
    }
    .stButton > button:hover,
    .stDownloadButton > button:hover,
    [data-testid="stFormSubmitButton"] > button:hover {
        background: var(--btn-secondary-hover) !important;
        border-color: var(--border-luminous) !important;
        color: var(--text-primary) !important;
    }
    .stButton > button:focus,
    .stDownloadButton > button:focus {
        box-shadow: var(--focus-ring) !important;
        outline: none !important;
    }
    .stButton > button:active,
    .stDownloadButton > button:active {
        background: var(--accent-soft-strong) !important;
    }
    .stButton > button[kind="primary"],
    .stDownloadButton > button[kind="primary"],
    button[data-testid="stBaseButton-primary"] {
        background: var(--primary) !important;
        border-color: var(--primary) !important;
        color: #FFFFFF !important;
    }
    .stButton > button[kind="primary"]:hover,
    .stDownloadButton > button[kind="primary"]:hover,
    button[data-testid="stBaseButton-primary"]:hover {
        background: var(--primary-dark) !important;
        border-color: var(--primary-dark) !important;
        color: #FFFFFF !important;
    }

    .btn-cyber-primary {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        background: var(--primary);
        color: #FFFFFF !important;
        font-weight: 500;
        font-size: 0.8125rem;
        padding: 10px 22px;
        border-radius: var(--radius-md);
        border: 1px solid var(--primary);
        text-decoration: none;
        transition: background-color 0.18s ease, border-color 0.18s ease;
    }
    .btn-cyber-primary:hover {
        background: var(--primary-dark);
        border-color: var(--primary-dark);
    }

    /* ==================== TABS ==================== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 2px;
        background: transparent !important;
        border: none !important;
        border-bottom: 1px solid var(--border) !important;
        border-radius: 0 !important;
        padding: 0 !important;
    }
    .stTabs [data-baseweb="tab"] {
        background: transparent !important;
        border: none !important;
        border-radius: var(--radius-sm) var(--radius-sm) 0 0 !important;
        padding: 8px 14px !important;
        font-family: var(--font-sans) !important;
        font-weight: 500 !important;
        font-size: 0.8125rem !important;
        color: var(--text-secondary) !important;
        transition: color 0.18s ease, background-color 0.18s ease !important;
    }
    .stTabs [data-baseweb="tab"]:hover {
        color: var(--text-primary) !important;
        background: var(--bg-hover) !important;
    }
    .stTabs [aria-selected="true"] {
        color: var(--text-primary) !important;
        background: transparent !important;
        font-weight: 600 !important;
    }
    .stTabs [data-baseweb="tab-highlight"] {
        background-color: var(--primary) !important;
        height: 2px !important;
    }
    .stTabs [data-baseweb="tab-border"] { display: none !important; }

    /* ==================== INPUTS ==================== */
    [data-testid="stWidgetLabel"] p,
    [data-testid="stWidgetLabel"] label,
    .stRadio label,
    .stCheckbox label,
    .stSlider label {
        color: var(--text-secondary) !important;
        font-size: 0.8125rem !important;
        font-weight: 500 !important;
    }

    div[data-baseweb="input"],
    div[data-baseweb="base-input"],
    div[data-baseweb="textarea"],
    div[data-baseweb="select"] > div {
        background-color: var(--bg-input) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        box-shadow: none !important;
        transition: border-color 0.18s ease, box-shadow 0.18s ease !important;
    }
    div[data-baseweb="input"] input,
    div[data-baseweb="textarea"] textarea,
    div[data-baseweb="select"] div {
        color: var(--text-primary) !important;
        font-family: var(--font-sans) !important;
    }
    div[data-baseweb="input"]:focus-within,
    div[data-baseweb="textarea"]:focus-within,
    div[data-baseweb="select"] > div:focus-within {
        border-color: var(--primary) !important;
        box-shadow: var(--focus-ring) !important;
    }
    div[data-baseweb="select"] svg { color: var(--text-muted) !important; fill: var(--text-muted) !important; }

    [data-baseweb="popover"] > div,
    [role="listbox"],
    [data-testid="stSelectboxVirtualDropdown"] {
        background-color: var(--bg-surface-elevated) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        box-shadow: var(--shadow-elevation) !important;
    }
    [role="option"] {
        background-color: transparent !important;
        color: var(--text-secondary) !important;
        font-size: 0.8125rem !important;
    }
    [role="option"]:hover,
    li[aria-selected="true"] {
        background-color: var(--bg-hover) !important;
        color: var(--text-primary) !important;
    }

    [data-testid="stSlider"] [role="slider"] { box-shadow: none !important; }
    [data-testid="stSlider"] div[data-baseweb="slider"] div[role="slider"] {
        background-color: var(--primary) !important;
    }

    /* ==================== EXPANDER ==================== */
    [data-testid="stExpander"] {
        background: var(--bg-surface) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        overflow: hidden;
    }
    [data-testid="stExpander"] summary,
    .streamlit-expanderHeader {
        background: transparent !important;
        color: var(--text-primary) !important;
        font-size: 0.8125rem !important;
        font-weight: 500 !important;
        border: none !important;
        border-radius: 0 !important;
        transition: color 0.18s ease, background-color 0.18s ease !important;
    }
    [data-testid="stExpander"] summary:hover {
        color: var(--secondary) !important;
        background: var(--bg-hover) !important;
    }
    [data-testid="stExpander"] details[open] > summary {
        border-bottom: 1px solid var(--border) !important;
    }
    [data-testid="stExpander"] svg { color: var(--text-muted) !important; fill: var(--text-muted) !important; }

    /* ==================== TABLES ==================== */
    .stDataFrame,
    [data-testid="stDataFrame"],
    [data-testid="stDataFrameResizable"] {
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        overflow: hidden !important;
        background: var(--bg-surface) !important;
        box-shadow: var(--shadow-card) !important;
    }

    .stat-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        background: var(--bg-surface);
        border: 1px solid var(--border);
        border-radius: var(--radius-md);
        overflow: hidden;
        font-family: var(--font-sans);
        font-size: 0.8125rem;
    }
    .stat-table thead th {
        background: var(--bg-table-header);
        color: var(--text-muted);
        padding: 9px 14px;
        text-align: left;
        font-family: var(--font-sans);
        font-weight: 600;
        font-size: 0.6875rem;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        white-space: nowrap;
        border-bottom: 1px solid var(--border);
    }
    .stat-table td {
        padding: 9px 14px;
        border-bottom: 1px solid var(--border-subtle);
        color: var(--text-primary);
        vertical-align: middle;
        line-height: 1.5;
    }
    .stat-table tr { transition: background-color 0.15s ease; }
    .stat-table tbody tr:hover { background: var(--bg-row-hover); }
    .stat-table tbody tr:last-child td { border-bottom: none; }
    .stat-table strong { color: var(--text-primary); font-weight: 600; }

    .stMarkdown table:not(.stat-table) {
        width: 100%;
        border-collapse: collapse;
        font-size: 0.8125rem;
    }
    .stMarkdown table:not(.stat-table) th {
        background: var(--bg-table-header);
        color: var(--text-muted);
        border: 1px solid var(--border);
        padding: 8px 12px;
        text-align: left;
        font-weight: 600;
    }
    .stMarkdown table:not(.stat-table) td {
        border: 1px solid var(--border-subtle);
        padding: 8px 12px;
        color: var(--text-primary);
    }

    /* ==================== PROGRESS BARS ==================== */
    .progress-bar-container {
        background: var(--border-subtle);
        border-radius: 999px;
        overflow: hidden;
        height: 4px;
        margin: 6px 0;
        border: none;
    }
    .progress-bar-fill {
        height: 100%;
        border-radius: 999px;
        transition: width 0.4s ease;
        opacity: 0.9;
    }
    .progress-bar-fill::after { content: none; }

    [data-testid="stProgress"] [role="progressbar"] {
        background-color: var(--border-subtle) !important;
    }
    [data-testid="stProgress"] [role="progressbar"] > div {
        background-color: var(--primary) !important;
    }

    /* ==================== BADGES ==================== */
    .badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 2px 8px;
        border-radius: var(--radius-sm);
        font-family: var(--font-mono);
        font-size: 0.6875rem;
        font-weight: 500;
        letter-spacing: 0.02em;
        margin-right: 6px;
        margin-bottom: 4px;
        vertical-align: middle;
    }
    .badge-primary, .badge-info {
        background: var(--accent-soft);
        color: var(--secondary);
        border: 1px solid var(--border-luminous);
    }
    .badge-secondary, .badge-accent {
        background: rgba(6, 182, 212, 0.10);
        color: var(--highlight);
        border: 1px solid rgba(6, 182, 212, 0.30);
    }
    .badge-success {
        background: rgba(34, 197, 94, 0.10);
        color: var(--success);
        border: 1px solid rgba(34, 197, 94, 0.30);
    }
    .badge-warning {
        background: rgba(245, 158, 11, 0.10);
        color: var(--warning);
        border: 1px solid rgba(245, 158, 11, 0.30);
    }
    .badge-error {
        background: rgba(239, 68, 68, 0.10);
        color: var(--error);
        border: 1px solid rgba(239, 68, 68, 0.30);
    }

    /* ==================== CALLOUTS ==================== */
    .info-box, .warning-box, .success-box {
        border: 1px solid var(--border);
        border-left-width: 2px;
        border-radius: var(--radius-md);
        padding: 12px 14px;
        margin: 12px 0;
        background: var(--bg-surface);
    }
    .info-box {
        border-left-color: var(--primary);
        background: var(--accent-soft);
    }
    .warning-box {
        border-left-color: var(--warning);
        background: rgba(245, 158, 11, 0.07);
    }
    .success-box {
        border-left-color: var(--success);
        background: rgba(34, 197, 94, 0.07);
    }
    .info-box p, .warning-box p, .success-box p {
        margin: 0;
        font-size: 0.8125rem;
        line-height: 1.6;
        color: var(--text-secondary);
    }
    .info-box strong, .warning-box strong, .success-box strong { color: var(--text-primary); }

    /* ==================== STREAMLIT ALERTS / TOASTS / SPINNER ==================== */
    [data-testid="stAlert"],
    [data-testid="stAlertContainer"] {
        border-radius: var(--radius-md) !important;
        border: 1px solid var(--border) !important;
        font-size: 0.8125rem !important;
    }
    [data-testid="stAlertContentInfo"], [data-testid="stAlertContentSuccess"],
    [data-testid="stAlertContentWarning"], [data-testid="stAlertContentError"] {
        font-size: 0.8125rem !important;
    }
    [data-testid="stToast"] {
        background: var(--bg-surface-elevated) !important;
        border: 1px solid var(--border) !important;
        border-radius: var(--radius-md) !important;
        color: var(--text-primary) !important;
        box-shadow: var(--shadow-elevation) !important;
    }
    [data-testid="stSpinner"] > div > div {
        border-top-color: var(--primary) !important;
    }
    [data-testid="stSpinner"] p { color: var(--text-secondary) !important; font-size: 0.8125rem !important; }

    /* ==================== SIDEBAR ==================== */
    section[data-testid="stSidebar"] {
        background: var(--bg-sidebar) !important;
        border-right: 1px solid var(--border) !important;
    }
    section[data-testid="stSidebar"] > div {
        background: var(--bg-sidebar) !important;
    }
    section[data-testid="stSidebar"] .block-container {
        padding-top: 1rem;
        padding-bottom: 2rem;
    }
    section[data-testid="stSidebar"] hr {
        border-top: 1px solid var(--border);
    }

    .sidebar-header {
        padding: 14px 12px 16px;
        border: 1px solid var(--border);
        border-radius: var(--radius-md);
        background: linear-gradient(160deg, var(--surface-tint) 0%, transparent 72%);
        text-align: left;
    }
    .sidebar-logo {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 30px;
        height: 30px;
        border-radius: var(--radius-md);
        background: var(--accent-soft);
        border: 1px solid var(--border-luminous);
        color: var(--secondary);
        line-height: 1;
        margin-bottom: 10px;
    }
    .sidebar-logo svg { width: 15px; height: 15px; }
    .sidebar-title {
        font-size: 0.9375rem;
        font-weight: 600;
        color: var(--text-primary);
        letter-spacing: -0.01em;
        line-height: 1.3;
    }
    .sidebar-subtitle {
        font-family: var(--font-mono);
        font-size: 0.625rem;
        font-weight: 500;
        color: var(--text-muted);
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-top: 3px;
    }
    .sidebar-hud-status {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-family: var(--font-mono);
        font-size: 0.625rem;
        font-weight: 500;
        letter-spacing: 0.05em;
        background: var(--bg-secondary);
        border: 1px solid var(--border);
        color: var(--text-muted);
        padding: 3px 8px;
        border-radius: var(--radius-sm);
        margin-top: 10px;
    }

    /* Navigation (streamlit-option-menu) */
    section[data-testid="stSidebar"] .nav-link {
        border-radius: var(--radius-sm) !important;
        transition: background-color 0.18s ease, color 0.18s ease !important;
    }
    section[data-testid="stSidebar"] .nav-link:hover {
        background-color: var(--bg-hover) !important;
    }
    section[data-testid="stSidebar"] .nav-link-selected {
        box-shadow: inset 2px 0 0 0 var(--primary);
    }
    section[data-testid="stSidebar"] [role="radiogroup"] label {
        font-size: 0.8125rem !important;
    }
    section[data-testid="stSidebar"] [role="radiogroup"] label:hover {
        color: var(--text-primary) !important;
    }

    /* ==================== FORM CONTROL INTERNALS ==================== */
    [data-testid="stFileUploaderDropzone"] button,
    [data-testid="stFileUploader"] button,
    button[data-testid="stBaseButton-secondary"] {
        background: var(--btn-secondary-bg) !important;
        border: 1px solid var(--border) !important;
        color: var(--text-primary) !important;
        border-radius: var(--radius-md) !important;
        font-size: 0.8125rem !important;
        font-weight: 500 !important;
        box-shadow: none !important;
        transition: background-color 0.18s ease, border-color 0.18s ease !important;
    }
    [data-testid="stFileUploaderDropzone"] button:hover,
    [data-testid="stFileUploader"] button:hover,
    button[data-testid="stBaseButton-secondary"]:hover {
        background: var(--btn-secondary-hover) !important;
        border-color: var(--border-luminous) !important;
        color: var(--text-primary) !important;
    }
    [data-testid="stCheckbox"] [data-baseweb="checkbox"] > div:first-child {
        border-color: var(--border) !important;
        background-color: var(--bg-input) !important;
    }
    [data-testid="stSlider"] [data-baseweb="slider"] > div > div {
        background-color: var(--border) !important;
    }
    [data-testid="stSlider"] [data-baseweb="slider"] > div > div > div {
        background-color: var(--primary) !important;
    }
    [data-testid="stFileUploaderDropzone"] * {
        color: var(--text-secondary) !important;
    }
    [data-testid="stFileUploaderDropzone"] button,
    [data-testid="stFileUploaderDropzone"] button * {
        color: var(--text-primary) !important;
    }
    [data-testid="stTooltipContent"] {
        background: var(--bg-surface-elevated) !important;
        border: 1px solid var(--border) !important;
        color: var(--text-primary) !important;
        border-radius: var(--radius-sm) !important;
    }

    /* ==================== DIVIDERS ==================== */
    .gradient-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent 0%, var(--border) 50%, transparent 100%);
        border: none;
        margin: 22px 0;
    }
    .gradient-divider-sm {
        height: 1px;
        background: linear-gradient(90deg, transparent 0%, var(--border) 50%, transparent 100%);
        border: none;
        margin: 12px 0;
    }

    /* ==================== SCROLLBARS ==================== */
    ::-webkit-scrollbar { width: 8px; height: 8px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb {
        background: var(--border);
        border-radius: 999px;
    }
    ::-webkit-scrollbar-thumb:hover { background: var(--text-disabled); }

    /* ==================== APPLICATION HEADER ==================== */
    div[class*="st-key-kyd-app-header"] {
        position: sticky;
        top: 0;
        z-index: 100;
        background: var(--bg-void);
        border-bottom: 1px solid var(--border);
        padding: 0.55rem 0 0.65rem;
        margin-bottom: 1.1rem;
    }
    .kyd-brand {
        display: flex;
        align-items: center;
        gap: 10px;
        min-width: 0;
    }
    .kyd-brand-mark {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        width: 30px;
        height: 30px;
        flex: 0 0 auto;
        border-radius: var(--radius-md);
        background: var(--accent-soft);
        border: 1px solid var(--border-luminous);
        color: var(--secondary);
    }
    .kyd-brand-mark svg { width: 15px; height: 15px; }
    .kyd-brand-text { display: flex; flex-direction: column; line-height: 1.25; min-width: 0; }
    .kyd-brand-title {
        font-size: 0.875rem;
        font-weight: 600;
        letter-spacing: -0.01em;
        color: var(--text-primary);
    }
    .kyd-brand-sub { font-size: 0.6875rem; color: var(--text-muted); }

    .kyd-crumb { display: flex; align-items: baseline; gap: 6px; min-width: 0; }
    .kyd-crumb-root {
        font-size: 0.6875rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: var(--text-muted);
    }
    .kyd-crumb-sep { color: var(--text-disabled); }
    .kyd-crumb-title {
        font-size: 0.8125rem;
        font-weight: 500;
        color: var(--text-primary);
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .kyd-status {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-size: 0.75rem;
        color: var(--text-muted);
    }
    .kyd-status-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: var(--text-disabled);
    }
    div[class*="st-key-kyd-app-header"] .badge {
        margin: 0;
        max-width: 100%;
        overflow: hidden;
        text-overflow: ellipsis;
        white-space: nowrap;
    }
    div[class*="st-key-kyd-app-header"] [data-testid="stColumn"]:last-child .stButton {
        display: flex;
        justify-content: flex-end;
    }
    div[class*="st-key-kyd-app-header"] .stButton > button {
        background: var(--bg-surface) !important;
        border: 1px solid var(--border) !important;
        color: var(--text-secondary) !important;
        font-size: 0.75rem !important;
        font-weight: 500 !important;
        letter-spacing: 0.01em !important;
        padding: 0.35rem 0.7rem !important;
        border-radius: var(--radius-md) !important;
        white-space: nowrap !important;
    }
    div[class*="st-key-kyd-app-header"] .stButton > button:hover {
        background: var(--accent-soft) !important;
        border-color: var(--border-luminous) !important;
        color: var(--text-primary) !important;
    }
    div[class*="st-key-kyd-app-header"] .stButton > button:focus {
        box-shadow: var(--focus-ring) !important;
    }

    /* ==================== STREAMLIT CHROME ==================== */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header[data-testid="stHeader"] {
        background: transparent !important;
        box-shadow: none !important;
    }
    [data-testid="stDecoration"],
    [data-testid="stHeaderActionElements"],
    [data-testid="stStatusWidget"] {
        display: none !important;
    }
    [data-testid="stSidebarCollapsedControl"] button,
    button[kind="header"],
    button[kind="headerNoPadding"] {
        background: var(--bg-surface-elevated) !important;
        border: 1px solid var(--border) !important;
        color: var(--text-primary) !important;
        border-radius: var(--radius-sm) !important;
        transition: background-color 0.18s ease, border-color 0.18s ease !important;
    }
    [data-testid="stSidebarCollapsedControl"] button:hover,
    button[kind="header"]:hover,
    button[kind="headerNoPadding"]:hover {
        background: var(--accent-soft) !important;
        border-color: var(--border-luminous) !important;
    }

    /* ==================== RESPONSIVE ==================== */
    @media (max-width: 900px) {
        div[class*="st-key-kyd-app-header"] {
            position: static;
            padding-top: 0.25rem;
        }
        .kyd-crumb-root,
        .kyd-crumb-sep {
            display: none;
        }
        div[class*="st-key-kyd-app-header"] [data-testid="stColumn"]:last-child .stButton {
            justify-content: flex-start;
        }
    }

    @media (max-width: 768px) {
        .hero-title { font-size: 1.75rem; }
        .hero-subtitle { font-size: 0.875rem; }
        .metric-card { padding: 14px; }
        .metric-card .metric-value { font-size: 1.375rem; }
        .section-header { font-size: 1.25rem; }
        .feature-card { min-height: auto; }
        .dropzone-cyber { padding: 26px 16px; }
    }
</style>
"""

# Backwards-compatible default export (dark palette).
CUSTOM_CSS = BASE_CSS.replace("__PALETTE__", DARK_PALETTE)
