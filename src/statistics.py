"""Statistical summary module."""

import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
from scipy.stats import skew, kurtosis, entropy

from utils.helpers import (
    format_number, get_numeric_columns, get_categorical_columns,
    metric_card_html, badge_html, section_header_html,
    glass_container_start, glass_container_end,
)
from utils.plotting import CHART_CONFIG, style_figure, COLORS

def render(df: pd.DataFrame) -> None:
    """Render statistical summary."""
    st.markdown(section_header_html("Statistical Summary", "Detailed descriptive statistics"), unsafe_allow_html=True)
    
    if df.empty:
        st.warning("Dataset is empty.")
        return

    tabs = st.tabs(["Numeric", "Categorical", "Full Summary"])
    
    num_cols = get_numeric_columns(df)
    cat_cols = get_categorical_columns(df)
    
    with tabs[0]:
        if not num_cols:
            st.info("No numeric columns found.")
        else:
            avg_mean = np.nanmean([df[c].mean() for c in num_cols])
            avg_std = np.nanmean([df[c].std() for c in num_cols])
            
            mc1, mc2, mc3 = st.columns(3)
            with mc1:
                st.markdown(metric_card_html("Numeric Columns", str(len(num_cols)), "#️⃣"), unsafe_allow_html=True)
            with mc2:
                st.markdown(metric_card_html("Avg Mean", format_number(avg_mean), "📈"), unsafe_allow_html=True)
            with mc3:
                st.markdown(metric_card_html("Avg Std Dev", format_number(avg_std), "📉"), unsafe_allow_html=True)
                
            for col in num_cols:
                series = df[col].dropna()
                if len(series) == 0:
                    continue
                
                st.markdown(glass_container_start(), unsafe_allow_html=True)
                st.subheader(col)
                
                c1, c2, c3, c4, c5 = st.columns(5)
                c1.metric("Mean", format_number(series.mean()))
                c2.metric("Median", format_number(series.median()))
                c3.metric("Std Dev", format_number(series.std()))
                c4.metric("Min", format_number(series.min()))
                c5.metric("Max", format_number(series.max()))
                
                s = skew(series)
                k = kurtosis(series)
                q1 = series.quantile(0.25)
                q3 = series.quantile(0.75)
                iqr = q3 - q1
                cv = (series.std() / series.mean()) if series.mean() != 0 else np.nan
                
                if abs(s) <= 0.5:
                    skew_badge = badge_html("Symmetric", "success")
                elif abs(s) <= 1:
                    skew_badge = badge_html("Moderate", "warning")
                else:
                    skew_badge = badge_html("High", "error")
                
                st.markdown(f"**Skewness:** {format_number(s)} {skew_badge} | **Kurtosis:** {format_number(k)} | **Q1:** {format_number(q1)} | **Q3:** {format_number(q3)} | **IQR:** {format_number(iqr)} | **CV:** {format_number(cv)}", unsafe_allow_html=True)
                
                fig = px.histogram(series, nbins=30)
                fig.update_layout(height=50, margin=dict(l=0, r=0, t=0, b=0), showlegend=False, 
                                  xaxis=dict(visible=False), yaxis=dict(visible=False),
                                  plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)')
                st.plotly_chart(fig, use_container_width=True, config=dict(displayModeBar=False))
                
                st.markdown(glass_container_end(), unsafe_allow_html=True)

    with tabs[1]:
        if not cat_cols:
            st.info("No categorical columns found.")
        else:
            for col in cat_cols:
                series = df[col].dropna().astype(str)
                if len(series) == 0:
                    continue
                
                st.markdown(glass_container_start(), unsafe_allow_html=True)
                st.subheader(col)
                
                val_counts = series.value_counts()
                n_unique = len(val_counts)
                mode_val = val_counts.index[0] if n_unique > 0 else "N/A"
                mode_freq = val_counts.iloc[0] if n_unique > 0 else 0
                
                prob = val_counts / len(series)
                ent = entropy(prob)
                
                st.write(f"**Unique values:** {n_unique} | **Mode:** {mode_val} | **Mode frequency:** {mode_freq} | **Entropy:** {format_number(ent)}")
                
                c1, c2 = st.columns(2)
                with c1:
                    top10 = val_counts.head(10)
                    fig = px.bar(x=top10.values, y=top10.index, orientation='h', labels={'x': 'Count', 'y': 'Value'})
                    fig.update_layout(yaxis={'categoryorder': 'total ascending'})
                    style_figure(fig)
                    st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)
                
                with c2:
                    if n_unique <= 15:
                        fig2 = px.pie(names=val_counts.index, values=val_counts.values, hole=0.4)
                        style_figure(fig2)
                        st.plotly_chart(fig2, use_container_width=True, config=CHART_CONFIG)
                
                st.markdown(glass_container_end(), unsafe_allow_html=True)

    with tabs[2]:
        st.subheader("Full Summary Statistics")
        desc = df.describe(include='all').T
        
        if num_cols:
            pcts = df[num_cols].quantile([0.01, 0.05, 0.95, 0.99]).T
            pcts.columns = ['1%', '5%', '95%', '99%']
            desc = desc.join(pcts)
            
        st.dataframe(desc, use_container_width=True)
