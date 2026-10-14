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


def main():
    inject_custom_css()
    setup_plotly_theme()

    with st.sidebar:
        st.markdown(
            clean_html("""
            <div class="sidebar-header">
                <div class="sidebar-logo">⚡</div>
                <div class="sidebar-title">Know Your Data</div>
                <div class="sidebar-subtitle">// NEURAL EDA COCKPIT</div>
                <div class="sidebar-hud-status">
                    <span style="color:#10B981; font-size:9px;">●</span> SYSTEM OPERATIONAL
                </div>
            </div>
            """),
            unsafe_allow_html=True,
        )

        st.markdown(
            "<hr style='margin-top: 14px; margin-bottom: 14px; border: 0; height: 1px; background: linear-gradient(to right, transparent, rgba(0,242,254,0.3), transparent);'>",
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
                styles={
                    "container": {"padding": "4px", "background-color": "transparent"},
                    "icon": {"color": "#00F2FE", "font-size": "15px"},
                    "nav-link": {
                        "font-size": "13.5px",
                        "font-family": "Inter, sans-serif",
                        "text-align": "left",
                        "margin": "3px 0",
                        "padding": "9px 12px",
                        "border-radius": "10px",
                        "color": "#94A3B8",
                        "transition": "all 0.25s ease",
                        "border": "1px solid transparent",
                    },
                    "nav-link-selected": {
                        "background": "linear-gradient(135deg, rgba(0, 242, 254, 0.18), rgba(79, 172, 254, 0.25))",
                        "color": "#00F2FE",
                        "font-weight": "700",
                        "border": "1px solid rgba(0, 242, 254, 0.4)",
                        "box-shadow": "0 0 15px rgba(0, 242, 254, 0.2)",
                    },
                },
            )
        else:
            selected = st.radio("Navigation", menu_options)

        if "df" in st.session_state and st.session_state["df"] is not None:
            df = st.session_state["df"]

            st.markdown(
                "<hr style='margin-top: 18px; margin-bottom: 14px; border: 0; height: 1px; background: linear-gradient(to right, transparent, rgba(0,242,254,0.3), transparent);'>",
                unsafe_allow_html=True,
            )
            st.markdown(
                "<div style='font-family: var(--font-mono); font-size: 0.75rem; color: #00F2FE; letter-spacing: 0.1em; margin-bottom: 8px;'>// ACTIVE DATASET STREAM</div>",
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

    no_data_html = clean_html("""
    <div style="text-align: center; padding: 90px 20px; animation: fadeInUp 0.6s ease-out;">
        <div style="font-size: 4rem; margin-bottom: 16px; filter: drop-shadow(0 0 25px rgba(0, 242, 254, 0.5));">⚡</div>
        <div class="gradient-text" style="font-size: 1.8rem; margin-bottom: 8px;">No Dataset Stream Detected</div>
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
