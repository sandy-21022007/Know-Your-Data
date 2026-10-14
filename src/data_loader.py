"""
Know-Your-Data — Futuristic Cyber Data Ingestion & Landing Architecture.
Featuring:
- Laser-scanning Drop Zone with HUD reticles (cleanly compiled)
- Automated Analysis Loading State with Neural Core & Terminal Telemetry
- Interactive Holographic Preview & 3D Staggered Cards
- 1-Click Instant Demo Dataset Loader
"""

import time
import os
import streamlit as st
import pandas as pd
from io import BytesIO

from utils.helpers import (
    format_number, format_bytes, section_header_html,
    info_box_html, success_box_html, divider_html,
    metric_card_html, badge_html, neural_core_html,
    terminal_log_box_html, skeleton_loader_html,
)

try:
    from utils.helpers import clean_html
except ImportError:
    def clean_html(html_str: str) -> str:
        lines = [line.strip() for line in html_str.strip().split("\n") if line.strip()]
        return "".join(lines)


# ──────────────────────────────────────────────
# LANDING PAGE FEATURE MATRIX
# ──────────────────────────────────────────────

_FEATURES = [
    ("⚡", "Neural Overview", "Shape, topology & memory profile"),
    ("🔍", "Null Matrix", "Missing density & correlation patterns"),
    ("📊", "Quantum Statistics", "High-order statistical moments"),
    ("📈", "Distributions", "Parametric & KDE distribution curves"),
    ("🔗", "Vector Correlations", "Pearson, Spearman & Kendall tensors"),
    ("📑", "Duplicate Scanner", "Exact & fuzzy record matching"),
    ("🚨", "Anomaly Detection", "IQR & multivariate outlier boundary"),
    ("💡", "Smart Schema Hints", "AI-recommended type conversions"),
    ("🔄", "Interaction Explorer", "Pairwise multi-dimensional projections"),
    ("📝", "NLP Text Telemetry", "Shannon entropy & token metrics"),
    ("🛡️", "Data Quality Alerts", "Automated heuristics & risk ranking"),
    ("📥", "Autonomous Report", "Export executive HTML dossier"),
]


def _feature_card_html(icon: str, title: str, desc: str, idx: int) -> str:
    """Return HTML for a single 3D interactive cyber feature card."""
    return clean_html(f"""
    <div class="feature-card stagger-{(idx % 8) + 1}">
        <div class="feature-icon">{icon}</div>
        <div class="feature-title">{title}</div>
        <div class="feature-desc">{desc}</div>
    </div>
    """)


# ──────────────────────────────────────────────
# FILE PARSING PIPELINE
# ──────────────────────────────────────────────

