import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from scipy import stats as scipy_stats
from utils.helpers import (
    section_header_html, metric_card_html, badge_html,
    info_box_html, get_numeric_columns, get_categorical_columns,
    format_number,
)
from utils.plotting import style_figure, COLORS, CHART_CONFIG

def render(df: pd.DataFrame) -> None:
    """
    Render the Interactions analysis section.
    Provides pairwise variable analysis including scatter plots, pair plots,
    and categorical cross-tabulations.
    """
    st.markdown(section_header_html("Interactions", "Pairwise variable analysis"), unsafe_allow_html=True)
    
    if df.empty or len(df.columns) < 2:
        st.markdown(info_box_html("Not enough data or columns to analyze interactions. Require at least 2 columns."), unsafe_allow_html=True)
        return

    num_cols = get_numeric_columns(df)
    cat_cols = get_categorical_columns(df)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(metric_card_html("🔢", str(len(num_cols)), "Numeric Columns"), unsafe_allow_html=True)
    with col2:
        st.markdown(metric_card_html("🏷️", str(len(cat_cols)), "Categorical Columns"), unsafe_allow_html=True)
    with col3:
        total_cols = len(df.columns)
        total_pairs = (total_cols * (total_cols - 1)) // 2
        st.markdown(metric_card_html("🔗", format_number(total_pairs), "Total Pairs"), unsafe_allow_html=True)

    # Tabs
    tab_names = []
    has_num_num = len(num_cols) >= 2
    has_num_cat = len(num_cols) >= 1 and len(cat_cols) >= 1
    has_cat_cat = len(cat_cols) >= 2
    
    if has_num_num:
        tab_names.extend(["Scatter Explorer", "Pair Plot"])
    if has_num_cat:
        tab_names.append("Num vs Cat")
    if has_cat_cat:
        tab_names.append("Cat vs Cat")
        
    if not tab_names:
        st.markdown(info_box_html("No valid interactions possible with current column types."), unsafe_allow_html=True)
        return
        
    tabs = st.tabs(tab_names)
    tab_idx = 0
    
    # Optional sampling for large datasets
    plot_df = df
    max_scatter_points = 5000
    if len(df) > max_scatter_points:
        plot_df = df.sample(max_scatter_points, random_state=42)
        st.info(f"Dataset has >{max_scatter_points} rows. Scatter plots are using a random sample of {max_scatter_points} points.")

    if has_num_num:
        with tabs[tab_idx]:
            st.markdown("### Scatter Explorer")
            scat_col1, scat_col2, scat_col3, scat_col4 = st.columns([1, 1, 1, 1])
            with scat_col1:
                x_col = st.selectbox("X-Axis", num_cols, index=0, key="scat_x")
            with scat_col2:
                y_col = st.selectbox("Y-Axis", num_cols, index=1 if len(num_cols) > 1 else 0, key="scat_y")
            with scat_col3:
                color_opts = ["None"] + cat_cols
                color_col = st.selectbox("Color By", color_opts, index=0, key="scat_color")
            with scat_col4:
                show_trend = st.checkbox("Show Trendline (OLS)", value=False)
                
            color_arg = color_col if color_col != "None" else None
            trend_arg = "ols" if show_trend else None
            
            try:
                fig = px.scatter(
                    plot_df, x=x_col, y=y_col, color=color_arg,
                    marginal_x="histogram", marginal_y="histogram",
                    trendline=trend_arg,
                    color_discrete_sequence=COLORS
                )
                style_figure(fig)
                st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)
            except Exception as e:
                st.error(f"Error generating scatter plot: {e}. If using trendline, install 'statsmodels'.")
                
        tab_idx += 1
        
        with tabs[tab_idx]:
            st.markdown("### Scatter Matrix (Pair Plot)")
            selected_cols = st.multiselect("Select columns", num_cols, default=num_cols[:min(4, len(num_cols))], key="splom_cols")
            splom_color = st.selectbox("Color By", ["None"] + cat_cols, index=0, key="splom_color")
            
            if len(selected_cols) > 6:
                st.warning("Selecting more than 6 columns might result in a cluttered plot.")
                
            if len(selected_cols) >= 2:
                color_arg = splom_color if splom_color != "None" else None
                try:
                    # Limit rows for splom strictly for performance
                    splom_df = plot_df if len(plot_df) <= 2000 else df.sample(2000, random_state=42)
                    
                    fig_splom = px.scatter_matrix(
                        splom_df, dimensions=selected_cols, color=color_arg,
                        color_discrete_sequence=COLORS
                    )
                    fig_splom.update_traces(diagonal_visible=False)
                    style_figure(fig_splom)
                    st.plotly_chart(fig_splom, use_container_width=True, config=CHART_CONFIG)
                except Exception as e:
                    st.error(f"Error generating pair plot: {e}")
            else:
                st.info("Select at least 2 columns to show the pair plot.")
                
        tab_idx += 1

    if has_num_cat:
        with tabs[tab_idx]:
            st.markdown("### Numeric vs Categorical")
            nc_col1, nc_col2, nc_col3 = st.columns([1, 1, 1])
            with nc_col1:
                nc_num = st.selectbox("Numeric Column", num_cols, key="nc_num")
            with nc_col2:
                nc_cat = st.selectbox("Categorical Column", cat_cols, key="nc_cat")
            with nc_col3:
                plot_type = st.radio("Plot Type", ["Box Plot", "Violin Plot", "Strip Plot"], horizontal=True)
                
            try:
                if plot_type == "Box Plot":
                    fig_nc = px.box(plot_df, x=nc_cat, y=nc_num, color=nc_cat, color_discrete_sequence=COLORS)
                elif plot_type == "Violin Plot":
                    fig_nc = px.violin(plot_df, x=nc_cat, y=nc_num, color=nc_cat, box=True, points="all", color_discrete_sequence=COLORS)
                else:
                    fig_nc = px.strip(plot_df, x=nc_cat, y=nc_num, color=nc_cat, color_discrete_sequence=COLORS)
                    
                style_figure(fig_nc)
                st.plotly_chart(fig_nc, use_container_width=True, config=CHART_CONFIG)
                
                # ANOVA hint / summary
                st.markdown("#### Summary by Category")
                summary_df = df.groupby(nc_cat)[nc_num].agg(['count', 'mean', 'median', 'std', 'min', 'max']).reset_index()
                st.dataframe(summary_df, use_container_width=True)
                
            except Exception as e:
                st.error(f"Error generating numeric vs categorical plot: {e}")
                
        tab_idx += 1
        
    if has_cat_cat:
        with tabs[tab_idx]:
            st.markdown("### Categorical vs Categorical")
            cc_col1, cc_col2 = st.columns(2)
            with cc_col1:
                cc_cat1 = st.selectbox("Categorical Column 1", cat_cols, index=0, key="cc_cat1")
            with cc_col2:
                cc_cat2 = st.selectbox("Categorical Column 2", cat_cols, index=1 if len(cat_cols) > 1 else 0, key="cc_cat2")
                
            try:
                crosstab = pd.crosstab(df[cc_cat1], df[cc_cat2])
                
                # Heatmap
                fig_heat = px.imshow(crosstab, text_auto=True, aspect="auto", 
                                     labels=dict(x=cc_cat2, y=cc_cat1, color="Count"),
                                     color_continuous_scale="Blues")
                style_figure(fig_heat)
                st.plotly_chart(fig_heat, use_container_width=True, config=CHART_CONFIG)
                
                # Proportions (Stacked Bar)
                crosstab_prop = crosstab.div(crosstab.sum(axis=1), axis=0).reset_index()
                crosstab_melted = crosstab_prop.melt(id_vars=cc_cat1, value_name='Proportion')
                
                fig_bar = px.bar(crosstab_melted, x=cc_cat1, y='Proportion', color=cc_cat2, barmode='stack', color_discrete_sequence=COLORS)
                style_figure(fig_bar)
                st.plotly_chart(fig_bar, use_container_width=True, config=CHART_CONFIG)
                
                # Cramér's V
                chi2 = scipy_stats.chi2_contingency(crosstab)[0]
                n = crosstab.sum().sum()
                min_dim = min(crosstab.shape) - 1
                if min_dim > 0 and n > 0:
                    cramer_v = np.sqrt(chi2 / (n * min_dim))
                    st.markdown(f"**Cramér's V (Association):** {cramer_v:.4f}")
                
            except Exception as e:
                st.error(f"Error generating categorical vs categorical analysis: {e}")
