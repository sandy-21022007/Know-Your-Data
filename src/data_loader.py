"""
Know-Your-Data — Data Loader Module.
Handles file upload (CSV, Excel, JSON, Parquet), parsing, caching,
and renders the animated landing page when no data is loaded.
"""

import streamlit as st
import pandas as pd
from io import BytesIO

from utils.helpers import (
    format_number, format_bytes, section_header_html,
    info_box_html, success_box_html,
)


# ──────────────────────────────────────────────
# LANDING PAGE FEATURE CARDS
# ──────────────────────────────────────────────

_FEATURES = [
    ("📋", "Data Overview", "Shape, types & memory"),
    ("🔍", "Missing Values", "Null analysis & heatmaps"),
    ("📊", "Statistics", "Deep statistical summary"),
    ("📈", "Distributions", "Histograms & box plots"),
    ("🔗", "Correlations", "Interactive heatmap"),
    ("📑", "Duplicates", "Duplicate detection"),
    ("⚡", "Outliers", "IQR & Z-score analysis"),
    ("💡", "Type Hints", "Smart type suggestions"),
    ("📥", "Export Report", "Download HTML report"),
    ("🚨", "Alerts", "Auto data-quality warnings"),
    ("🔄", "Interactions", "Pairwise scatter explorer"),
    ("📝", "Text Analysis", "Word & character stats"),
]


def _feature_card_html(icon: str, title: str, desc: str, idx: int) -> str:
    """Return HTML for a single animated feature card."""
    return f"""
    <div class="feature-card stagger-{(idx % 8) + 1}">
        <div class="feature-icon">{icon}</div>
        <div class="feature-title">{title}</div>
        <div class="feature-desc">{desc}</div>
    </div>
    """


# ──────────────────────────────────────────────
# FILE PARSING
# ──────────────────────────────────────────────

def load_file(uploaded_file) -> pd.DataFrame:
    """
    Parse an uploaded file based on its extension.

    Supported: .csv, .xlsx, .xls, .json, .parquet
    Returns a pandas DataFrame.
    Raises ValueError on unsupported format or parse errors.
    """
    name = uploaded_file.name.lower()
    raw = BytesIO(uploaded_file.getvalue())

    try:
        if name.endswith(".csv"):
            return pd.read_csv(raw)

        elif name.endswith((".xlsx", ".xls")):
            xls = pd.ExcelFile(raw)
            sheets = xls.sheet_names
            st.session_state["excel_sheets"] = sheets
            st.session_state["raw_file_bytes"] = uploaded_file.getvalue()
            st.session_state["current_sheet"] = sheets[0]
            return pd.read_excel(raw, sheet_name=sheets[0])

        elif name.endswith(".json"):
            try:
                return pd.read_json(raw)
            except ValueError:
                raw.seek(0)
                return pd.read_json(raw, orient="records")

        elif name.endswith(".parquet"):
            return pd.read_parquet(raw)

        else:
            raise ValueError(
                f"Unsupported file format: {name.split('.')[-1]}"
            )

    except Exception as exc:
        raise ValueError(f"Error parsing **{uploaded_file.name}**: {exc}") from exc


def get_file_info(uploaded_file) -> dict:
    """Return metadata dict for the uploaded file."""
    return {
        "name": uploaded_file.name,
        "size": uploaded_file.size,
        "type": uploaded_file.type or "unknown",
    }


# ──────────────────────────────────────────────
# MAIN RENDER FUNCTION
# ──────────────────────────────────────────────

