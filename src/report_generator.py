"""
Report Generator module for Know-Your-Data.
"""
import streamlit as st
import pandas as pd
import datetime
import io
import plotly.express as px
from utils.helpers import (
    section_header_html, metric_card_html, get_numeric_columns, 
    get_categorical_columns, glass_container_start, glass_container_end,
    success_box_html
)

def _generate_overview_section(df: pd.DataFrame) -> str:
    html = "<div class='section'><h2>Data Overview</h2>"
    
    rows, cols = df.shape
    num_cols = len(get_numeric_columns(df))
    cat_cols = len(get_categorical_columns(df))
    missing_total = df.isna().sum().sum()
    dup_rows = df.duplicated().sum()
    
    html += "<div class='metrics'>"
    html += f"<div class='metric'><strong>Rows:</strong> {rows}</div>"
    html += f"<div class='metric'><strong>Columns:</strong> {cols}</div>"
    html += f"<div class='metric'><strong>Numeric:</strong> {num_cols}</div>"
    html += f"<div class='metric'><strong>Categorical:</strong> {cat_cols}</div>"
    html += f"<div class='metric'><strong>Missing Cells:</strong> {missing_total}</div>"
    html += f"<div class='metric'><strong>Duplicate Rows:</strong> {dup_rows}</div>"
    html += "</div>"
    
    html += "<h3>Head (First 5 Rows)</h3>"
    html += df.head().to_html(classes='data-table')
    html += "</div>"
    return html

def _generate_missing_section(df: pd.DataFrame) -> str:
    html = "<div class='section'><h2>Missing Values Analysis</h2>"
    missing = df.isna().sum()
    missing = missing[missing > 0].sort_values(ascending=False)
    
    if len(missing) == 0:
        html += "<p>No missing values found in the dataset.</p>"
    else:
        missing_df = pd.DataFrame({
            'Missing Count': missing,
            'Missing Percentage': (missing / len(df) * 100).round(2)
        })
        html += missing_df.to_html(classes='data-table')
        
        # Add simple bar chart using plotly
        fig = px.bar(x=missing.index, y=missing.values, labels={'x':'Column', 'y':'Missing Count'})
        fig.update_layout(title="Missing Values by Column")
        html += fig.to_html(include_plotlyjs=False, full_html=False)
        
    html += "</div>"
    return html

def _generate_statistics_section(df: pd.DataFrame) -> str:
    html = "<div class='section'><h2>Statistical Summary</h2>"
    num_cols = get_numeric_columns(df)
    if num_cols:
        html += "<h3>Numeric Columns</h3>"
        html += df[num_cols].describe().T.to_html(classes='data-table')
    cat_cols = get_categorical_columns(df)
    if cat_cols:
        html += "<h3>Categorical Columns</h3>"
        html += df[cat_cols].describe().T.to_html(classes='data-table')
    html += "</div>"
    return html

def _generate_correlation_section(df: pd.DataFrame) -> str:
    html = "<div class='section'><h2>Correlation Analysis</h2>"
    num_cols = get_numeric_columns(df)
    if len(num_cols) > 1:
        corr = df[num_cols].corr()
        fig = px.imshow(corr, text_auto=True, aspect="auto")
        fig.update_layout(title="Correlation Matrix")
        html += fig.to_html(include_plotlyjs=False, full_html=False)
    else:
        html += "<p>Not enough numeric columns for correlation analysis.</p>"
    html += "</div>"
    return html

def _generate_duplicates_section(df: pd.DataFrame) -> str:
    html = "<div class='section'><h2>Duplicate Detection</h2>"
    dup_sum = df.duplicated().sum()
    html += f"<p>Number of duplicate rows: <strong>{dup_sum}</strong> ({(dup_sum/len(df)*100):.2f}%)</p>"
    if dup_sum > 0:
        html += "<h3>Sample Duplicate Rows</h3>"
        dupes_sample = df[df.duplicated(keep=False)]
        try:
            dupes_sample = dupes_sample.sort_values(by=list(df.columns))
        except Exception:
            pass
        html += dupes_sample.head(10).to_html(classes='data-table')
    html += "</div>"
    return html

def _generate_outliers_section(df: pd.DataFrame) -> str:
    html = "<div class='section'><h2>Outlier Analysis</h2>"
    num_cols = get_numeric_columns(df)
    if num_cols:
        html += "<p>Outliers detected using IQR method (1.5 * IQR).</p>"
        outliers_data = []
        for col in num_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
            if not outliers.empty:
                outliers_data.append({
                    "Column": col,
                    "Outliers Count": len(outliers),
                    "% Outliers": round(len(outliers) / len(df) * 100, 2)
                })
        
        if outliers_data:
            outliers_df = pd.DataFrame(outliers_data)
            html += outliers_df.to_html(classes='data-table', index=False)
        else:
            html += "<p>No outliers found.</p>"
    else:
        html += "<p>No numeric columns available.</p>"
    html += "</div>"
    return html

