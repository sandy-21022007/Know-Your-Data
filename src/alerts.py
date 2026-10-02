import pandas as pd
import numpy as np
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from scipy.stats import skew

from utils.helpers import (
    metric_card_html, badge_html, section_header_html,
    info_box_html, warning_box_html, success_box_html,
    get_numeric_columns, get_categorical_columns,
    classify_column, format_number, format_percentage,
)
from utils.plotting import style_figure, COLORS, CHART_CONFIG, get_colorscale

def generate_alerts(df: pd.DataFrame) -> list[dict]:
    """
    Scans the dataframe and returns a prioritized list of data quality alerts.
    """
    alerts = []
    
    if df.empty:
        return alerts

    n_rows = len(df)
    
    # 9. DUPLICATES
    try:
        n_dupes = df.duplicated().sum()
        if n_dupes > 0:
            pct_dupes = (n_dupes / n_rows) * 100
            severity = 'HIGH' if pct_dupes > 10 else ('MEDIUM' if pct_dupes > 1 else 'LOW')
            alerts.append({
                'type': 'DUPLICATES',
                'severity': severity,
                'column': None,
                'message': f"Dataset has {format_number(n_dupes)} duplicate rows ({format_percentage(pct_dupes)})",
                'details': f"Consider dropping duplicates unless row duplication is expected in your domain."
            })
    except Exception:
        pass

    num_cols = get_numeric_columns(df)
    cat_cols = get_categorical_columns(df)
    
    for col in df.columns:
        col_series = df[col]
        n_missing = col_series.isna().sum()
        pct_missing = (n_missing / n_rows) * 100
        
        # 1. MISSING
        if n_missing > 0:
            severity = 'HIGH' if pct_missing > 50 else ('MEDIUM' if pct_missing > 15 else 'LOW')
            alerts.append({
                'type': 'MISSING',
                'severity': severity,
                'column': col,
                'message': f"{col}: {format_percentage(pct_missing)} missing values ({format_number(n_missing)} rows)",
                'details': f"High missingness can affect analysis. Consider imputation or dropping the column."
            })
            
        valid_series = col_series.dropna()
        if valid_series.empty:
            continue
            
        n_unique = valid_series.nunique()
        pct_unique = (n_unique / len(valid_series)) * 100
        
        # 2. CONSTANT
        if n_unique == 1:
            alerts.append({
                'type': 'CONSTANT',
                'severity': 'HIGH',
                'column': col,
                'message': f"{col}: has constant value '{valid_series.iloc[0]}'",
                'details': f"Constant columns provide no variance and can often be safely dropped."
            })
            continue # Skip other value-based checks if constant
            
        # 14. UNIQUE
        if n_unique == len(valid_series) and len(valid_series) > 100:
            alerts.append({
                'type': 'UNIQUE',
                'severity': 'INFO',
                'column': col,
                'message': f"{col}: every value is unique",
                'details': f"This column might be an identifier or primary key."
            })
            
        is_numeric = col in num_cols
        is_cat = col in cat_cols
        
        if is_numeric:
            # 5. LOW_CARDINALITY
            if n_unique < 10 and len(valid_series) > 50:
                alerts.append({
                    'type': 'LOW_CARDINALITY',
                    'severity': 'INFO',
                    'column': col,
                    'message': f"{col}: low cardinality numeric ({n_unique} unique values)",
                    'details': f"Might be a categorical variable encoded as numbers."
                })
                
            # 7. SKEWED
            try:
                col_skew = skew(valid_series)
                if abs(col_skew) > 2:
                    alerts.append({
                        'type': 'SKEWED',
                        'severity': 'MEDIUM',
                        'column': col,
                        'message': f"{col}: highly skewed (skewness={col_skew:.2f})",
                        'details': f"Consider log-transforming if used in linear models."
                    })
            except Exception:
                pass
                
            # 8. ZEROS
            n_zeros = (valid_series == 0).sum()
            pct_zeros = (n_zeros / len(valid_series)) * 100
            if pct_zeros > 50:
                alerts.append({
                    'type': 'ZEROS',
                    'severity': 'MEDIUM',
                    'column': col,
                    'message': f"{col}: {format_percentage(pct_zeros)} zero values",
                    'details': f"Over half the values are zero. Check if this is structural or missing data."
                })
                
            # 11. INFINITE
            try:
                n_infs = np.isinf(valid_series).sum()
                if n_infs > 0:
                    alerts.append({
                        'type': 'INFINITE',
                        'severity': 'HIGH',
                        'column': col,
                        'message': f"{col}: contains {format_number(n_infs)} infinite values",
                        'details': f"Infinite values will break most machine learning models."
                    })
            except Exception:
                pass
                
            # 15. NEGATIVE_VALUES
            n_neg = (valid_series < 0).sum()
            pct_neg = (n_neg / len(valid_series)) * 100
            if pct_neg > 30:
                alerts.append({
                    'type': 'NEGATIVE_VALUES',
                    'severity': 'LOW',
                    'column': col,
                    'message': f"{col}: {format_percentage(pct_neg)} negative values",
                    'details': f"Ensure negative values are expected for this metric."
                })
                
            # 10. UNIFORM
            try:
                val_range = valid_series.max() - valid_series.min()
                if val_range > 0 and valid_series.std() > 0:
                    # Very rough heuristic for uniform
                    expected_std_uniform = val_range / np.sqrt(12)
                    if abs(valid_series.std() - expected_std_uniform) / expected_std_uniform < 0.1:
                        alerts.append({
                            'type': 'UNIFORM',
                            'severity': 'INFO',
                            'column': col,
                            'message': f"{col}: appears uniformly distributed",
                            'details': f"Standard deviation closely matches a theoretical uniform distribution."
                        })
            except Exception:
                pass
                
            # 16. MEMORY_INEFFICIENT (Rough check: float64 that could be float32, etc.)
            if valid_series.dtype == 'float64':
                alerts.append({
                    'type': 'MEMORY_INEFFICIENT',
                    'severity': 'INFO',
                    'column': col,
                    'message': f"{col}: uses float64",
                    'details': f"Could potentially be downcast to float32 to save memory."
                })
            elif valid_series.dtype == 'int64':
                alerts.append({
                    'type': 'MEMORY_INEFFICIENT',
                    'severity': 'INFO',
                    'column': col,
                    'message': f"{col}: uses int64",
                    'details': f"Could potentially be downcast to smaller integer types."
                })
                
        else:
            # 4. HIGH_CARDINALITY
            if pct_unique > 50 and n_unique > 100:
                alerts.append({
                    'type': 'HIGH_CARDINALITY',
                    'severity': 'MEDIUM',
                    'column': col,
                    'message': f"{col}: high cardinality ({format_number(n_unique)} unique values, {format_percentage(pct_unique)} of rows)",
                    'details': f"High cardinality categorical columns might need hashing, target encoding, or dropping."
                })
                
            # 13. IMBALANCED
            if n_unique > 1:
                top_val = valid_series.mode().iloc[0]
                pct_top = (valid_series == top_val).sum() / len(valid_series) * 100
                if pct_top > 80:
                    alerts.append({
                        'type': 'IMBALANCED',
                        'severity': 'MEDIUM',
                        'column': col,
                        'message': f"{col}: imbalanced - '{top_val}' appears in {format_percentage(pct_top)} of rows",
                        'details': f"Highly imbalanced categories might not provide useful signals."
                    })
                    
            # String specific checks
            if valid_series.dtype == 'object' or pd.api.types.is_string_dtype(valid_series):
                # 3. CONSTANT_LENGTH
                try:
                    lengths = valid_series.astype(str).str.len()
                    if lengths.nunique() == 1 and lengths.iloc[0] > 0:
                        alerts.append({
                            'type': 'CONSTANT_LENGTH',
                            'severity': 'INFO',
                            'column': col,
                            'message': f"{col}: all values have length {lengths.iloc[0]}",
                            'details': f"This suggests a fixed-format code or identifier."
                        })
                except Exception:
                    pass
                    
                # 12. TYPE_MISMATCH
                try:
                    pd.to_numeric(valid_series)
                    alerts.append({
                        'type': 'TYPE_MISMATCH',
                        'severity': 'MEDIUM',
                        'column': col,
                        'message': f"{col}: stored as text but looks like numeric",
                        'details': f"Consider converting to numeric for proper analysis."
                    })
                except Exception:
                    try:
                        # try parse a subset to see if it's datetime
                        pd.to_datetime(valid_series.head(100))
                        alerts.append({
                            'type': 'TYPE_MISMATCH',
                            'severity': 'MEDIUM',
                            'column': col,
                            'message': f"{col}: stored as text but looks like datetime",
                            'details': f"Consider converting to datetime for time-series analysis."
                        })
                    except Exception:
                        pass
                        
    # 6. HIGH_CORRELATION
    if len(num_cols) > 1:
        try:
            corr_matrix = df[num_cols].corr()
            # Get upper triangle
            upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
            for i in range(len(upper.columns)):
                for j in range(i+1, len(upper.columns)):
                    col1 = upper.columns[i]
                    col2 = upper.columns[j]
                    val = upper.iloc[i, j]
                    if pd.notna(val) and abs(val) > 0.9:
                        alerts.append({
                            'type': 'HIGH_CORRELATION',
                            'severity': 'HIGH',
                            'column': f"{col1} & {col2}",
                            'message': f"{col1} & {col2}: highly correlated (r={val:.3f})",
                            'details': f"Highly correlated features provide redundant information and can cause multicollinearity."
                        })
        except Exception:
            pass

    return alerts

