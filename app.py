import streamlit as st

st.set_page_config(
    page_title="Know Your Data — EDA Tool",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

try:
    from streamlit_option_menu import option_menu
except ImportError:
    option_menu = None

from utils.styles import inject_custom_css
from utils.plotting import setup_plotly_theme
from utils.helpers import badge_html, format_bytes

def main():
    inject_custom_css()
    setup_plotly_theme()
    
    with st.sidebar:
        st.markdown("""
        <div class="sidebar-header">
            <div class="sidebar-logo">📊</div>
            <div class="sidebar-title">Know Your Data</div>
            <div class="sidebar-subtitle">EDA Tool</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<hr style='margin-top: 10px; margin-bottom: 10px; border: 0; height: 1px; background: linear-gradient(to right, transparent, rgba(255,255,255,0.2), transparent);'>", unsafe_allow_html=True)
        
        menu_options = [
            "Upload", "Overview", "Alerts", "Missing Values", "Statistics",
            "Distributions", "Correlations", "Interactions",
            "Duplicates", "Outliers", "Type Hints", "Text Analysis", "Report"
        ]
        
        if option_menu:
            selected = option_menu(
                menu_title=None,
                options=menu_options,
                icons=["cloud-upload", "grid", "exclamation-triangle", "search",
                       "bar-chart-line", "graph-up", "link-45deg", "arrows-angle-expand",
                       "files", "lightning", "lightbulb", "fonts", "download"],
                default_index=0,
                styles={
                    "container": {"padding": "4px", "background-color": "transparent"},
                    "icon": {"color": "#667eea", "font-size": "16px"},
                    "nav-link": {
                        "font-size": "14px", "text-align": "left",
                        "margin": "2px 0", "padding": "10px 14px",
                        "border-radius": "8px", "color": "#a0aec0",
                        "transition": "all 0.3s ease",
                    },
                    "nav-link-selected": {
                        "background": "linear-gradient(135deg, #667eea, #764ba2)",
                        "color": "white", "font-weight": "600",
                    },
                },
            )
        else:
            selected = st.radio("Navigation", menu_options)
            
        if 'df' in st.session_state and st.session_state['df'] is not None:
            df = st.session_state['df']
            
            st.markdown("<hr style='margin-top: 20px; margin-bottom: 20px; border: 0; height: 1px; background: linear-gradient(to right, transparent, rgba(255,255,255,0.2), transparent);'>", unsafe_allow_html=True)
            st.markdown("### Dataset Info")
            
            # Show badges
            file_name = st.session_state.get('file_name', 'Dataset')
            st.markdown(badge_html("File", file_name, "primary"), unsafe_allow_html=True)
            st.markdown(badge_html("Rows", str(df.shape[0]), "success"), unsafe_allow_html=True)
            st.markdown(badge_html("Columns", str(df.shape[1]), "accent"), unsafe_allow_html=True)
            
            mem_usage = df.memory_usage(deep=True).sum()
            st.markdown(badge_html("Memory", format_bytes(mem_usage), "secondary"), unsafe_allow_html=True)
            
            st.markdown("<br>", unsafe_allow_html=True)
            if st.button("Clear Data", use_container_width=True):
                for k in ['df', 'file_name', 'file_info', 'excel_sheets', 'raw_file_bytes', 'current_sheet', 'report_html']:
                    st.session_state.pop(k, None)
                st.rerun()

    no_data_html = """
    <div style="text-align:center; padding:80px 20px; animation: fadeInUp 0.6s ease-out;">
        <div style="font-size:4rem; margin-bottom:16px;">📂</div>
        <div class="gradient-text" style="font-size:1.5rem; margin-bottom:8px;">No Data Loaded</div>
        <div style="color:#a0aec0;">Please go to the Upload page and upload a dataset to begin analysis.</div>
    </div>
    """

    if selected == "Upload":
        from src.data_loader import render_upload
        df = render_upload()
        if df is not None:
            st.session_state['df'] = df
    elif 'df' not in st.session_state or st.session_state['df'] is None:
        st.markdown(no_data_html, unsafe_allow_html=True)
    else:
        df = st.session_state['df']
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