def _generate_type_section(df: pd.DataFrame) -> str:
    html = "<div class='section'><h2>Type Recommendations</h2>"
    html += "<p>Current memory usage: <strong>" + f"{df.memory_usage(deep=True).sum() / (1024*1024):.2f} MB" + "</strong></p>"
    types_df = pd.DataFrame({
        'Column': df.columns,
        'Current Type': df.dtypes.astype(str)
    })
    html += types_df.to_html(classes='data-table', index=False)
    html += "</div>"
    return html


def generate_html_report(df: pd.DataFrame, sections: dict) -> str:
    """Generate the complete self-contained HTML report."""
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>EDA Report - Know Your Data</title>
        <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
        <style>
            :root {{
                --bg-color: #0e1117;
                --text-color: #e2e8f0;
                --card-bg: #1e2532;
                --primary: #667eea;
                --border: #2d3748;
            }}
            body {{
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
                background-color: var(--bg-color);
                color: var(--text-color);
                line-height: 1.6;
                padding: 20px;
                max-width: 1200px;
                margin: 0 auto;
            }}
            h1, h2, h3 {{ color: #ffffff; }}
            .header {{
                text-align: center;
                padding: 40px 20px;
                background: linear-gradient(135deg, rgba(102,126,234,0.1), rgba(118,75,162,0.1));
                border-radius: 12px;
                margin-bottom: 30px;
                border: 1px solid var(--border);
            }}
            .section {{
                background-color: var(--card-bg);
                border-radius: 12px;
                padding: 24px;
                margin-bottom: 24px;
                border: 1px solid var(--border);
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
            .metrics {{
                display: flex;
                flex-wrap: wrap;
                gap: 16px;
                margin-bottom: 20px;
            }}
            .metric {{
                background: rgba(255,255,255,0.05);
                padding: 12px 20px;
                border-radius: 8px;
                border: 1px solid var(--border);
            }}
            .data-table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                font-size: 0.9em;
            }}
            .data-table th, .data-table td {{
                padding: 12px 15px;
                border: 1px solid var(--border);
                text-align: left;
            }}
            .data-table th {{
                background-color: rgba(255,255,255,0.05);
                font-weight: 600;
            }}
            .data-table tr:nth-child(even) {{
                background-color: rgba(255,255,255,0.02);
            }}
        </style>
    </head>
    <body>
        <div class="header">
            <h1>📊 Know Your Data - EDA Report</h1>
            <p>Generated on {now}</p>
        </div>
    """
    
    if sections.get("overview", True): html += _generate_overview_section(df)
    if sections.get("missing", True): html += _generate_missing_section(df)
    if sections.get("statistics", True): html += _generate_statistics_section(df)
    if sections.get("correlations", True): html += _generate_correlation_section(df)
    if sections.get("duplicates", True): html += _generate_duplicates_section(df)
    if sections.get("outliers", True): html += _generate_outliers_section(df)
    if sections.get("types", True): html += _generate_type_section(df)
    
    html += """
    </body>
    </html>
    """
    return html

def render(df: pd.DataFrame) -> None:
    """Render the report generator interface."""
    st.markdown(section_header_html("Generate Report", "Export your analysis to a standalone HTML file"), unsafe_allow_html=True)
    
    st.markdown(glass_container_start(), unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("Select Sections to Include")
        
        # Organize in columns for compact view
        c1, c2 = st.columns(2)
        
        sections = {}
        with c1:
            sections["overview"] = st.checkbox("Data Overview", value=True)
            sections["missing"] = st.checkbox("Missing Values Analysis", value=True)
            sections["statistics"] = st.checkbox("Statistical Summary", value=True)
            sections["correlations"] = st.checkbox("Correlation Analysis", value=True)
            
        with c2:
            sections["duplicates"] = st.checkbox("Duplicate Detection", value=True)
            sections["outliers"] = st.checkbox("Outlier Analysis", value=True)
            sections["types"] = st.checkbox("Type Recommendations", value=True)
            
    with col2:
        st.subheader("Report Info")
        st.markdown(metric_card_html("📄", str(sum(sections.values())), "Selected Sections"), unsafe_allow_html=True)
        
        if st.button("Generate HTML Report", type="primary", use_container_width=True):
            with st.spinner("Generating report... This may take a moment."):
                report_html = generate_html_report(df, sections)
                st.session_state['report_html'] = report_html
                st.markdown(success_box_html("Report generated successfully!"), unsafe_allow_html=True)
                
        if 'report_html' in st.session_state:
            st.download_button(
                label="📥 Download HTML Report",
                data=st.session_state['report_html'],
                file_name=f"eda_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.html",
                mime="text/html",
                use_container_width=True
            )
            
    st.markdown(glass_container_end(), unsafe_allow_html=True)