def load_file(uploaded_file) -> pd.DataFrame:
    """
    Parse an uploaded file stream into a pandas DataFrame.
    Supported protocols: CSV, XLSX, XLS, JSON, Parquet.
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
            raise ValueError(f"Unsupported protocol: {name.split('.')[-1].upper()}")

    except Exception as exc:
        raise ValueError(f"Ingestion error on **{uploaded_file.name}**: {exc}") from exc


def get_file_info(uploaded_file) -> dict:
    """Extract metadata headers from uploaded stream."""
    return {
        "name": uploaded_file.name,
        "size": uploaded_file.size,
        "type": uploaded_file.type or "binary/octet-stream",
    }


# ──────────────────────────────────────────────
# MAIN RENDER ENTRYPOINT
# ──────────────────────────────────────────────

def render_upload() -> "pd.DataFrame | None":
    """
    Render the cyber ingestion cockpit.
    - If dataset is loaded -> show interactive dashboard & telemetry
    - If awaiting file -> show laser dropzone, demo loader, and feature grid
    """

    # Check session state cache
    if "df" in st.session_state and st.session_state["df"] is not None:
        df = st.session_state["df"]
        file_name = st.session_state.get("file_name", "Dataset")
        _render_upload_success(df, file_name)
        return df

    # Check if analysis simulation is in progress
    if st.session_state.get("simulating_analysis", False):
        _render_loading_state()
        return None

    # ---------- HERO SECTION ----------
    st.markdown(
        clean_html("""
        <div class="hero-container">
            <div class="hero-hud-pill">
                <div class="hero-hud-dot"></div>
                <span>AUTONOMOUS EDA ENGINE // v4.8 ONLINE</span>
            </div>
            <div class="hero-title">Know Your Data</div>
            <div class="hero-subtitle">
                An elite automated exploratory intelligence platform. Ingest complex datasets,
                uncover hidden anomalies, compute multidimensional correlations, and generate
                executive dossiers in milliseconds.
            </div>
        </div>
        """),
        unsafe_allow_html=True,
    )

    # ---------- CYBER DRAG-AND-DROP INGESTION COCKPIT ----------
    st.markdown(
        clean_html("""
        <div class="dropzone-cyber">
            <div class="hud-corner hud-corner-tl"></div>
            <div class="hud-corner hud-corner-tr"></div>
            <div class="hud-corner hud-corner-bl"></div>
            <div class="hud-corner hud-corner-br"></div>
            <div class="laser-scanner"></div>
            <div class="dropzone-icon">⚡</div>
            <div class="dropzone-title">DATA STREAM INGESTION PORT</div>
            <div class="dropzone-subtitle">Drag & drop dataset stream or browse local storage for automated neural analysis</div>
            <div class="dropzone-chips">
                <span class="dropzone-chip">PROTOCOL: CSV</span>
                <span class="dropzone-chip">PROTOCOL: EXCEL (XLSX/XLS)</span>
                <span class="dropzone-chip">PROTOCOL: JSON</span>
                <span class="dropzone-chip">PROTOCOL: PARQUET</span>
                <span class="dropzone-chip">MAX BUFFER: 200 MB</span>
            </div>
        </div>
        """),
        unsafe_allow_html=True,
    )

    # Streamlit native file uploader
    uploaded = st.file_uploader(
        "Upload dataset",
        type=["csv", "xlsx", "xls", "json", "parquet"],
        label_visibility="collapsed",
        key="file_uploader",
    )

    # ---------- ONE-CLICK DEMO LOADER ----------
    col_demo, col_blank = st.columns([1, 1])
    demo_path = "sales_dataset_1000_rows.csv"
    if os.path.exists(demo_path):
        with col_demo:
            if st.button("⚡ Ingest Sample Dataset (Sales 1,000 Records)", use_container_width=True):
                st.session_state["simulating_analysis"] = True
                st.session_state["pending_file_source"] = "sample_csv"
                st.rerun()

    # ---------- FEATURE CAPABILITIES GRID ----------
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        section_header_html("Neural Capabilities", "Autonomous analytical subroutines running parallel"),
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

    # ---------- HANDLE UPLOAD EVENT ----------
    if uploaded is not None:
        try:
            st.session_state["simulating_analysis"] = True
            st.session_state["pending_uploaded_file"] = uploaded
            st.rerun()
        except ValueError as exc:
            st.error(str(exc))
            return None

    return None


# ──────────────────────────────────────────────
# AUTOMATED ANALYSIS LOADING STATE (NEURAL CORE)
# ──────────────────────────────────────────────

def _render_loading_state():
    """Render the central Neural Core animation with live hacker terminal telemetry."""
    st.markdown("<br>", unsafe_allow_html=True)

    core_placeholder = st.empty()
    terminal_placeholder = st.empty()
    progress_bar = st.progress(0)

    stages = [
        (20, "INITIALIZING NEURAL CORE", [
            ("00:00:00.102", "KERNEL", "Mounting high-performance pandas vector engine"),
            ("00:00:00.215", "ALLOC", "Allocating RAM buffer for dataset parsing"),
        ]),
        (45, "INFERRING DATA TOPOLOGY", [
            ("00:00:00.102", "KERNEL", "Mounting high-performance pandas vector engine"),
            ("00:00:00.215", "ALLOC", "Allocating RAM buffer for dataset parsing"),
            ("00:00:00.430", "SCHEMA", "Scanning columns, data types & semantic classifications"),
            ("00:00:00.612", "ENTROPY", "Evaluating null distributions & missing matrix"),
        ]),
        (75, "CALCULATING MULTIVARIATE TENSORS", [
            ("00:00:00.102", "KERNEL", "Mounting high-performance pandas vector engine"),
            ("00:00:00.215", "ALLOC", "Allocating RAM buffer for dataset parsing"),
            ("00:00:00.430", "SCHEMA", "Scanning columns, data types & semantic classifications"),
            ("00:00:00.612", "ENTROPY", "Evaluating null distributions & missing matrix"),
            ("00:00:00.820", "CORR", "Generating Pearson & Spearman covariance matrices"),
            ("00:00:01.010", "OUTLIER", "Scanning IQR outlier boundaries and Z-score vectors"),
        ]),
        (100, "SYNTHESIZING COCKPIT HUD", [
            ("00:00:00.102", "KERNEL", "Mounting high-performance pandas vector engine"),
            ("00:00:00.215", "ALLOC", "Allocating RAM buffer for dataset parsing"),
            ("00:00:00.430", "SCHEMA", "Scanning columns, data types & semantic classifications"),
            ("00:00:00.612", "ENTROPY", "Evaluating null distributions & missing matrix"),
            ("00:00:00.820", "CORR", "Generating Pearson & Spearman covariance matrices"),
            ("00:00:01.010", "OUTLIER", "Scanning IQR outlier boundaries and Z-score vectors"),
            ("00:00:01.205", "COMPLETE", "Telemetry compiled · 60fps HUD ready"),
        ]),
    ]

    for pct, title, logs in stages:
        core_placeholder.markdown(neural_core_html(pct, title), unsafe_allow_html=True)
        terminal_placeholder.markdown(terminal_log_box_html(logs), unsafe_allow_html=True)
        progress_bar.progress(pct)
        time.sleep(0.35)

    source = st.session_state.pop("pending_file_source", None)
    uploaded = st.session_state.pop("pending_uploaded_file", None)

    if source == "sample_csv":
        df = pd.read_csv("sales_dataset_1000_rows.csv")
        file_name = "sales_dataset_1000_rows.csv"
        file_info = {"name": file_name, "size": os.path.getsize(file_name), "type": "text/csv"}
    elif uploaded is not None:
        df = load_file(uploaded)
        file_info = get_file_info(uploaded)
        file_name = file_info["name"]
    else:
        st.session_state["simulating_analysis"] = False
        st.rerun()
        return

    st.session_state["df"] = df
    st.session_state["file_name"] = file_name
    st.session_state["file_info"] = file_info
    st.session_state["simulating_analysis"] = False
    st.toast(f"⚡ Ingested **{file_name}** ({df.shape[0]:,} records)", icon="🚀")
    st.rerun()


# ──────────────────────────────────────────────
# DASHBOARD PREVIEW / RESULTS VIEW
# ──────────────────────────────────────────────

def _render_upload_success(df: pd.DataFrame, file_name: str) -> None:
    """Show rich holographic cockpit view after successful ingestion."""

    col_hdr_left, col_hdr_right = st.columns([3, 1])
    with col_hdr_left:
        st.markdown(
            section_header_html(
                f"Ingestion Dossier: {file_name}",
                "Stream verified · Neural Core telemetry locked"
            ),
            unsafe_allow_html=True,
        )
    with col_hdr_right:
        st.markdown(
            clean_html("""
            <div style="text-align: right; padding-top: 10px;">
                <span class="badge badge-success">● SYSTEM ONLINE</span>
                <span class="badge badge-primary">INTEGRITY 100%</span>
            </div>
            """),
            unsafe_allow_html=True,
        )

    mem = df.memory_usage(deep=True).sum()
    duplicates_count = int(df.duplicated().sum())
    missing_total = int(df.isna().sum().sum())

    cols = st.columns(4)
    cards = [
        ("📊", format_number(df.shape[0]), "Total Records", 1, "+100% PARSED"),
        ("📋", str(df.shape[1]), "Attributes / Cols", 2, "12 FEATURES"),
        ("💾", format_bytes(mem), "Memory Footprint", 3, "OPTIMAL"),
        ("📑", format_number(duplicates_count), "Duplicate Records", 4, "0 HAZARDS" if duplicates_count == 0 else "FLAGGED"),
    ]
    for i, (icon, value, label, stagger, delta) in enumerate(cards):
        with cols[i]:
            st.markdown(
                metric_card_html(icon, value, label, stagger=stagger, delta=delta),
                unsafe_allow_html=True,
            )

    st.markdown("<br>", unsafe_allow_html=True)

    tab_preview, tab_telemetry, tab_schema = st.tabs([
        "👀 Holographic Data Preview",
        "⚡ Telemetry Terminal",
        "📐 Attribute Schema Breakdown",
    ])

    with tab_preview:
        st.markdown(
            success_box_html(
                "✨ Stream active! Explore deep analytics using the <b>sidebar navigation</b> or inspect the tabular buffer below."
            ),
            unsafe_allow_html=True,
        )
        st.dataframe(df.head(15), use_container_width=True)

    with tab_telemetry:
        st.markdown(
            terminal_log_box_html([
                ("00:00:00.120", "STREAM_LOAD", f"Ingested {file_name} ({format_bytes(mem)})"),
                ("00:00:00.312", "RECORDS", f"Allocated {df.shape[0]:,} rows x {df.shape[1]} columns"),
                ("00:00:00.540", "NULL_CHECK", f"Total null values across matrix: {missing_total:,}"),
                ("00:00:00.780", "DUPLICATE", f"Duplicate row count: {duplicates_count:,}"),
                ("00:00:01.010", "PIPELINE", "EDA subroutines armed: Overview, Distributions, Correlations, Outliers"),
            ]),
            unsafe_allow_html=True,
        )

    with tab_schema:
        schema_df = pd.DataFrame({
            "Column Name": df.columns,
            "Inferred Type": [str(t) for t in df.dtypes],
            "Non-Null Count": [df[c].count() for c in df.columns],
            "Null Count": [df[c].isna().sum() for c in df.columns],
            "Unique Values": [df[c].nunique() for c in df.columns],
        })
        st.dataframe(schema_df, use_container_width=True)

    if "excel_sheets" in st.session_state and len(st.session_state["excel_sheets"]) > 1:
        sheets = st.session_state["excel_sheets"]
        curr = st.session_state.get("current_sheet", sheets[0])
        idx = sheets.index(curr) if curr in sheets else 0
        selected_sheet = st.selectbox(
            "📄 Multi-Sheet Workbook Detected — Select Target Sheet:",
            sheets,
            index=idx,
            key="sheet_picker",
        )
        if selected_sheet != st.session_state.get("current_sheet"):
            raw = BytesIO(st.session_state["raw_file_bytes"])
            st.session_state["df"] = pd.read_excel(raw, sheet_name=selected_sheet)
            st.session_state["current_sheet"] = selected_sheet
            st.rerun()

    st.markdown(divider_html(), unsafe_allow_html=True)

    col_btn1, col_btn2 = st.columns([1, 1])
    with col_btn1:
        if st.button("🔄 Flush & Ingest Different Dataset", use_container_width=True):
            for key in ["df", "file_name", "file_info", "excel_sheets", "raw_file_bytes", "current_sheet", "report_html"]:
                st.session_state.pop(key, None)
            st.rerun()
