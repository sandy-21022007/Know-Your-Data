import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils.helpers import (
    format_number, format_percentage, section_header_html, info_box_html,
    get_numeric_columns, metric_card_html, progress_bar_html, badge_html,
    glass_container_start, glass_container_end
)
from utils.plotting import style_figure, CHART_CONFIG

def render(df: pd.DataFrame) -> None:
    """
    Render outlier detection module.
    """
    st.markdown(section_header_html("Outlier Detection", "Identify anomalous values in numeric columns"), unsafe_allow_html=True)
    
    numeric_cols = get_numeric_columns(df)
    if not numeric_cols:
        st.markdown(info_box_html("No numeric columns available for outlier detection."), unsafe_allow_html=True)
        return
        
    st.markdown(glass_container_start(), unsafe_allow_html=True)
    method = st.radio("Outlier Detection Method", ["IQR Method", "Z-Score Method"], horizontal=True)
    st.markdown(glass_container_end(), unsafe_allow_html=True)
    
    outlier_results = {}
    total_data_points = len(df) * len(numeric_cols)
    total_outliers = 0
    cols_with_outliers = 0
    
    if method == "IQR Method":
        multiplier = st.slider("IQR Multiplier", min_value=1.0, max_value=3.0, value=1.5, step=0.1)
        
        for col in numeric_cols:
            q1 = df[col].quantile(0.25)
            q3 = df[col].quantile(0.75)
            iqr = q3 - q1
            lower_bound = q1 - multiplier * iqr
            upper_bound = q3 + multiplier * iqr
            
            outliers = (df[col] < lower_bound) | (df[col] > upper_bound)
            outlier_count = outliers.sum()
            
            if outlier_count > 0:
                cols_with_outliers += 1
                total_outliers += outlier_count
                
            outlier_results[col] = {
                "count": outlier_count,
                "percentage": outlier_count / len(df) if len(df) > 0 else 0,
                "bound_info": f"[{lower_bound:.2f}, {upper_bound:.2f}]",
                "mask": outliers
            }
            
    else: # Z-Score Method
        threshold = st.slider("Z-Score Threshold", min_value=2.0, max_value=5.0, value=3.0, step=0.1)
        
        for col in numeric_cols:
            mean = df[col].mean()
            std = df[col].std()
            
            if std == 0 or pd.isna(std):
                outliers = pd.Series([False] * len(df), index=df.index)
            else:
                z_scores = np.abs((df[col] - mean) / std)
                outliers = z_scores > threshold
                
            outlier_count = outliers.sum()
            
            if outlier_count > 0:
                cols_with_outliers += 1
                total_outliers += outlier_count
                
            outlier_results[col] = {
                "count": outlier_count,
                "percentage": outlier_count / len(df) if len(df) > 0 else 0,
                "bound_info": f"|z| > {threshold}",
                "mask": outliers
            }
            
    outlier_pct = (total_outliers / total_data_points * 100) if total_data_points > 0 else 0
    
    st.markdown(glass_container_start(), unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(metric_card_html("🚨", format_number(total_outliers), "Total Outliers Detected"), unsafe_allow_html=True)
    with col2:
        st.markdown(metric_card_html("📋", f"{cols_with_outliers} / {len(numeric_cols)}", "Columns w/ Outliers"), unsafe_allow_html=True)
    with col3:
        st.markdown(metric_card_html("📉", format_percentage(outlier_pct), "% Outlier Data Points"), unsafe_allow_html=True)
    st.markdown(glass_container_end(), unsafe_allow_html=True)
    
    st.subheader("Per-column Outlier Summary")
    
    html = "<table class='stat-table'><thead><tr><th>Column</th><th>Outlier Count</th><th>% Outliers</th><th>Bounds / Threshold</th><th>Status</th></tr></thead><tbody>"
    for col, res in outlier_results.items():
        count = res["count"]
        pct = res["percentage"]
        bounds = res["bound_info"]
        
        if count == 0:
            status = badge_html("CLEAN", "success")
        elif pct > 0.05:
            status = badge_html("HIGH", "error")
        else:
            status = badge_html("LOW", "warning")
            
        prog = progress_bar_html(pct)
        html += f"<tr><td>{col}</td><td>{count}</td><td>{prog}</td><td>{bounds}</td><td>{status}</td></tr>"
    html += "</tbody></table>"
    st.markdown(html, unsafe_allow_html=True)
    
    st.subheader("Distribution Box Plots")
    plot_cols = [col for col, res in outlier_results.items() if res["count"] > 0]
    if not plot_cols:
        plot_cols = numeric_cols[:5] # Plot first 5 if no outliers
        
    for col in plot_cols:
        fig = px.box(df, y=col, title=f"Distribution of {col}", points="outliers")
        style_figure(fig)
        st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)
        
    st.subheader("Outlier Details")
    if cols_with_outliers > 0:
        det_col = st.selectbox("Select column to view outlier rows", [c for c, r in outlier_results.items() if r["count"] > 0])
        if det_col:
            mask = outlier_results[det_col]["mask"]
            st.dataframe(df[mask], use_container_width=True)
    else:
        st.info("No outliers to display.")
