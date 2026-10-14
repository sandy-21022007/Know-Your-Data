"""Data overview module showing comprehensive dataset summary."""

import pandas as pd
import streamlit as st
import plotly.express as px

from utils.helpers import (
    format_number, format_percentage, format_bytes,
    classify_column, get_numeric_columns, get_categorical_columns, get_datetime_columns,
    get_column_icon,
    metric_card_html, progress_bar_html, badge_html,
    section_header_html, divider_html,
    info_box_html, warning_box_html, success_box_html,
    glass_container_start, glass_container_end,
)

from utils.plotting import (
    COLORS, GRADIENT_PAIR, CHART_CONFIG, DEFAULT_LAYOUT,
    create_figure, style_figure, get_color, get_colorscale,
)

def render(df: pd.DataFrame) -> None:
    """Render the overview section."""
    if df is None or df.empty:
        st.warning("No data available.")
        return
        
    st.markdown(section_header_html("Data Overview", "High-level summary of your dataset"), unsafe_allow_html=True)
    
    # 1. Top metric cards row
    total_rows = df.shape[0]
    total_cols = df.shape[1]
    memory_usage = df.memory_usage(deep=True).sum()
    duplicate_rows = df.duplicated().sum()
    
    cols = st.columns(4)
    cols[0].markdown(metric_card_html("📊", format_number(total_rows), "Total Rows"), unsafe_allow_html=True)
    cols[1].markdown(metric_card_html("📋", format_number(total_cols), "Total Columns"), unsafe_allow_html=True)
    cols[2].markdown(metric_card_html("💾", format_bytes(memory_usage), "Memory Usage"), unsafe_allow_html=True)
    cols[3].markdown(metric_card_html("📑", format_number(duplicate_rows), "Duplicate Rows"), unsafe_allow_html=True)
    
    st.markdown(divider_html(), unsafe_allow_html=True)
    
    # 2. Data Types Summary
    st.markdown(glass_container_start(), unsafe_allow_html=True)
    st.subheader("Data Types Summary")
    
    dtype_counts = df.dtypes.value_counts().reset_index()
    dtype_counts.columns = ['Data Type', 'Count']
    dtype_counts['Data Type'] = dtype_counts['Data Type'].astype(str)
    
    fig = px.bar(
        dtype_counts, 
        y='Data Type', 
        x='Count', 
        orientation='h',
        color='Data Type',
        color_discrete_sequence=COLORS,
        title="Columns by Data Type"
    )
    fig = style_figure(fig)
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)
        
    with col2:
        num_cols = len(get_numeric_columns(df))
        cat_cols = len(get_categorical_columns(df))
        date_cols = len(get_datetime_columns(df))
        
        st.markdown(metric_card_html("🔢", format_number(num_cols), "Numeric"), unsafe_allow_html=True)
        st.markdown(metric_card_html("🔤", format_number(cat_cols), "Categorical"), unsafe_allow_html=True)
        st.markdown(metric_card_html("📅", format_number(date_cols), "Datetime"), unsafe_allow_html=True)
    
    st.markdown(glass_container_end(), unsafe_allow_html=True)
    st.markdown(divider_html(), unsafe_allow_html=True)
    
    # 3. Column Details Table
    # 3. Column Details Table
    st.subheader("Column Details")
    
    rows = []
    for col in df.columns:
        dtype_str = str(df[col].dtype)
        non_null = df[col].count()
        null_count = df[col].isnull().sum()
        null_pct = (null_count / total_rows) * 100 if total_rows > 0 else 0
        unique_vals = df[col].nunique(dropna=True)
        
        sample_val = ""
        if non_null > 0:
            sample_idx = df[col].first_valid_index()
            if sample_idx is not None:
                sample_val = str(df.loc[sample_idx, col])
                if len(sample_val) > 30:
                    sample_val = sample_val[:27] + "..."
                    
        type_class = classify_column(df[col])
        icon = get_column_icon(type_class)
        prog_bar = progress_bar_html(null_pct, 'error' if null_pct > 50 else ('warning' if null_pct > 0 else 'success'))
        badge = badge_html(dtype_str, type_class, 'info')
        
        row_str = (
            f"<tr>"
            f"<td style='padding: 10px 14px;'><strong>{icon} {col}</strong></td>"
            f"<td style='padding: 10px 14px;'>{badge}</td>"
            f"<td style='text-align: right; padding: 10px 14px; font-family: var(--font-mono);'>{format_number(non_null)}</td>"
            f"<td style='padding: 10px 14px;'><div>{format_number(null_count)} ({format_percentage(null_pct)})</div>{prog_bar}</td>"
            f"<td style='text-align: right; padding: 10px 14px; font-family: var(--font-mono);'>{format_number(unique_vals)}</td>"
            f"<td style='padding: 10px 14px; font-family: var(--font-mono); color: #94A3B8;'>{sample_val}</td>"
            f"</tr>"
        )
        rows.append(row_str)
        
    table_html = (
        f"<div style='overflow-x: auto; margin-top: 10px; margin-bottom: 20px;'>"
        f"<table class='stat-table' style='width: 100%; border-collapse: separate; border-spacing: 0;'>"
        f"<thead><tr>"
        f"<th style='text-align: left;'>Column</th>"
        f"<th style='text-align: left;'>Type</th>"
        f"<th style='text-align: right;'>Non-Null</th>"
        f"<th style='text-align: left;'>Nulls</th>"
        f"<th style='text-align: right;'>Unique</th>"
        f"<th style='text-align: left;'>Sample</th>"
        f"</tr></thead>"
        f"<tbody>{''.join(rows)}</tbody>"
        f"</table></div>"
    )
    
    st.markdown(table_html, unsafe_allow_html=True)
    st.markdown(divider_html(), unsafe_allow_html=True)
    
    # 4. Data Preview
    st.subheader("Data Preview")
    tab1, tab2, tab3 = st.tabs(["First Rows", "Last Rows", "Random Sample"])
    
    with tab1:
        st.dataframe(df.head(), use_container_width=True)
    with tab2:
        st.dataframe(df.tail(), use_container_width=True)
    with tab3:
        if len(df) > 5:
            st.dataframe(df.sample(5), use_container_width=True)
        else:
            st.dataframe(df, use_container_width=True)
            
    # 5. Shape & Memory Info Box
    with st.expander("Detailed Shape & Memory Info"):
        st.markdown(info_box_html(
            f"Dataset dimensions: <strong>{total_rows}</strong> rows × <strong>{total_cols}</strong> columns<br>"
            f"Total elements: <strong>{format_number(total_rows * total_cols)}</strong><br>"
            f"Total memory usage: <strong>{format_bytes(memory_usage)}</strong>"
        ), unsafe_allow_html=True)
