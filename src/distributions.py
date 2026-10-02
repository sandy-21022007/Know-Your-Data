"""Column-wise distribution plots module."""

import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import scipy.stats as stats

from utils.helpers import (
    get_numeric_columns, get_categorical_columns, format_number,
    section_header_html, glass_container_start, glass_container_end,
)
from utils.plotting import CHART_CONFIG, style_figure, COLORS

def render(df: pd.DataFrame) -> None:
    """Render distribution analysis."""
    st.markdown(section_header_html("Distributions", "Explore column distributions and densities"), unsafe_allow_html=True)
    
    if df.empty:
        st.warning("Dataset is empty.")
        return

    num_cols = get_numeric_columns(df)
    cat_cols = get_categorical_columns(df)
    all_cols = df.columns.tolist()

    tabs = st.tabs(["Single Column", "All Columns Overview"])
    
    with tabs[0]:
        selected_col = st.selectbox("Select Column to Analyze", all_cols)
        
        if selected_col:
            series = df[selected_col].dropna()
            
            if len(series) == 0:
                st.warning("Column is entirely empty.")
            elif selected_col in num_cols:
                # Numeric Analysis
                st.markdown(glass_container_start(), unsafe_allow_html=True)
                col1, col2 = st.columns([3, 1])
                
                with col2:
                    st.write("**Summary Stats**")
                    st.metric("Mean", format_number(series.mean()))
                    st.metric("Median", format_number(series.median()))
                    try:
                        mode_val = series.mode().iloc[0]
                    except:
                        mode_val = np.nan
                    st.metric("Mode", format_number(mode_val) if pd.notnull(mode_val) else "N/A")
                    st.metric("Std Dev", format_number(series.std()))
                    st.metric("Skewness", format_number(stats.skew(series)))
                    st.metric("Kurtosis", format_number(stats.kurtosis(series)))
                    
                    if len(series) >= 3:
                        if len(series) < 5000:
                            stat, p = stats.shapiro(series)
                            test_name = "Shapiro-Wilk"
                        else:
                            stat, p = stats.normaltest(series)
                            test_name = "D'Agostino"
                        
                        st.write(f"**Normality ({test_name})**")
                        st.write(f"p-value: {p:.4f}")
                        if p > 0.05:
                            st.success("Looks Normal")
                        else:
                            st.error("Not Normal")
                
                with col1:
                    # Hist + KDE
                    import plotly.figure_factory as ff
                    if len(series.unique()) > 1:
                        try:
                            fig_hist = ff.create_distplot([series], [selected_col], show_hist=True, show_rug=False)
                            style_figure(fig_hist)
                            st.plotly_chart(fig_hist, use_container_width=True, config=CHART_CONFIG)
                        except Exception:
                            fig_hist = px.histogram(series, x=series.name, marginal="box")
                            style_figure(fig_hist)
                            st.plotly_chart(fig_hist, use_container_width=True, config=CHART_CONFIG)
                    else:
                        st.info("Constant value column.")
                    
                    show_violin = st.checkbox("Show Violin Plot")
                    if show_violin:
                        fig_box = px.violin(series, x=series.name, box=True, points="all")
                    else:
                        fig_box = px.box(series, x=series.name, points="all")
                        
                    style_figure(fig_box)
                    st.plotly_chart(fig_box, use_container_width=True, config=CHART_CONFIG)
                    
                    # QQ Plot
                    if len(series.unique()) > 1:
                        osm, osr = stats.probplot(series, dist="norm")
                        fig_qq = px.scatter(x=osm[0], y=osm[1], labels={'x': 'Theoretical Quantiles', 'y': 'Sample Quantiles'}, title="Q-Q Plot")
                        # add reference line
                        m, b = np.polyfit(osm[0], osm[1], 1)
                        fig_qq.add_trace(go.Scatter(x=osm[0], y=m*osm[0] + b, mode='lines', name='Fit'))
                        style_figure(fig_qq)
                        st.plotly_chart(fig_qq, use_container_width=True, config=CHART_CONFIG)
                        
                st.markdown(glass_container_end(), unsafe_allow_html=True)
                
            else:
                # Categorical Analysis
                st.markdown(glass_container_start(), unsafe_allow_html=True)
                col1, col2 = st.columns([2, 1])
                
                val_counts = series.value_counts()
                
                with col1:
                    fig_bar = px.bar(x=val_counts.head(20).index, y=val_counts.head(20).values, labels={'x': selected_col, 'y': 'Count'}, title="Top 20 Value Counts")
                    style_figure(fig_bar)
                    st.plotly_chart(fig_bar, use_container_width=True, config=CHART_CONFIG)
                    
                    if len(val_counts) <= 10:
                        fig_pie = px.pie(names=val_counts.index, values=val_counts.values, hole=0.4, title="Distribution Proportions")
                        style_figure(fig_pie)
                        st.plotly_chart(fig_pie, use_container_width=True, config=CHART_CONFIG)
                        
                with col2:
                    pct = (val_counts / len(series)) * 100
                    df_counts = pd.DataFrame({'Count': val_counts, 'Percentage': pct.round(2)})
                    st.dataframe(df_counts)
                    
                st.markdown(glass_container_end(), unsafe_allow_html=True)

    with tabs[1]:
        st.subheader("All Columns Overview")
        cols = st.columns(2)
        
        for i, col_name in enumerate(all_cols):
            with cols[i % 2]:
                series = df[col_name].dropna()
                if len(series) == 0:
                    st.write(f"**{col_name}** - Empty")
                    continue
                    
                if col_name in num_cols and len(series.unique()) > 1:
                    fig = px.histogram(series, title=col_name, height=200)
                else:
                    vc = series.astype(str).value_counts().head(10)
                    fig = px.bar(x=vc.index, y=vc.values, title=col_name, height=200)
                    
                fig.update_layout(margin=dict(l=20, r=20, t=30, b=20), showlegend=False)
                style_figure(fig)
                st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)
