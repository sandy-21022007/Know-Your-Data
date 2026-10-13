"""
Know-Your-Data — Text / String Column Analysis.
Inspired by ydata-profiling's text analysis: word frequency, character stats,
length distributions, and pattern detection.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from collections import Counter
import re

from utils.helpers import (
    section_header_html, metric_card_html, badge_html,
    info_box_html, success_box_html, warning_box_html,
    format_number, format_percentage,
    get_categorical_columns,
)
from utils.plotting import style_figure, COLORS, CHART_CONFIG

# ──────────────────────────────────────────────
# STOP WORDS (basic English set — no NLTK needed)
# ──────────────────────────────────────────────

STOP_WORDS = {
    "the", "a", "an", "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "by", "from", "is", "was", "are", "were", "be", "been",
    "being", "have", "has", "had", "do", "does", "did", "will", "would",
    "could", "should", "may", "might", "shall", "can", "need", "dare",
    "ought", "used", "it", "its", "this", "that", "these", "those",
    "i", "me", "my", "we", "our", "you", "your", "he", "him", "his",
    "she", "her", "they", "them", "their", "what", "which", "who",
    "whom", "where", "when", "why", "how", "not", "no", "nor",
    "as", "if", "then", "than", "too", "very", "just", "about",
    "above", "after", "again", "all", "also", "any", "because",
    "before", "between", "both", "each", "few", "more", "most",
    "other", "over", "same", "so", "some", "such", "up", "out",
}


# ──────────────────────────────────────────────
# HELPER UTILITIES
# ──────────────────────────────────────────────

def _get_text_columns(df: pd.DataFrame) -> list[str]:
    """Return object / string dtype column names."""
    return df.select_dtypes(include=["object", "string"]).columns.tolist()


def _safe_series(series: pd.Series, max_rows: int = 10_000) -> pd.Series:
    """Return a (possibly sampled) non-null series of strings."""
    s = series.dropna().astype(str)
    if len(s) > max_rows:
        s = s.sample(max_rows, random_state=42)
    return s


# ──────────────────────────────────────────────
# RENDER
# ──────────────────────────────────────────────

def render(df: pd.DataFrame) -> None:
    """Render the text analysis section."""

    st.markdown(
        section_header_html(
            "📝 Text Analysis",
            "Deep-dive into text and string columns — words, characters, and patterns",
        ),
        unsafe_allow_html=True,
    )

    text_cols = _get_text_columns(df)
    if not text_cols:
        st.markdown(
            info_box_html("No text / object columns found in this dataset."),
            unsafe_allow_html=True,
        )
        return

    # Column selector
    selected_col = st.selectbox("Select a text column", text_cols, key="txt_col")
    raw = df[selected_col]
    non_null = raw.dropna()
    safe = _safe_series(raw)

    # ── Tabs ──────────────────────────────────
    tabs = st.tabs(["Overview", "Word Analysis", "Character Analysis", "Patterns", "Value Counts"])

    # ============================
    # TAB 1: OVERVIEW
    # ============================
    with tabs[0]:
        _render_overview(raw, non_null, safe, selected_col)

    # ============================
    # TAB 2: WORD ANALYSIS
    # ============================
    with tabs[1]:
        _render_word_analysis(safe, selected_col)

    # ============================
    # TAB 3: CHARACTER ANALYSIS
    # ============================
    with tabs[2]:
        _render_character_analysis(safe, selected_col)

    # ============================
    # TAB 4: PATTERN DETECTION
    # ============================
    with tabs[3]:
        _render_patterns(safe, selected_col)

    # ============================
    # TAB 5: VALUE COUNTS
    # ============================
    with tabs[4]:
        _render_value_counts(non_null, selected_col)


# ──────────────────────────────────────────────
# TAB RENDERERS
# ──────────────────────────────────────────────

def _render_overview(raw, non_null, safe, col_name):
    """Overview metrics & length distribution."""

    total = len(non_null)
    unique = non_null.nunique()
    lengths = safe.str.len()
    avg_len = lengths.mean() if len(lengths) > 0 else 0
    empty_count = int((safe == "").sum())

    cols = st.columns(4)
    cards = [
        ("📊", format_number(total), "Total Values", 1),
        ("🔢", format_number(unique), "Unique Values", 2),
        ("📏", f"{avg_len:.1f}", "Avg Length", 3),
        ("⬜", format_number(empty_count), "Empty Strings", 4),
    ]
    for i, (icon, val, label, stag) in enumerate(cards):
        with cols[i]:
            st.markdown(metric_card_html(icon, val, label, stag), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Length distribution
    if len(lengths) > 0:
        c1, c2 = st.columns(2)
        with c1:
            fig = px.histogram(
                x=lengths, nbins=50,
                labels={"x": "String Length", "y": "Count"},
                title="String Length Distribution",
                color_discrete_sequence=[COLORS[0]],
            )
            style_figure(fig)
            st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)

        with c2:
            fig = px.box(
                x=lengths,
                labels={"x": "String Length"},
                title="String Length Box Plot",
                color_discrete_sequence=[COLORS[2]],
            )
            style_figure(fig)
            st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)

        # Length stats
        lcols = st.columns(4)
        for i, (label, val) in enumerate([
            ("Min Length", int(lengths.min())),
            ("Max Length", int(lengths.max())),
            ("Median Length", f"{lengths.median():.0f}"),
            ("Std Dev", f"{lengths.std():.1f}"),
        ]):
            with lcols[i]:
                st.metric(label, val)


def _render_word_analysis(safe, col_name):
    """Word frequency and word-length analysis."""

    exclude_stop = st.checkbox("Exclude stop words", value=True, key="txt_stopwords")

    all_words = []
    for text in safe:
        words = re.findall(r"\b[a-zA-Z]+\b", text.lower())
        if exclude_stop:
            words = [w for w in words if w not in STOP_WORDS]
        all_words.extend(words)

    if not all_words:
        st.markdown(
            info_box_html("No words found in this column (or all filtered out by stop words)."),
            unsafe_allow_html=True,
        )
        return

    word_counter = Counter(all_words)
    total_words = len(all_words)
    unique_words = len(word_counter)
    words_per_val = total_words / max(len(safe), 1)

    cols = st.columns(3)
    cards = [
        ("📝", format_number(total_words), "Total Words"),
        ("🔤", format_number(unique_words), "Unique Words"),
        ("📐", f"{words_per_val:.1f}", "Avg Words / Value"),
    ]
    for i, (icon, val, label) in enumerate(cards):
        with cols[i]:
            st.markdown(metric_card_html(icon, val, label, i + 1), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Top 30 words bar chart
    top_words = word_counter.most_common(30)
    words_df = pd.DataFrame(top_words, columns=["Word", "Count"])

    fig = px.bar(
        words_df, x="Count", y="Word", orientation="h",
        title="Top 30 Most Frequent Words",
        color="Count",
        color_continuous_scale=[[0, COLORS[0]], [1, COLORS[1]]],
    )
    style_figure(fig, height=max(400, len(top_words) * 22))
    fig.update_layout(yaxis=dict(autorange="reversed"), showlegend=False)
    st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)

    # Word length distribution
    word_lengths = [len(w) for w in all_words]
    fig = px.histogram(
        x=word_lengths, nbins=30,
        labels={"x": "Word Length (chars)", "y": "Count"},
        title="Word Length Distribution",
        color_discrete_sequence=[COLORS[2]],
    )
    style_figure(fig)
    st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)


def _render_character_analysis(safe, col_name):
    """Character frequency and type breakdown."""

    all_chars = "".join(safe.values)
    if not all_chars:
        st.markdown(info_box_html("No characters to analyse."), unsafe_allow_html=True)
        return

    total_chars = len(all_chars)
    unique_chars = len(set(all_chars))

    # Character type counts
    n_lower = sum(1 for c in all_chars if c.islower())
    n_upper = sum(1 for c in all_chars if c.isupper())
    n_digit = sum(1 for c in all_chars if c.isdigit())
    n_space = sum(1 for c in all_chars if c.isspace())
    n_special = total_chars - n_lower - n_upper - n_digit - n_space

    cols = st.columns(2)
    with cols[0]:
        st.markdown(metric_card_html("🔡", format_number(total_chars), "Total Characters", 1), unsafe_allow_html=True)
    with cols[1]:
        st.markdown(metric_card_html("✨", format_number(unique_chars), "Unique Characters", 2), unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        # Donut chart of character types
        labels = ["Lowercase", "Uppercase", "Digits", "Spaces", "Special"]
        values = [n_lower, n_upper, n_digit, n_space, n_special]
        fig = go.Figure(data=[go.Pie(
            labels=labels, values=values,
            hole=0.55,
            marker=dict(colors=COLORS[:5]),
            textinfo="label+percent",
            textfont=dict(color="#fafafa"),
        )])
        style_figure(fig, title_text="Character Type Breakdown")
        st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)

    with c2:
        # Top 30 character frequency
        char_counter = Counter(all_chars)
        top_chars = char_counter.most_common(30)
        char_df = pd.DataFrame(top_chars, columns=["Character", "Count"])
        # Make whitespace visible
        char_df["Character"] = char_df["Character"].apply(
            lambda c: repr(c) if c.isspace() else c
        )

        fig = px.bar(
            char_df, x="Count", y="Character", orientation="h",
            title="Top 30 Characters",
            color="Count",
            color_continuous_scale=[[0, COLORS[0]], [1, COLORS[1]]],
        )
        style_figure(fig, height=max(400, len(top_chars) * 20))
        fig.update_layout(yaxis=dict(autorange="reversed"), showlegend=False)
        st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)


def _render_patterns(safe, col_name):
    """Pattern detection: emails, URLs, phones, dates, prefixes, suffixes."""

    st.markdown("#### 🔎 Detected Patterns", unsafe_allow_html=True)

    # Pattern checks
    email_mask = safe.str.contains(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", regex=True, na=False)
    url_mask = safe.str.contains(r"https?://|www\.", regex=True, na=False)
    phone_mask = safe.str.contains(r"\+?\d[\d\s\-]{7,}\d", regex=True, na=False)

    n_email = int(email_mask.sum())
    n_url = int(url_mask.sum())
    n_phone = int(phone_mask.sum())

    # Date detection (sample-based)
    n_date = 0
    try:
        sample = safe.head(200)
        parsed = pd.to_datetime(sample, errors="coerce", format="mixed")
        n_date = int(parsed.notna().sum())
        if n_date < len(sample) * 0.5:
            n_date = 0  # Not convincingly date-like
    except Exception:
        pass

    # Display badges
    patterns_found = []
    if n_email > 0:
        patterns_found.append(("📧 Email Addresses", n_email, "info"))
    if n_url > 0:
        patterns_found.append(("🔗 URLs", n_url, "info"))
    if n_phone > 0:
        patterns_found.append(("📞 Phone Numbers", n_phone, "info"))
    if n_date > 0:
        patterns_found.append(("📅 Date-like Values", n_date, "warning"))

    if patterns_found:
        cols = st.columns(len(patterns_found))
        for i, (label, count, btype) in enumerate(patterns_found):
            with cols[i]:
                st.markdown(
                    metric_card_html(label.split(" ")[0], format_number(count), " ".join(label.split(" ")[1:]), i + 1),
                    unsafe_allow_html=True,
                )
    else:
        st.markdown(
            info_box_html("No specific patterns (email, URL, phone, date) detected."),
            unsafe_allow_html=True,
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Prefix / suffix analysis
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("#### Common Prefixes (first 5 chars)")
        prefixes = safe.str[:5].value_counts().head(10)
        if len(prefixes) > 0:
            fig = px.bar(
                x=prefixes.values, y=prefixes.index, orientation="h",
                labels={"x": "Count", "y": "Prefix"},
                color_discrete_sequence=[COLORS[0]],
            )
            style_figure(fig, height=300)
            fig.update_layout(yaxis=dict(autorange="reversed"))
            st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)

    with c2:
        st.markdown("#### Common Suffixes (last 5 chars)")
        suffixes = safe.str[-5:].value_counts().head(10)
        if len(suffixes) > 0:
            fig = px.bar(
                x=suffixes.values, y=suffixes.index, orientation="h",
                labels={"x": "Count", "y": "Suffix"},
                color_discrete_sequence=[COLORS[1]],
            )
            style_figure(fig, height=300)
            fig.update_layout(yaxis=dict(autorange="reversed"))
            st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)


def _render_value_counts(non_null, col_name):
    """Value counts: top N, bottom N, frequency distribution."""

    vc = non_null.value_counts()
    total = len(non_null)

    # Top 20
    top = vc.head(20)
    top_df = pd.DataFrame({"Value": top.index, "Count": top.values})
    top_df["Percentage"] = (top_df["Count"] / total * 100).round(2)

    fig = px.bar(
        top_df, x="Count", y="Value", orientation="h",
        title=f"Top 20 Most Frequent Values",
        color="Count",
        color_continuous_scale=[[0, COLORS[0]], [1, COLORS[1]]],
        hover_data=["Percentage"],
    )
    style_figure(fig, height=max(400, len(top_df) * 24))
    fig.update_layout(yaxis=dict(autorange="reversed", dtick=1), showlegend=False)
    fig.update_traces(hovertemplate="<b>%{y}</b><br>Count: %{x}<br>%{customdata[0]:.2f}%<extra></extra>")
    st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)

    # Bottom 10 (rarest)
    if len(vc) > 20:
        with st.expander("🔻 10 Rarest Values"):
            bottom = vc.tail(10)
            bottom_df = pd.DataFrame({"Value": bottom.index, "Count": bottom.values})
            st.dataframe(bottom_df, use_container_width=True)

    # Frequency of frequencies
    with st.expander("📊 Frequency Distribution (how many values appear N times)"):
        freq_of_freq = vc.value_counts().sort_index()
        ff_df = pd.DataFrame({"Occurrences": freq_of_freq.index, "Num Values": freq_of_freq.values})

        fig = px.bar(
            ff_df.head(30), x="Occurrences", y="Num Values",
            title="Frequency of Frequencies",
            color_discrete_sequence=[COLORS[2]],
        )
        style_figure(fig)
        st.plotly_chart(fig, use_container_width=True, config=CHART_CONFIG)

        cols = st.columns(3)
        appear_once = int((vc == 1).sum())
        with cols[0]:
            st.metric("Appear Once", format_number(appear_once))
        with cols[1]:
            st.metric("Appear 2-5×", format_number(int(((vc >= 2) & (vc <= 5)).sum())))
        with cols[2]:
            st.metric("Appear 5+×", format_number(int((vc > 5).sum())))
