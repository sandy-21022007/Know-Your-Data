"""Missing/null value analysis module."""

import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

from utils.helpers import (
    format_number, format_percentage,
    metric_card_html, progress_bar_html, badge_html,
    section_header_html, divider_html,
    info_box_html, success_box_html,
    glass_container_start, glass_container_end,
)
from utils.plotting import (
    CHART_CONFIG, style_figure, get_colorscale, COLORS
)

def render(df: pd.DataFrame) -> None:
    """Render missing values analysis."""
    st.markdown(section_header_html("Missing Values", "Analyze completeness and missing data patterns"), unsafe_allow_html=True)

    total_cells = np.prod(df.shape)
    total_missing = df.isnull().sum().sum()
    
    if total_missing == 0:
        st.markdown(success_box_html("🎉 Dataset is 100% complete! No missing values found."), unsafe_allow_html=True)
        return

    cols = st.columns(4)
    cols_with_missing = (df.isnull().sum() > 0).sum()
    complete_rows = df.dropna().shape[0]
    completeness = ((total_cells - total_missing) / total_cells) * 100 if total_cells else 0
    
    with cols[0]:
        st.markdown(metric_card_html("Total Missing Values", format_number(total_missing), "🔍"), unsafe_allow_html=True)
    with cols[1]:
        st.markdown(metric_card_html("Columns with Missing", format_number(cols_with_missing), "📋"), unsafe_allow_html=True)
    with cols[2]:
        st.markdown(metric_card_html("Complete Rows", format_number(complete_rows), "✅"), unsafe_allow_html=True)
    with cols[3]:
        st.markdown(metric_card_html("Overall Completeness", format_percentage(completeness), "📊"), unsafe_allow_html=True)

    st.markdown(divider_html(), unsafe_allow_html=True)

    missing_series = df.isnull().sum()
    missing_series = missing_series[missing_series > 0].sort_values(ascending=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Missing Values Count per Column")
        if not missing_series.empty:
            missing_pcts = (missing_series / len(df)) * 100
            fig = px.bar(
                x=missing_series.values, 
                y=missing_series.index, 
                orientation='h',
                color=missing_pcts.values,
                color_continuous_scale=['#00c853', '#ff6d00', '#ff1744'],
                labels={'x': 'Missing Count', 'y': 'Column', 'color': 'Missing %'}
            )
            style_figure(fig)
            st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)
            
    with col2:
        st.subheader("Missing Values Heatmap")
        sample_df = df if len(df) <= 500 else df.sample(500, random_state=42)
        # 1 for missing, 0 for present
        heatmap_data = sample_df.isnull().astype(int)
        
        fig2 = px.imshow(
            heatmap_data,
            color_continuous_scale=['#1a1f2e', '#ff1744'],
            aspect="auto",
            labels=dict(x="Columns", y="Rows", color="Missing")
        )
        fig2.update_layout(coloraxis_showscale=False)
        style_figure(fig2)
        st.plotly_chart(fig2, use_container_width=True, config=CHART_CONFIG)

    st.markdown(divider_html(), unsafe_allow_html=True)
    st.subheader("Per-Column Missing Details")
    
    details_html = """
    <table style='width:100%; text-align:left; border-collapse: collapse;'>
        <tr>
            <th style='padding:8px; border-bottom:1px solid #333;'>Column</th>
            <th style='padding:8px; border-bottom:1px solid #333;'>Missing Count</th>
            <th style='padding:8px; border-bottom:1px solid #333; width:40%;'>Missing %</th>
            <th style='padding:8px; border-bottom:1px solid #333;'>Present Count</th>
            <th style='padding:8px; border-bottom:1px solid #333;'>Status</th>
        </tr>
    """
    
    for col in df.columns:
        m_count = df[col].isnull().sum()
        m_pct = (m_count / len(df)) * 100
        p_count = len(df) - m_count
        
        if m_pct == 0:
            status = badge_html("COMPLETE", "success")
        elif m_pct < 5:
            status = badge_html("LOW", "info")
        elif m_pct < 20:
            status = badge_html("MODERATE", "warning")
        else:
            status = badge_html("HIGH", "error")
            
        details_html += f"""
        <tr>
            <td style='padding:8px; border-bottom:1px solid #222;'>{col}</td>
            <td style='padding:8px; border-bottom:1px solid #222;'>{m_count}</td>
            <td style='padding:8px; border-bottom:1px solid #222;'>{progress_bar_html(m_pct)}</td>
            <td style='padding:8px; border-bottom:1px solid #222;'>{p_count}</td>
            <td style='padding:8px; border-bottom:1px solid #222;'>{status}</td>
        </tr>
        """
    details_html += "</table>"
    st.markdown(details_html, unsafe_allow_html=True)

    st.markdown(divider_html(), unsafe_allow_html=True)
    
    col3, col4 = st.columns([1, 1])
    with col3:
        st.subheader("Missing Value Patterns")
        st.write("Correlation of missingness between columns.")
        missing_df = df.isnull().astype(int)
        corr_matrix = missing_df.loc[:, (missing_df.sum() > 0)].corr()
        if not corr_matrix.empty and len(corr_matrix.columns) > 1:
            fig3 = px.imshow(corr_matrix, color_continuous_scale="RdBu_r", zmin=-1, zmax=1)
            style_figure(fig3)
            st.plotly_chart(fig3, use_container_width=True, config=CHART_CONFIG)
        else:
            st.info("Not enough columns with missing values to show correlations.")
            
    with col4:
        st.subheader("Handling Suggestions")
        st.markdown(glass_container_start(), unsafe_allow_html=True)
        st.markdown(info_box_html("If < 5% missing: Safe to drop rows"), unsafe_allow_html=True)
        st.markdown(info_box_html("If 5-30% missing: Consider imputation (mean/median/mode)"), unsafe_allow_html=True)
        st.markdown(info_box_html("If > 30% missing: Consider dropping the column or advanced imputation"), unsafe_allow_html=True)
        st.markdown(glass_container_end(), unsafe_allow_html=True)
