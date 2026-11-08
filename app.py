"""
Know-Your-Data — Main Application Entrypoint & Executive Cyber Cockpit.
Automated Exploratory Data Analysis platform powered by Neural Telemetry.
"""

import streamlit as st

st.set_page_config(
    page_title="Know Your Data // Neural EDA Cockpit",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

try:
    from streamlit_option_menu import option_menu
except ImportError:
    option_menu = None

from utils.styles import inject_custom_css
from utils.plotting import setup_plotly_theme
from utils.helpers import badge_html, format_bytes, format_number

def clean_html(html_str: str) -> str:
    """Safely strip indentation and blank lines so CommonMark never treats HTML as code blocks."""
    lines = [line.strip() for line in html_str.strip().split("\n") if line.strip()]
    return "".join(lines)


BRAND_MARK_SVG = (
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" '
    'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
    '<ellipse cx="12" cy="5" rx="8" ry="3"></ellipse>'
    '<path d="M4 5v14c0 1.66 3.58 3 8 3s8-1.34 8-3V5"></path>'
    '<path d="M4 12c0 1.66 3.58 3 8 3s8-1.34 8-3"></path>'
    '</svg>'
)


def main():
    if "kyd_theme" not in st.session_state:
        st.session_state["kyd_theme"] = "dark"
    theme = st.session_state["kyd_theme"]

    inject_custom_css(theme)
    setup_plotly_theme(theme)

    # Force menu re-render on theme change
    if "menu_key" not in st.session_state:
        st.session_state["menu_key"] = 0
    if st.session_state.get("prev_theme") != theme:
        st.session_state["menu_key"] += 1
        st.session_state["prev_theme"] = theme

    with st.sidebar:
        st.markdown(
            clean_html(f"""
            <div class="sidebar-header">
                <div class="sidebar-logo">{BRAND_MARK_SVG}</div>
                <div class="sidebar-title">Know Your Data</div>
                <div class="sidebar-subtitle">ANALYTICS WORKSPACE</div>
                <div class="sidebar-hud-status">
                    <span style="color:#22C55E; font-size:9px;">●</span> SYSTEM OPERATIONAL
                </div>
            </div>
            """),
            unsafe_allow_html=True,
        )

        st.markdown(
            "<hr style='margin-top: 14px; margin-bottom: 14px; border: 0; height: 1px; background: linear-gradient(to right, transparent, rgba(99,102,241,0.25), transparent);'>",
            unsafe_allow_html=True,
        )

        menu_options = [
            "Upload", "Overview", "Alerts", "Missing Values", "Statistics",
            "Distributions", "Correlations", "Interactions",
            "Duplicates", "Outliers", "Type Hints", "Text Analysis", "Report"
        ]

        if option_menu:
            selected = option_menu(
                menu_title=None,
                options=menu_options,
                icons=[
                    "cloud-upload", "grid", "exclamation-triangle", "search",
                    "bar-chart-line", "graph-up", "link-45deg", "arrows-angle-expand",
                    "files", "lightning", "lightbulb", "fonts", "download"
                ],
                default_index=0,
                key=f"menu_{st.session_state['menu_key']}",
                styles={
                    "container": {"padding": "4px", "background-color": "transparent"},
                    "icon": {"color": "var(--secondary)", "font-size": "14px"},
                    "nav-link": {
                        "font-size": "13.5px",
                        "font-family": "Inter, sans-serif",
                        "text-align": "left",
                        "margin": "3px 0",
                        "padding": "9px 12px",
                        "border-radius": "var(--radius-md)",
                        "color": "var(--text-secondary)",
                        "transition": "all 0.2s ease",
                        "border": "1px solid transparent",
                    },
                    "nav-link-hover": {
                        "background-color": "var(--bg-hover)",
                        "color": "var(--text-primary)",
                    },
                    "nav-link-selected": {
                        "background": "var(--accent-soft-strong)",
                        "color": "var(--text-primary)",
                        "font-weight": "600",
                        "border": "1px solid var(--border-luminous)",
                    },
                },
            )
        else:
            selected = st.radio("Navigation", menu_options)

        if "df" in st.session_state and st.session_state["df"] is not None:
            df = st.session_state["df"]

            st.markdown(
                "<hr style='margin-top: 18px; margin-bottom: 14px; border: 0; height: 1px; background: linear-gradient(to right, transparent, rgba(99,102,241,0.25), transparent);'>",
                unsafe_allow_html=True,
            )
            st.markdown(
                "<div style='font-family: var(--font-mono); font-size: 0.75rem; color: var(--secondary); letter-spacing: 0.1em; margin-bottom: 8px;'>// ACTIVE DATASET STREAM</div>",
                unsafe_allow_html=True,
            )

            file_name = st.session_state.get("file_name", "Dataset")
            st.markdown(badge_html("FILE", file_name, "primary"), unsafe_allow_html=True)
            st.markdown(badge_html("ROWS", format_number(df.shape[0]), "success"), unsafe_allow_html=True)
            st.markdown(badge_html("COLS", str(df.shape[1]), "accent"), unsafe_allow_html=True)

            mem_usage = df.memory_usage(deep=True).sum()
            st.markdown(badge_html("RAM", format_bytes(mem_usage), "secondary"), unsafe_allow_html=True)

            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("⚡ Flush Stream Buffer", use_container_width=True):
                for k in ["df", "file_name", "file_info", "excel_sheets", "raw_file_bytes", "current_sheet", "report_html", "simulating_analysis"]:
                    st.session_state.pop(k, None)
                st.rerun()

    # ---------- APPLICATION HEADER ----------
    header_df = st.session_state.get("df")
    with st.container(key="kyd-app-header"):
        h_brand, h_context, h_status, h_theme = st.columns(
            [3.0, 2.4, 2.4, 1.4], vertical_alignment="center"
        )

        with h_brand:
            st.markdown(
                clean_html(f"""
                <div class="kyd-brand">
                    <span class="kyd-brand-mark">{BRAND_MARK_SVG}</span>
                    <span class="kyd-brand-text">
                        <span class="kyd-brand-title">Know Your Data</span>
                        <span class="kyd-brand-sub">Analytics Workspace</span>
                    </span>
                </div>
                """),
                unsafe_allow_html=True,
            )

        with h_context:
            st.markdown(
                clean_html(f"""
                <div class="kyd-crumb">
                    <span class="kyd-crumb-root">Workspace</span>
                    <span class="kyd-crumb-sep">/</span>
                    <span class="kyd-crumb-title">{selected}</span>
                </div>
                """),
                unsafe_allow_html=True,
            )

        with h_status:
            if header_df is not None:
                st.markdown(
                    badge_html("DATASET", st.session_state.get("file_name", "Dataset"), "primary"),
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    '<span class="kyd-status"><span class="kyd-status-dot"></span>No dataset loaded</span>',
                    unsafe_allow_html=True,
                )

        with h_theme:
            next_theme = "light" if theme == "dark" else "dark"
            if st.button(
                "☀ Light" if theme == "dark" else "☾ Dark",
                key="kyd_theme_toggle",
                help=f"Switch to {next_theme} theme",
            ):
                st.session_state["kyd_theme"] = next_theme
                st.rerun()

    no_data_html = clean_html("""
    <div style="text-align: center; padding: 90px 20px; animation: fadeInUp 0.6s ease-out;">
        <div style="font-size: 3rem; margin-bottom: 16px; color: #6366F1;">⚡</div>
        <div style="font-size: 1.5rem; margin-bottom: 8px; color: #F1F5F9; font-weight: 600;">No Dataset Stream Detected</div>
        <div style="color: #94A3B8; font-size: 0.95rem; max-width: 500px; margin: 0 auto 24px;">
            The Neural EDA engine requires a dataset stream to compute telemetry.
            Please visit the Ingestion cockpit to upload a file or launch the demo dataset.
        </div>
    </div>
    """)

    if selected == "Upload":
        from src.data_loader import render_upload
        df = render_upload()
        if df is not None:
            st.session_state["df"] = df
    elif "df" not in st.session_state or st.session_state["df"] is None:
        st.markdown(no_data_html, unsafe_allow_html=True)
    else:
        df = st.session_state["df"]
        if selected == "Overview":
            from src.overview import render
            render(df)
        elif selected == "Alerts":
            from src.alerts import render
            render(df)
        elif selected == "Missing Values":
            from src.missing_values import render
            render(df)
        elif selected == "Statistics":
            from src.statistics import render
            render(df)
        elif selected == "Distributions":
            from src.distributions import render
            render(df)
        elif selected == "Correlations":
            from src.correlations import render
            render(df)
        elif selected == "Interactions":
            from src.interactions import render
            render(df)
        elif selected == "Duplicates":
            from src.duplicates import render
            render(df)
        elif selected == "Outliers":
            from src.outliers import render
            render(df)
        elif selected == "Type Hints":
            from src.type_recommendations import render
            render(df)
        elif selected == "Text Analysis":
            from src.text_analysis import render
            render(df)
        elif selected == "Report":
            from src.report_generator import render
            render(df)


if __name__ == "__main__":
    main()
