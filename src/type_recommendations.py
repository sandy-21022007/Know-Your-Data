import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils.helpers import (
    format_number, format_bytes, format_percentage, section_header_html, success_box_html,
    metric_card_html, badge_html, glass_container_start, glass_container_end
)
from utils.plotting import style_figure, CHART_CONFIG

def render(df: pd.DataFrame) -> None:
    """
    Render data type recommendations module.
    """
    st.markdown(section_header_html("Data Type Recommendations", "Optimize memory usage with better data types"), unsafe_allow_html=True)
    
    if df.empty:
        st.info("Dataset is empty.")
        return
        
    recommendations = []
    total_savings = 0
    
    memory_before = df.memory_usage(deep=True)
    
    for col in df.columns:
        current_dtype = df[col].dtype
        mem_before = memory_before[col]
        suggested_dtype = None
        reason = ""
        
        # Check object types
        if current_dtype == 'object':
            # Check for datetime
            try:
                # Try on a sample first
                sample = df[col].dropna().head(100)
                if not sample.empty:
                    pd.to_datetime(sample, format="mixed")
                    # If it works on sample, test the whole column
                    pd.to_datetime(df[col], format="mixed")
                    suggested_dtype = "datetime64[ns]"
                    reason = "Contains date/time formatted strings"
            except:
                pass
                
            if not suggested_dtype:
                # Check for category
                nunique = df[col].nunique()
                nrows = len(df[col].dropna())
                if nrows > 0 and nunique / nrows < 0.5:
                    suggested_dtype = "category"
                    reason = "Low cardinality string column"
                    
            if not suggested_dtype:
                # Check for numeric disguised as string
                try:
                    sample = df[col].dropna().head(100)
                    if not sample.empty:
                        pd.to_numeric(sample)
                        suggested_dtype = "numeric"
                        reason = "Strings containing numeric values"
                except:
                    pass
                    
        # Check int types
        elif pd.api.types.is_integer_dtype(current_dtype):
            if df[col].isna().any():
                suggested_dtype = "Int64"
                reason = "Integer with null values (use pandas nullable int)"
            elif current_dtype == 'int64':
                min_val = df[col].min()
                max_val = df[col].max()
                
                if min_val >= np.iinfo(np.int8).min and max_val <= np.iinfo(np.int8).max:
                    suggested_dtype = "int8"
                elif min_val >= np.iinfo(np.int16).min and max_val <= np.iinfo(np.int16).max:
                    suggested_dtype = "int16"
                elif min_val >= np.iinfo(np.int32).min and max_val <= np.iinfo(np.int32).max:
                    suggested_dtype = "int32"
                    
                if suggested_dtype:
                    reason = f"Values fit in {suggested_dtype} range"
                    
        # Check float types
        elif pd.api.types.is_float_dtype(current_dtype):
            if current_dtype == 'float64':
                # Simplified check for float32 compatibility
                suggested_dtype = "float32"
                reason = "Often sufficient precision, uses half memory"
                
        if suggested_dtype:
            # Estimate savings
            if suggested_dtype == "category":
                # Roughly num_categories * 8 bytes + num_rows * 1-4 bytes
                est_mem_after = df[col].nunique() * 8 + len(df) * 2 
            elif suggested_dtype in ["int8"]:
                est_mem_after = len(df) * 1
            elif suggested_dtype in ["int16"]:
                est_mem_after = len(df) * 2
            elif suggested_dtype in ["int32", "float32"]:
                est_mem_after = len(df) * 4
            elif suggested_dtype == "datetime64[ns]":
                est_mem_after = len(df) * 8
            else:
                est_mem_after = mem_before * 0.8 # Rough guess
                
            savings = max(0, mem_before - est_mem_after)
            if savings > 0:
                recommendations.append({
                    "Column": col,
                    "Current Type": str(current_dtype),
                    "Suggested Type": suggested_dtype,
                    "Reason": reason,
                    "Savings Bytes": savings,
                    "Current Bytes": mem_before,
                    "Suggested Bytes": est_mem_after
                })
                total_savings += savings
                
    st.markdown(glass_container_start(), unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(metric_card_html("🛠️", str(len(recommendations)), "Columns to Optimize"), unsafe_allow_html=True)
    
    pct_savings = (total_savings / memory_before.sum() * 100) if memory_before.sum() > 0 else 0
    with col2:
        st.markdown(metric_card_html("💾", f"{format_bytes(total_savings)} ({format_percentage(pct_savings)})", "Est. Memory Savings"), unsafe_allow_html=True)
    st.markdown(glass_container_end(), unsafe_allow_html=True)
    
    if not recommendations:
        st.markdown(success_box_html("All columns are already using optimal data types!"), unsafe_allow_html=True)
        return
        
    st.subheader("Recommendations")
    
    html = "<table class='stat-table'><thead><tr><th>Column</th><th>Current Type</th><th>Suggested Type</th><th>Reason</th><th>Est. Savings</th></tr></thead><tbody>"
    for rec in recommendations:
        curr = badge_html(rec['Current Type'], "warning")
        sugg = badge_html(rec['Suggested Type'], "success")
        sav = format_bytes(rec['Savings Bytes'])
        html += f"<tr><td>{rec['Column']}</td><td>{curr}</td><td>{sugg}</td><td>{rec['Reason']}</td><td>{sav}</td></tr>"
    html += "</tbody></table>"
    st.markdown(html, unsafe_allow_html=True)
    
    st.subheader("Memory Comparison")
    
    plot_data = []
    for rec in recommendations:
        plot_data.append({
            "Column": rec['Column'],
            "Memory (Bytes)": rec['Current Bytes'],
            "State": "Current"
        })
        plot_data.append({
            "Column": rec['Column'],
            "Memory (Bytes)": rec['Suggested Bytes'],
            "State": "Optimized"
        })
        
    df_plot = pd.DataFrame(plot_data)
    
    fig = px.bar(
        df_plot,
        x="Column",
        y="Memory (Bytes)",
        color="State",
        barmode="group",
        title="Memory Usage: Current vs Optimized"
    )
    style_figure(fig)
    st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)
