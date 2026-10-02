import streamlit as st
import pandas as pd
import plotly.express as px
from utils.helpers import (
    format_number, format_percentage, section_header_html, 
    success_box_html, metric_card_html, glass_container_start, glass_container_end
)
from utils.plotting import style_figure, CHART_CONFIG

def render(df: pd.DataFrame) -> None:
    """
    Render duplicate row detection module.
    """
    st.markdown(section_header_html("Duplicate Detection", "Identify and analyze duplicate rows and values"), unsafe_allow_html=True)
    
    total_rows = len(df)
    duplicates_mask = df.duplicated(keep=False)
    duplicate_rows = duplicates_mask.sum()
    dup_rate = duplicate_rows / total_rows if total_rows > 0 else 0
    
    st.markdown(glass_container_start(), unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(metric_card_html("Total Rows", format_number(total_rows), "📊"), unsafe_allow_html=True)
    with col2:
        st.markdown(metric_card_html("Duplicate Rows", format_number(duplicate_rows), "📑"), unsafe_allow_html=True)
    with col3:
        st.markdown(metric_card_html("Duplication Rate", format_percentage(dup_rate), "📈"), unsafe_allow_html=True)
    st.markdown(glass_container_end(), unsafe_allow_html=True)
    
    if duplicate_rows == 0:
        st.markdown(success_box_html("No duplicate rows found! Your dataset is clean."), unsafe_allow_html=True)
    else:
        st.subheader("Duplicate Rows Preview")
        st.markdown(f"Showing duplicate rows (max 100 out of {duplicate_rows})")
        dupes_df = df[duplicates_mask].sort_values(by=list(df.columns))
        st.dataframe(dupes_df.head(100), use_container_width=True)
        
    st.subheader("Column-wise Duplicate Analysis")
    st.markdown("Number of non-unique (duplicate) values per column.")
    
    col_dupes = []
    for col in df.columns:
        dupes_in_col = len(df) - df[col].nunique(dropna=False)
        col_dupes.append({"Column": col, "Duplicate Values": dupes_in_col})
        
    col_dupes_df = pd.DataFrame(col_dupes).sort_values("Duplicate Values", ascending=True)
    
    fig = px.bar(
        col_dupes_df, 
        x="Duplicate Values", 
        y="Column", 
        orientation='h',
        title="Duplicate Values by Column"
    )
    style_figure(fig)
    st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)
    
    st.subheader("Subset Duplicate Check")
    subset_cols = st.multiselect("Select columns to check for duplicates", df.columns.tolist())
    
    if subset_cols:
        subset_dupes_mask = df.duplicated(subset=subset_cols, keep=False)
        subset_dupes_count = subset_dupes_mask.sum()
        
        if subset_dupes_count == 0:
            st.markdown(success_box_html(f"No duplicates found using subset: {', '.join(subset_cols)}"), unsafe_allow_html=True)
        else:
            st.warning(f"Found {subset_dupes_count} duplicate rows using the selected subset.")
            st.dataframe(df[subset_dupes_mask].sort_values(by=subset_cols).head(100), use_container_width=True)
