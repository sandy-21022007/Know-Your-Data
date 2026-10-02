"""
Know-Your-Data — Custom CSS Styles & Animations.
Central stylesheet for the entire application.
"""

import streamlit as st


def inject_custom_css():
    """Inject all custom CSS styles and animations into the Streamlit app."""
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


CUSTOM_CSS = """
<style>
    /* ==================== IMPORTS ==================== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    /* ==================== ROOT VARIABLES ==================== */
    :root {
        --primary: #667eea;
        --primary-dark: #5a6fd6;
        --secondary: #764ba2;
        --accent: #00d2ff;
        --success: #00c853;
        --warning: #ff6d00;
        --error: #ff1744;
        --bg-card: rgba(255, 255, 255, 0.05);
        --border-card: rgba(255, 255, 255, 0.1);
        --text-primary: #fafafa;
        --text-secondary: #a0aec0;
        --gradient-primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --gradient-accent: linear-gradient(135deg, #00d2ff 0%, #667eea 100%);
        --shadow-card: 0 8px 32px rgba(0, 0, 0, 0.3);
        --radius-lg: 16px;
        --radius-md: 12px;
        --radius-sm: 8px;
    }

    /* ==================== GLOBAL ==================== */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    /* ==================== ANIMATIONS ==================== */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(30px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInLeft {
        from { opacity: 0; transform: translateX(-30px); }
        to   { opacity: 1; transform: translateX(0); }
    }
    @keyframes fadeInRight {
        from { opacity: 0; transform: translateX(30px); }
        to   { opacity: 1; transform: translateX(0); }
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to   { opacity: 1; }
    }
    @keyframes scaleIn {
        from { opacity: 0; transform: scale(0.9); }
        to   { opacity: 1; transform: scale(1); }
    }
    @keyframes slideDown {
        from { opacity: 0; transform: translateY(-20px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulse {
        0%, 100% { transform: scale(1); }
        50%      { transform: scale(1.03); }
    }
    @keyframes shimmer {
        0%   { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    @keyframes gradientFlow {
        0%   { background-position: 0% 50%; }
        50%  { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    @keyframes borderGlow {
        0%, 100% { border-color: rgba(102, 126, 234, 0.3); box-shadow: 0 0 15px rgba(102, 126, 234, 0.1); }
        50%      { border-color: rgba(102, 126, 234, 0.8); box-shadow: 0 0 25px rgba(102, 126, 234, 0.25); }
    }
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50%      { transform: translateY(-10px); }
    }
    @keyframes countUp {
        from { opacity: 0; transform: translateY(10px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes typing {
        from { width: 0; }
        to   { width: 100%; }
    }
    @keyframes blink {
        50% { border-color: transparent; }
    }
    @keyframes rotateIn {
        from { opacity: 0; transform: rotate(-10deg) scale(0.9); }
        to   { opacity: 1; transform: rotate(0) scale(1); }
    }
    @keyframes ripple {
        0%   { transform: scale(0.8); opacity: 1; }
        100% { transform: scale(2.4); opacity: 0; }
    }
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(50px); }
        to   { opacity: 1; transform: translateX(0); }
    }

    /* Stagger delays */
    .stagger-1 { animation-delay: 0.1s !important; }
    .stagger-2 { animation-delay: 0.2s !important; }
    .stagger-3 { animation-delay: 0.3s !important; }
    .stagger-4 { animation-delay: 0.4s !important; }
    .stagger-5 { animation-delay: 0.5s !important; }
    .stagger-6 { animation-delay: 0.6s !important; }
    .stagger-7 { animation-delay: 0.7s !important; }
    .stagger-8 { animation-delay: 0.8s !important; }

    /* ==================== GRADIENT TEXT ==================== */
    .gradient-text {
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
    }
    .gradient-text-accent {
        background: var(--gradient-accent);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 700;
    }

    /* ==================== SECTION HEADER ==================== */
    .section-header {
        font-size: 1.8rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        animation: fadeInLeft 0.6s ease-out both;
    }
    .section-subheader {
        font-size: 1rem;
        color: var(--text-secondary);
        margin-bottom: 1.5rem;
        animation: fadeInLeft 0.6s ease-out 0.1s both;
    }

    /* ==================== METRIC CARDS ==================== */
    .metric-card {
        background: var(--bg-card);
        border: 1px solid var(--border-card);
        border-radius: var(--radius-lg);
        padding: 24px;
        text-align: center;
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        animation: fadeInUp 0.6s ease-out both;
        position: relative;
        overflow: hidden;
    }
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        background: var(--gradient-primary);
        border-radius: var(--radius-lg) var(--radius-lg) 0 0;
    }
    .metric-card:hover {
        transform: translateY(-5px);
        border-color: rgba(102, 126, 234, 0.4);
        box-shadow: 0 12px 40px rgba(102, 126, 234, 0.15);
    }
    .metric-card .metric-icon {
        font-size: 2rem;
        margin-bottom: 8px;
    }
    .metric-card .metric-value {
        font-size: 2rem;
        font-weight: 800;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.2;
        animation: countUp 0.8s ease-out both;
    }
    .metric-card .metric-label {
        font-size: 0.85rem;
        color: var(--text-secondary);
        margin-top: 4px;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    /* ==================== GLASS CONTAINER ==================== */
    .glass-container {
        background: var(--bg-card);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: var(--radius-lg);
        border: 1px solid var(--border-card);
        padding: 24px;
        margin: 16px 0;
        animation: fadeInUp 0.6s ease-out both;
        transition: border-color 0.3s ease, box-shadow 0.3s ease;
    }
    .glass-container:hover {
        border-color: rgba(102, 126, 234, 0.3);
        box-shadow: 0 4px 20px rgba(102, 126, 234, 0.08);
    }

    /* ==================== HERO SECTION ==================== */
    .hero-container {
        text-align: center;
        padding: 60px 20px;
        animation: fadeIn 1s ease-out;
    }
    .hero-title {
        font-size: 3.5rem;
        font-weight: 900;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 16px;
        animation: fadeInUp 0.8s ease-out both;
        line-height: 1.2;
    }
    .hero-subtitle {
        font-size: 1.2rem;
        color: var(--text-secondary);
        max-width: 600px;
        margin: 0 auto 40px;
        animation: fadeInUp 0.8s ease-out 0.2s both;
        line-height: 1.6;
    }

    /* ==================== UPLOAD AREA ==================== */
    .upload-area {
        border: 2px dashed rgba(102, 126, 234, 0.4);
        border-radius: var(--radius-lg);
        padding: 60px 40px;
        text-align: center;
        background: rgba(102, 126, 234, 0.05);
        transition: all 0.3s ease;
        animation: fadeInUp 0.8s ease-out 0.4s both;
    }
    .upload-area:hover {
        border-color: var(--primary);
        background: rgba(102, 126, 234, 0.1);
        animation: borderGlow 2s infinite;
    }
    .upload-icon {
        font-size: 3rem;
        margin-bottom: 16px;
        animation: float 3s ease-in-out infinite;
    }

    /* ==================== FEATURE CARDS ==================== */
    .feature-card {
        background: var(--bg-card);
        border: 1px solid var(--border-card);
        border-radius: var(--radius-md);
        padding: 20px;
        text-align: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        animation: fadeInUp 0.6s ease-out both;
        min-height: 140px;
    }
    .feature-card:hover {
        transform: translateY(-6px);
        border-color: rgba(102, 126, 234, 0.5);
        box-shadow: 0 16px 48px rgba(102, 126, 234, 0.2);
    }
    .feature-card .feature-icon {
        font-size: 2.2rem;
        margin-bottom: 10px;
    }
    .feature-card .feature-title {
        font-size: 0.95rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 6px;
    }
    .feature-card .feature-desc {
        font-size: 0.78rem;
        color: var(--text-secondary);
        line-height: 1.4;
    }

    /* ==================== DATA TABLE ==================== */
    .stDataFrame {
        border-radius: var(--radius-md) !important;
        animation: fadeIn 0.5s ease-out both;
    }
    .stDataFrame [data-testid="stDataFrameResizable"] {
        border-radius: var(--radius-md);
        overflow: hidden;
    }

    /* ==================== TAB STYLING ==================== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: var(--bg-card);
        border-radius: var(--radius-md);
        padding: 4px;
        border: 1px solid var(--border-card);
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: var(--radius-sm);
        padding: 10px 20px;
        font-weight: 600;
        font-size: 0.9rem;
    }
    .stTabs [aria-selected="true"] {
        background: var(--gradient-primary) !important;
        color: white !important;
    }

    /* ==================== PROGRESS BAR ==================== */
    .progress-bar-container {
        background: rgba(255, 255, 255, 0.08);
        border-radius: 10px;
        overflow: hidden;
        height: 10px;
        margin: 6px 0;
    }
    .progress-bar-fill {
        height: 100%;
        border-radius: 10px;
        transition: width 1.2s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    .progress-bar-fill::after {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: linear-gradient(
            90deg,
            rgba(255,255,255,0) 0%,
            rgba(255,255,255,0.15) 50%,
            rgba(255,255,255,0) 100%
        );
        background-size: 200% 100%;
        animation: shimmer 2s infinite;
    }

    /* ==================== BADGES ==================== */
    .badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    .badge-success {
        background: rgba(0, 200, 83, 0.15);
        color: var(--success);
        border: 1px solid rgba(0, 200, 83, 0.3);
    }
    .badge-warning {
        background: rgba(255, 109, 0, 0.15);
        color: var(--warning);
        border: 1px solid rgba(255, 109, 0, 0.3);
    }
    .badge-error {
        background: rgba(255, 23, 68, 0.15);
        color: var(--error);
        border: 1px solid rgba(255, 23, 68, 0.3);
    }
    .badge-info {
        background: rgba(102, 126, 234, 0.15);
        color: var(--primary);
        border: 1px solid rgba(102, 126, 234, 0.3);
    }

    /* ==================== SIDEBAR ==================== */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0e1117 0%, #141926 50%, #1a1f2e 100%);
        border-right: 1px solid var(--border-card);
    }
    section[data-testid="stSidebar"] .block-container {
        padding-top: 1rem;
    }
    .sidebar-header {
        text-align: center;
        padding: 20px 10px 10px;
        animation: fadeInUp 0.6s ease-out both;
    }
    .sidebar-logo {
        font-size: 2.5rem;
        margin-bottom: 4px;
        animation: pulse 3s ease-in-out infinite;
    }
    .sidebar-title {
        font-size: 1.4rem;
        font-weight: 800;
        background: var(--gradient-primary);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    .sidebar-subtitle {
        font-size: 0.75rem;
        color: var(--text-secondary);
        margin-top: 2px;
        letter-spacing: 1px;
        text-transform: uppercase;
    }

    /* ==================== DIVIDERS ==================== */
    .gradient-divider {
        height: 2px;
        background: var(--gradient-primary);
        border: none;
        border-radius: 1px;
        margin: 24px 0;
        opacity: 0.4;
    }
    .gradient-divider-sm {
        height: 1px;
        background: var(--gradient-primary);
        border: none;
        border-radius: 1px;
        margin: 12px 0;
        opacity: 0.3;
    }

    /* ==================== INFO BOX ==================== */
    .info-box {
        background: rgba(102, 126, 234, 0.08);
        border-left: 4px solid var(--primary);
        border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
        padding: 16px 20px;
        margin: 12px 0;
        animation: fadeInLeft 0.5s ease-out both;
    }
    .info-box p {
        margin: 0;
        color: var(--text-primary);
        font-size: 0.9rem;
        line-height: 1.5;
    }

    .warning-box {
        background: rgba(255, 109, 0, 0.08);
        border-left: 4px solid var(--warning);
        border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
        padding: 16px 20px;
        margin: 12px 0;
        animation: fadeInLeft 0.5s ease-out both;
    }
    .warning-box p {
        margin: 0;
        color: var(--text-primary);
        font-size: 0.9rem;
    }

    .success-box {
        background: rgba(0, 200, 83, 0.08);
        border-left: 4px solid var(--success);
        border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
        padding: 16px 20px;
        margin: 12px 0;
        animation: fadeInLeft 0.5s ease-out both;
    }
    .success-box p {
        margin: 0;
        color: var(--text-primary);
        font-size: 0.9rem;
    }

    /* ==================== STAT TABLE ==================== */
    .stat-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        border-radius: var(--radius-md);
        overflow: hidden;
        animation: fadeInUp 0.6s ease-out both;
    }
    .stat-table th {
        background: rgba(102, 126, 234, 0.15);
        color: var(--primary);
        padding: 12px 16px;
        text-align: left;
        font-weight: 700;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        border-bottom: 1px solid var(--border-card);
    }
    .stat-table td {
        padding: 10px 16px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.04);
        color: var(--text-primary);
        font-size: 0.9rem;
    }
    .stat-table tr {
        transition: background 0.2s ease;
    }
    .stat-table tr:hover {
        background: rgba(102, 126, 234, 0.05);
    }
    .stat-table tr:last-child td {
        border-bottom: none;
    }

    /* ==================== CHIP/TAG ==================== */
    .chip {
        display: inline-block;
        padding: 4px 10px;
        border-radius: 16px;
        font-size: 0.72rem;
        font-weight: 600;
        margin: 2px 3px;
        background: rgba(102, 126, 234, 0.12);
        color: var(--primary);
        border: 1px solid rgba(102, 126, 234, 0.2);
        transition: all 0.2s ease;
    }
    .chip:hover {
        background: rgba(102, 126, 234, 0.2);
        transform: translateY(-1px);
    }

    /* ==================== SCROLLBAR ==================== */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: transparent; }
    ::-webkit-scrollbar-thumb {
        background: rgba(102, 126, 234, 0.3);
        border-radius: 3px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(102, 126, 234, 0.5);
    }

    /* ==================== EXPANDER ==================== */
    .streamlit-expanderHeader {
        font-weight: 600;
        font-size: 0.95rem;
        border-radius: var(--radius-sm);
        transition: color 0.2s ease;
    }
    details[open] .streamlit-expanderHeader {
        color: var(--primary);
    }

    /* ==================== HIDE BRANDING ==================== */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }

    /* ==================== RESPONSIVE ==================== */
    @media (max-width: 768px) {
        .hero-title { font-size: 2rem; }
        .hero-subtitle { font-size: 1rem; }
        .metric-card { padding: 16px; }
        .metric-card .metric-value { font-size: 1.5rem; }
        .section-header { font-size: 1.4rem; }
        .feature-card { min-height: auto; }
    }
</style>
"""