def render_upload() -> "pd.DataFrame | None":
    """
    Render the upload page.

    * When no file is uploaded → beautiful hero landing page.
    * When a file is uploaded  → parse it, cache in session_state, show summary.

    Returns the parsed DataFrame, or None.
    """

    # ---------- check session cache ----------
    if "df" in st.session_state and st.session_state["df"] is not None:
        df = st.session_state["df"]
        file_name = st.session_state.get("file_name", "Dataset")
        _render_upload_success(df, file_name)
        return df

    # ---------- hero section ----------
    st.markdown(
        """
        <div class="hero-container">
            <div class="hero-title">Know Your Data</div>
            <div class="hero-subtitle">
                Upload your dataset and get instant, comprehensive exploratory
                data analysis.&nbsp;Save hours of repetitive work.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ---------- file uploader ----------
    st.markdown(
        """
        <div class="upload-area">
            <div class="upload-icon">📁</div>
            <div style="color: #fafafa; font-size: 1.1rem; font-weight: 600; margin-bottom: 4px;">
                Drag & drop your file here
            </div>
            <div style="color: #a0aec0; font-size: 0.85rem;">
                Supports CSV · Excel · JSON · Parquet &nbsp;(up to 200 MB)
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    uploaded = st.file_uploader(
        "Upload your dataset",
        type=["csv", "xlsx", "xls", "json", "parquet"],
        label_visibility="collapsed",
        key="file_uploader",
    )

    # ---------- feature cards grid ----------
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        section_header_html("✨ What You'll Get", "Comprehensive analysis in seconds"),
        unsafe_allow_html=True,
    )

    rows = [_FEATURES[i : i + 4] for i in range(0, len(_FEATURES), 4)]
    for row_idx, row in enumerate(rows):
        cols = st.columns(len(row))
        for col_idx, (icon, title, desc) in enumerate(row):
            with cols[col_idx]:
                st.markdown(
                    _feature_card_html(icon, title, desc, row_idx * 4 + col_idx),
                    unsafe_allow_html=True,
                )

    # ---------- handle upload ----------
    if uploaded is not None:
        try:
            with st.spinner("🔄 Parsing your data…"):
                df = load_file(uploaded)
            file_info = get_file_info(uploaded)
            st.session_state["df"] = df
            st.session_state["file_name"] = file_info["name"]
            st.session_state["file_info"] = file_info
            st.toast(f"✅ Loaded **{file_info['name']}** — {df.shape[0]:,} rows × {df.shape[1]} cols", icon="🎉")
            st.rerun()
        except ValueError as exc:
            st.error(str(exc))
            return None

    return None


def _render_upload_success(df: pd.DataFrame, file_name: str) -> None:
    """Show a summary after successful data upload."""

    st.markdown(
        section_header_html("✅ Dataset Loaded", f"{file_name}"),
        unsafe_allow_html=True,
    )

    mem = df.memory_usage(deep=True).sum()

    cols = st.columns(4)
    cards = [
        ("📊", format_number(df.shape[0]), "Rows"),
        ("📋", str(df.shape[1]), "Columns"),
        ("💾", format_bytes(mem), "Memory"),
        ("📑", format_number(df.duplicated().sum()), "Duplicates"),
    ]
    for i, (icon, value, label) in enumerate(cards):
        with cols[i]:
            st.markdown(
                f"""
                <div class="metric-card stagger-{i + 1}">
                    <div class="metric-icon">{icon}</div>
                    <div class="metric-value">{value}</div>
                    <div class="metric-label">{label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        success_box_html(
            f"🎉 Your data is ready! Use the <b>sidebar navigation</b> to explore every aspect of your dataset."
        ),
        unsafe_allow_html=True,
    )

    with st.expander("👀 Quick Preview — First 10 Rows", expanded=True):
        st.dataframe(df.head(10), use_container_width=True)

    if "excel_sheets" in st.session_state and len(st.session_state["excel_sheets"]) > 1:
        sheets = st.session_state["excel_sheets"]
        curr = st.session_state.get("current_sheet", sheets[0])
        idx = sheets.index(curr) if curr in sheets else 0
        selected_sheet = st.selectbox(
            "📄 Multiple sheets detected — choose sheet to analyze:",
            sheets,
            index=idx,
            key="sheet_picker",
        )
        if selected_sheet != st.session_state.get("current_sheet"):
            raw = BytesIO(st.session_state["raw_file_bytes"])
            st.session_state["df"] = pd.read_excel(raw, sheet_name=selected_sheet)
            st.session_state["current_sheet"] = selected_sheet
            st.rerun()

    if st.button("🔄 Upload a different file", use_container_width=True):
        for key in ["df", "file_name", "file_info", "excel_sheets", "raw_file_bytes", "current_sheet", "report_html"]:
            st.session_state.pop(key, None)
        st.rerun()
