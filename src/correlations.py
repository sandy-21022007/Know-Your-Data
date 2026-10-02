import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from utils.helpers import (
    format_number, badge_html, section_header_html, info_box_html,
    get_numeric_columns, metric_card_html, glass_container_start, glass_container_end
)
from utils.plotting import style_figure, get_colorscale, CHART_CONFIG

def render(df: pd.DataFrame) -> None:
    """
    Render the correlation analysis module.
    """
    st.markdown(section_header_html("Correlation Analysis", "Understand linear relationships between variables"), unsafe_allow_html=True)
    
    numeric_cols = get_numeric_columns(df)
    if len(numeric_cols) < 2:
        st.markdown(info_box_html("Not enough numeric columns for correlation analysis. At least 2 numeric columns are required."), unsafe_allow_html=True)
        return
        
    st.markdown(glass_container_start(), unsafe_allow_html=True)
    
    method = st.radio("Correlation Method", ["Pearson", "Spearman", "Kendall"], horizontal=True)
    method_key = method.lower()
    
    corr_matrix = df[numeric_cols].corr(method=method_key)
    
    # Highly correlated pairs
    threshold = st.slider("Absolute Correlation Threshold", min_value=0.0, max_value=1.0, value=0.7, step=0.05)
    
    pairs = []
    for i in range(len(corr_matrix.columns)):
        for j in range(i+1, len(corr_matrix.columns)):
            col1 = corr_matrix.columns[i]
            col2 = corr_matrix.columns[j]
            val = corr_matrix.iloc[i, j]
            if not np.isnan(val) and abs(val) >= threshold:
                pairs.append((col1, col2, val))
                
    pairs.sort(key=lambda x: abs(x[2]), reverse=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(metric_card_html("Highly Correlated Pairs", str(len(pairs)), "🔗"), unsafe_allow_html=True)
        
    avg_corr = corr_matrix.abs().mean().mean() if not corr_matrix.empty else 0
    with col2:
        st.markdown(metric_card_html("Avg Abs Correlation", f"{avg_corr:.3f}", "📊"), unsafe_allow_html=True)
        
    strongest_pair = f"{pairs[0][0]} & {pairs[0][1]}" if pairs else "None"
    with col3:
        st.markdown(metric_card_html("Strongest Pair", strongest_pair, "⚡"), unsafe_allow_html=True)
        
    st.markdown(glass_container_end(), unsafe_allow_html=True)
    
    tab1, tab2, tab3 = st.tabs(["Correlation Heatmap", "Highly Correlated Pairs", "Scatter Plot Explorer"])
    
    with tab1:
        st.subheader("Correlation Heatmap")
        
        # Calculate size based on number of columns
        height = max(400, len(numeric_cols) * 35)
        
        # Create heatmap
        text_matrix = np.around(corr_matrix.values, decimals=2)
        fig = go.Figure(data=go.Heatmap(
            z=corr_matrix.values,
            x=corr_matrix.columns,
            y=corr_matrix.columns,
            colorscale=get_colorscale('correlation'),
            zmin=-1, zmax=1,
            text=text_matrix,
            texttemplate="%{text}",
            textfont={"size": 10},
            hovertemplate="X: %{x}<br>Y: %{y}<br>Correlation: %{z:.3f}<extra></extra>"
        ))
        
        fig.update_layout(
            height=height,
            title=f"{method} Correlation Matrix",
            xaxis_title="Features",
            yaxis_title="Features",
            yaxis_autorange='reversed'
        )
        style_figure(fig)
        st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)
        
    with tab2:
        st.subheader("Highly Correlated Pairs")
        
        if not pairs:
            st.markdown(info_box_html(f"No pairs found with absolute correlation >= {threshold}"), unsafe_allow_html=True)
        else:
            pair_data = []
            for c1, c2, val in pairs:
                if val >= 0.7:
                    status = badge_html("STRONG POSITIVE", "success")
                elif val <= -0.7:
                    status = badge_html("STRONG NEGATIVE", "error")
                else:
                    status = badge_html("MODERATE", "warning")
                    
                pair_data.append({
                    "Feature 1": c1,
                    "Feature 2": c2,
                    "Correlation": round(val, 4),
                    "Strength": status
                })
            
            # Simple HTML table for display
            html = "<table class='stat-table'><thead><tr><th>Feature 1</th><th>Feature 2</th><th>Correlation</th><th>Strength</th></tr></thead><tbody>"
            for row in pair_data:
                html += f"<tr><td>{row['Feature 1']}</td><td>{row['Feature 2']}</td><td>{row['Correlation']}</td><td>{row['Strength']}</td></tr>"
            html += "</tbody></table>"
            st.markdown(html, unsafe_allow_html=True)
            
    with tab3:
        st.subheader("Scatter Plot Explorer")
        
        col1, col2 = st.columns(2)
        with col1:
            x_col = st.selectbox("X-axis Feature", numeric_cols, index=0)
        with col2:
            y_idx = 1 if len(numeric_cols) > 1 else 0
            y_col = st.selectbox("Y-axis Feature", numeric_cols, index=y_idx)
            
        if x_col and y_col:
            scatter_fig = px.scatter(df, x=x_col, y=y_col, trendline="ols", title=f"Scatter Plot: {x_col} vs {y_col}")
            style_figure(scatter_fig)
            st.plotly_chart(scatter_fig, use_container_width=True, config=CHART_CONFIG)