def get_alert_color(severity: str) -> str:
    return {
        'HIGH': '#ff1744',
        'MEDIUM': '#ff6d00',
        'LOW': '#ffc400',
        'INFO': '#00d2ff'
    }.get(severity, '#888888')

def calculate_quality_score(alerts: list[dict]) -> int:
    score = 100
    for alert in alerts:
        sev = alert.get('severity', 'INFO')
        if sev == 'HIGH':
            score -= 15
        elif sev == 'MEDIUM':
            score -= 5
        elif sev == 'LOW':
            score -= 2
    return max(0, score)

def render(df: pd.DataFrame) -> None:
    """
    Renders the Data Quality Alerts dashboard.
    """
    st.markdown(section_header_html("Data Quality Alerts", "Automated anomaly & issue detection"), unsafe_allow_html=True)
    
    with st.spinner("Scanning for data quality issues..."):
        alerts = generate_alerts(df)
        
    if not alerts:
        st.markdown(success_box_html("🎉 Your dataset looks great! No data quality issues detected."), unsafe_allow_html=True)
        return
        
    # Categorize alerts
    high_alerts = [a for a in alerts if a['severity'] == 'HIGH']
    medium_alerts = [a for a in alerts if a['severity'] == 'MEDIUM']
    low_alerts = [a for a in alerts if a['severity'] == 'LOW']
    info_alerts = [a for a in alerts if a['severity'] == 'INFO']
    
    # Summary Bar
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown(metric_card_html("High Priority 🔴", str(len(high_alerts))), unsafe_allow_html=True)
    c2.markdown(metric_card_html("Medium Priority 🟠", str(len(medium_alerts))), unsafe_allow_html=True)
    c3.markdown(metric_card_html("Low Priority 🟡", str(len(low_alerts))), unsafe_allow_html=True)
    c4.markdown(metric_card_html("Info / Notes 🔵", str(len(info_alerts))), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    col_score, col_list = st.columns([1, 2])
    
    with col_score:
        score = calculate_quality_score(alerts)
        color = "#00c853"
        if score < 40:
            color = "#ff1744"
        elif score < 60:
            color = "#ff6d00"
        elif score < 80:
            color = "#ffc400"
        elif score < 90:
            color = "#00d2ff"
            
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=score,
            title={'text': "Data Quality Score", 'font': {'size': 20, 'color': 'white'}},
            gauge={
                'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "white"},
                'bar': {'color': color},
                'bgcolor': "rgba(0,0,0,0)",
                'borderwidth': 0,
                'steps': [
                    {'range': [0, 40], 'color': 'rgba(255, 23, 68, 0.2)'},
                    {'range': [40, 60], 'color': 'rgba(255, 109, 0, 0.2)'},
                    {'range': [60, 80], 'color': 'rgba(255, 196, 0, 0.2)'},
                    {'range': [80, 90], 'color': 'rgba(0, 210, 255, 0.2)'},
                    {'range': [90, 100], 'color': 'rgba(0, 200, 83, 0.2)'},
                ]
            }
        ))
        style_figure(fig)
        fig.update_layout(height=350, margin=dict(l=20, r=20, t=50, b=20))
        st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)
        
    with col_list:
        st.markdown("### 📋 Alert List")
        # Sort alerts by severity
        severity_order = {'HIGH': 0, 'MEDIUM': 1, 'LOW': 2, 'INFO': 3}
        sorted_alerts = sorted(alerts, key=lambda x: (severity_order.get(x['severity'], 4), x['type']))
        
        for idx, alert in enumerate(sorted_alerts):
            sev_color = get_alert_color(alert['severity'])
            
            # Simple card layout using markdown
            html = f"""
            <div style="border-left: 5px solid {sev_color}; padding: 10px; margin-bottom: 10px; background-color: rgba(255,255,255,0.05); border-radius: 4px;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 5px;">
                    <strong>{badge_html(alert['severity'], sev_color)} <span style="color:#ddd; margin-left:10px;">{alert['type']}</span></strong>
                </div>
                <div style="font-size: 1.1em; color: white; margin-bottom: 5px;">{alert['message']}</div>
            """
            st.markdown(html, unsafe_allow_html=True)
            with st.expander("Details"):
                st.write(alert['details'])
                if alert['column']:
                    st.caption(f"Column: {alert['column']}")
            st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # Heatmap of alerts by column
    st.markdown("### 🔍 Alerts by Column")
    # Exclude non-column alerts (like duplicates)
    col_alerts = [a for a in alerts if a['column'] and ' & ' not in a['column']]
    
    if col_alerts:
        heatmap_data = []
        for a in col_alerts:
            heatmap_data.append({'Column': a['column'], 'Alert Type': a['type'], 'Count': 1})
            
        if heatmap_data:
            hm_df = pd.DataFrame(heatmap_data)
            hm_pivot = hm_df.pivot_table(index='Column', columns='Alert Type', values='Count', aggfunc='sum').fillna(0)
            
            fig2 = px.imshow(
                hm_pivot, 
                text_auto=True, 
                aspect="auto",
                color_continuous_scale="Blues"
            )
            style_figure(fig2)
            fig2.update_layout(height=max(400, len(hm_pivot) * 30))
            st.plotly_chart(fig2, use_container_width=True, config=CHART_CONFIG)
    else:
        st.info("No column-specific alerts found.")
