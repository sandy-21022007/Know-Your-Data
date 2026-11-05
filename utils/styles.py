"""
Know-Your-Data — Custom CSS Styles & Futuristic Theme System.
Executive Dark Mode with Cyber-Cyan & Electric Indigo Accents.
High-End Micro-Interactions, 3D Tilt, Neural Core, and Glassmorphism.
"""

import streamlit as st


def inject_custom_css():
    """Inject all custom CSS styles, animations, and typography into the Streamlit app."""
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


CUSTOM_CSS = """
<style>
    /* ==================== TYPOGRAPHY & FONTS ==================== */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&display=swap');

    /* ==================== ROOT VARIABLES ==================== */
    :root {
        /* Enterprise Light Palette */
        --bg-void: #F5F7FB;
        --bg-darker: #F5F7FB;
        --bg-surface: rgba(255, 255, 255, 0.9);
        --bg-surface-elevated: rgba(248, 250, 252, 0.95);
        --bg-surface-card: rgba(255, 255, 255, 0.95);
        --bg-glass-heavy: rgba(245, 247, 251, 0.95);

        /* Professional Accents */
        --cyber-cyan: #4F46E5;
        --electric-indigo: #0891B2;
        --neon-violet: #8B5CF6;
        --emerald-success: #16A34A;
        --amber-warning: #D97706;
        --crimson-error: #DC2626;

        /* Backward-compatible aliases */
        --primary: #4F46E5;
        --primary-dark: #4338CA;
        --secondary: #0891B2;
        --accent: #8B5CF6;
        --success: #16A34A;
        --warning: #D97706;
        --error: #DC2626;

        /* Gradients */
        --gradient-cyber: linear-gradient(135deg, #4F46E5 0%, #0891B2 100%);
        --gradient-neural: linear-gradient(135deg, #4F46E5 0%, #0891B2 50%, #8B5CF6 100%);
        --gradient-emerald: linear-gradient(135deg, #16A34A 0%, #15803D 100%);
        --gradient-amber: linear-gradient(135deg, #D97706 0%, #B45309 100%);
        --gradient-glass-border: linear-gradient(135deg, rgba(79, 70, 229, 0.2), rgba(8, 145, 178, 0.1), rgba(139, 92, 246, 0.15));

        /* Borders & Glass */
        --border-glass: rgba(79, 70, 229, 0.1);
        --border-luminous: rgba(79, 70, 229, 0.3);
        --border-subtle: rgba(0, 0, 0, 0.06);

        /* Shadows & Glows */
        --glow-cyan: 0 0 15px rgba(79, 70, 229, 0.15);
        --glow-indigo: 0 0 15px rgba(8, 145, 178, 0.15);
        --glow-neural: 0 0 20px rgba(79, 70, 229, 0.1), 0 0 40px rgba(8, 145, 178, 0.05);
        --shadow-elevation: 0 4px 12px rgba(0, 0, 0, 0.08), 0 0 1px 1px rgba(0, 0, 0, 0.04);

        /* Typography */
        --text-primary: #17243A;
        --text-secondary: #64748B;
        --text-muted: #9CA3AF;
        --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        --font-mono: 'JetBrains Mono', 'Fira Code', monospace;

        --radius-xl: 12px;
        --radius-lg: 10px;
        --radius-md: 8px;
        --radius-sm: 6px;
    }

    /* ==================== GLOBAL APP CANVAS ==================== */
    html, body, [class*="css"], .stApp {
        font-family: var(--font-sans);
        color: var(--text-primary);
        background-color: var(--bg-void) !important;
    }

    .stApp {
        background-color: #F5F7FB !important;
        background-image: 
            radial-gradient(circle at 50% -10%, rgba(79, 70, 229, 0.03) 0%, transparent 45%),
            radial-gradient(circle at 85% 30%, rgba(8, 145, 178, 0.02) 0%, transparent 40%),
            radial-gradient(circle at 15% 70%, rgba(139, 92, 246, 0.02) 0%, transparent 40%);
        background-size: 100% 100%, 100% 100%, 100% 100%;
        background-attachment: fixed;
    }

    .main .block-container {
        padding-top: 1.8rem;
        padding-bottom: 3rem;
        max-width: 1280px;
    }

    /* Code & Monospace styling */
    code, pre, .font-mono, [data-testid="stMetricValue"] {
        font-family: var(--font-mono) !important;
    }

    /* ==================== KEYFRAME ANIMATIONS ==================== */
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(24px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-20px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInLeft {
        from { opacity: 0; transform: translateX(-24px); }
        to   { opacity: 1; transform: translateX(0); }
    }
    @keyframes fadeInRight {
        from { opacity: 0; transform: translateX(24px); }
        to   { opacity: 1; transform: translateX(0); }
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to   { opacity: 1; }
    }
    @keyframes scaleIn {
        from { opacity: 0; transform: scale(0.92); }
        to   { opacity: 1; transform: scale(1); }
    }
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        50%      { transform: translateY(-10px) rotate(1deg); }
    }
    @keyframes pulseGlow {
        0%, 100% {
            box-shadow: 0 0 12px rgba(99, 102, 241, 0.15), inset 0 0 8px rgba(99, 102, 241, 0.03);
            border-color: rgba(99, 102, 241, 0.25);
        }
        50% {
            box-shadow: 0 0 20px rgba(99, 102, 241, 0.25), inset 0 0 12px rgba(99, 102, 241, 0.08);
            border-color: rgba(99, 102, 241, 0.4);
        }
    }
    @keyframes laserScan {
        0% {
            top: 0%;
            opacity: 0;
        }
        12% {
            opacity: 1;
        }
        88% {
            opacity: 1;
        }
        100% {
            top: 100%;
            opacity: 0;
        }
    }
    @keyframes spinClockwise {
        from { transform: rotate(0deg); }
        to   { transform: rotate(360deg); }
    }
    @keyframes spinCounterClockwise {
        from { transform: rotate(360deg); }
        to   { transform: rotate(0deg); }
    }
    @keyframes corePulse {
        0%, 100% { transform: scale(0.92); opacity: 0.85; filter: drop-shadow(0 0 10px #6366F1); }
        50%      { transform: scale(1.1); opacity: 1; filter: drop-shadow(0 0 20px #6366F1) drop-shadow(0 0 30px #06B6D4); }
    }
    @keyframes shimmerSweep {
        0%   { background-position: -200% 0; }
        100% { background-position: 200% 0; }
    }
    @keyframes terminalBlink {
        0%, 49%   { opacity: 1; }
        50%, 100% { opacity: 0; }
    }
    @keyframes floatOrb {
        0%   { transform: translate(0, 0) scale(1); }
        50%  { transform: translate(30px, -40px) scale(1.1); }
        100% { transform: translate(-20px, 20px) scale(0.95); }
    }

    /* Stagger Delays */
    .stagger-1 { animation-delay: 0.06s !important; }
    .stagger-2 { animation-delay: 0.12s !important; }
    .stagger-3 { animation-delay: 0.18s !important; }
    .stagger-4 { animation-delay: 0.24s !important; }
    .stagger-5 { animation-delay: 0.30s !important; }
    .stagger-6 { animation-delay: 0.36s !important; }
    .stagger-7 { animation-delay: 0.42s !important; }
    .stagger-8 { animation-delay: 0.48s !important; }

    /* ==================== AMBIENT PARTICLES / ORBS ==================== */
    .cyber-ambient-orb-1 {
        position: fixed;
        top: 10%;
        right: 15%;
        width: 380px;
        height: 380px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(79, 70, 229, 0.04) 0%, transparent 70%);
        filter: blur(80px);
        pointer-events: none;
        z-index: 0;
        animation: floatOrb 22s ease-in-out infinite alternate;
    }
    .cyber-ambient-orb-2 {
        position: fixed;
        bottom: 15%;
        left: 10%;
        width: 440px;
        height: 440px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(8, 145, 178, 0.03) 0%, transparent 70%);
        filter: blur(100px);
        pointer-events: none;
        z-index: 0;
        animation: floatOrb 26s ease-in-out infinite alternate-reverse;
    }

    /* ==================== GRADIENTS & TEXT ==================== */
    .gradient-text, .cyber-gradient-text {
        background: var(--gradient-cyber);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
        letter-spacing: -0.02em;
    }
    .gradient-text-neural {
        background: var(--gradient-neural);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 800;
        letter-spacing: -0.02em;
    }
    .gradient-text-accent {
        background: linear-gradient(135deg, #00F2FE 0%, #8B5CF6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 700;
    }

    /* Section Headers */
    .section-header {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 0.4rem;
        color: var(--text-primary);
        letter-spacing: -0.01em;
        display: flex;
        align-items: center;
        gap: 12px;
        animation: fadeInLeft 0.5s ease-out both;
    }
    .section-subheader {
        font-size: 0.875rem;
        color: var(--text-secondary);
        margin-bottom: 1.6rem;
        font-weight: 400;
        letter-spacing: 0.01em;
        animation: fadeInLeft 0.5s ease-out 0.1s both;
    }

    /* ==================== GLASSMORPHISM PANELS ==================== */
    .glass-container, .cyber-panel {
        background: var(--bg-surface);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid var(--border-glass);
        border-radius: var(--radius-lg);
        padding: 24px;
        margin: 18px 0;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        transition: all 0.25s ease;
        position: relative;
        overflow: hidden;
        animation: fadeInUp 0.5s ease-out both;
    }
    .glass-container:hover, .cyber-panel:hover {
        border-color: rgba(99, 102, 241, 0.3);
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.4);
    }

    /* ==================== PROFESSIONAL METRIC CARDS ==================== */
    .metric-card {
        background: var(--bg-surface-card);
        border: 1px solid var(--border-glass);
        border-radius: var(--radius-lg);
        padding: 20px 18px;
        text-align: left;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        transition: all 0.2s ease;
        animation: fadeInUp 0.55s ease-out both;
        position: relative;
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
    }
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: var(--gradient-cyber);
        opacity: 0.6;
        transition: opacity 0.2s ease;
    }
    .metric-card:hover {
        transform: translateY(-2px);
        border-color: rgba(99, 102, 241, 0.3);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }
    .metric-card:hover::before {
        opacity: 1;
    }
    .metric-card .metric-header-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 12px;
    }
    .metric-card .metric-icon-badge {
        width: 36px;
        height: 36px;
        border-radius: 8px;
        background: rgba(99, 102, 241, 0.08);
        border: 1px solid rgba(99, 102, 241, 0.15);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.2rem;
    }
    .metric-card .metric-delta-tag {
        font-family: var(--font-mono);
        font-size: 0.7rem;
        font-weight: 600;
        padding: 2px 8px;
        border-radius: 6px;
        background: rgba(34, 197, 94, 0.1);
        color: #22C55E;
        border: 1px solid rgba(34, 197, 94, 0.2);
    }
    .metric-card .metric-value {
        font-family: var(--font-mono);
        font-size: 1.75rem;
        font-weight: 700;
        color: var(--text-primary);
        line-height: 1.2;
        letter-spacing: -0.02em;
    }
    .metric-card .metric-label {
        font-size: 0.75rem;
        color: var(--text-secondary);
        margin-top: 6px;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }

    /* ==================== HERO SECTION ==================== */
    .hero-container {
        text-align: center;
        padding: 45px 20px 30px;
        animation: fadeIn 0.6s ease-out;
        position: relative;
    }
    .hero-hud-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 6px 16px;
        border-radius: 20px;
        background: rgba(99, 102, 241, 0.08);
        border: 1px solid rgba(99, 102, 241, 0.2);
        color: var(--cyber-cyan);
        font-family: var(--font-mono);
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.04em;
        margin-bottom: 20px;
        animation: fadeInDown 0.5s ease-out both;
    }
    .hero-hud-dot {
        width: 6px;
        height: 6px;
        border-radius: 50%;
        background: var(--cyber-cyan);
        animation: terminalBlink 1.4s infinite;
    }
    .hero-title {
        font-size: 2.25rem;
        font-weight: 700;
        color: var(--text-primary);
        margin-bottom: 16px;
        animation: fadeInUp 0.6s ease-out both;
        line-height: 1.2;
        letter-spacing: -0.02em;
    }
    .hero-subtitle {
        font-size: 0.95rem;
        color: var(--text-secondary);
        max-width: 680px;
        margin: 0 auto 30px;
        animation: fadeInUp 0.6s ease-out 0.1s both;
        line-height: 1.6;
        font-weight: 400;
    }

    /* ==================== PROFESSIONAL UPLOAD ZONE ==================== */
    .dropzone-cyber {
        position: relative;
        background: var(--bg-surface-card);
        border: 2px dashed var(--border-glass);
        border-radius: var(--radius-lg);
        padding: 40px 30px;
        text-align: center;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        overflow: hidden;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
        transition: all 0.2s ease;
    }
    .dropzone-cyber:hover {
        border-color: rgba(99, 102, 241, 0.4);
        background: rgba(99, 102, 241, 0.03);
    }

    .dropzone-icon {
        font-size: 2.5rem;
        margin-bottom: 16px;
        display: inline-block;
        color: var(--cyber-cyan);
    }
    .dropzone-title {
        color: var(--text-primary);
        font-size: 1.15rem;
        font-weight: 600;
        margin-bottom: 8px;
        letter-spacing: -0.01em;
    }
    .dropzone-subtitle {
        color: var(--text-secondary);
        font-size: 0.875rem;
        margin-bottom: 18px;
    }
    .dropzone-chips {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 8px;
        margin-top: 14px;
    }
    .dropzone-chip {
        font-family: var(--font-mono);
        font-size: 0.7rem;
        font-weight: 500;
        padding: 4px 10px;
        border-radius: 6px;
        background: rgba(255, 255, 255, 0.04);
        color: var(--text-secondary);
        border: 1px solid var(--border-glass);
        letter-spacing: 0.02em;
    }

    /* Style Streamlit Native File Uploader to blend into Theme */
    [data-testid="stFileUploader"] {
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
    }
    [data-testid="stFileUploader"] section {
        background: var(--bg-surface-card) !important;
        border: 2px dashed var(--border-glass) !important;
        border-radius: var(--radius-lg) !important;
        padding: 24px !important;
        transition: all 0.2s ease !important;
    }
    [data-testid="stFileUploader"] section:hover {
        border-color: rgba(99, 102, 241, 0.4) !important;
        background: rgba(99, 102, 241, 0.03) !important;
    }

    /* ==================== LOADING STATE ==================== */
    .neural-core-wrapper {
        text-align: center;
        padding: 40px 20px;
        position: relative;
    }
    .neural-rings-container {
        position: relative;
        width: 120px;
        height: 120px;
        margin: 0 auto 30px;
    }
    .neural-ring-outer {
        position: absolute;
        inset: 0;
        border: 2px dashed rgba(99, 102, 241, 0.3);
        border-radius: 50%;
        animation: spinClockwise 20s linear infinite;
    }
    .neural-ring-middle {
        position: absolute;
        inset: 20px;
        border: 2px dotted rgba(6, 182, 212, 0.4);
        border-radius: 50%;
        animation: spinCounterClockwise 15s linear infinite;
    }
    .neural-ring-inner {
        position: absolute;
        inset: 40px;
        border: 2px solid rgba(139, 92, 246, 0.3);
        border-top-color: transparent;
        border-radius: 50%;
        animation: spinClockwise 10s linear infinite;
    }
    .neural-core-center {
        position: absolute;
        inset: 50px;
        border-radius: 50%;
        background: radial-gradient(circle, #6366F1 0%, #06B6D4 60%, #8B5CF6 100%);
        animation: corePulse 3s ease-in-out infinite;
        box-shadow: 0 0 15px rgba(99, 102, 241, 0.3);
    }

    /* Terminal Hacker Logs */
    .terminal-box {
        background: var(--bg-darker);
        border: 1px solid var(--border-glass);
        border-radius: var(--radius-md);
        padding: 0;
        max-width: 680px;
        margin: 0 auto;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        overflow: hidden;
        text-align: left;
    }
    .terminal-header {
        background: var(--bg-surface-card);
        border-bottom: 1px solid var(--border-glass);
        padding: 10px 16px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .terminal-dots {
        display: flex;
        gap: 6px;
    }
    .terminal-dot {
        width: 10px;
        height: 10px;
        border-radius: 50%;
    }
    .terminal-dot.red { background: #EF4444; }
    .terminal-dot.yellow { background: #F59E0B; }
    .terminal-dot.green { background: #22C55E; }
    .terminal-title {
        font-family: var(--font-mono);
        font-size: 0.75rem;
        color: var(--text-secondary);
        font-weight: 600;
        letter-spacing: 0.05em;
    }
    .terminal-body {
        padding: 16px 20px;
        font-family: var(--font-mono);
        font-size: 0.82rem;
        color: var(--text-primary);
        line-height: 1.7;
        min-height: 140px;
    }
    .terminal-line {
        margin-bottom: 4px;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .terminal-time {
        color: var(--text-muted);
        font-size: 0.72rem;
    }
    .terminal-tag {
        color: var(--cyber-cyan);
        font-weight: 700;
    }
    .cursor-blink {
        display: inline-block;
        width: 8px;
        height: 14px;
        background: var(--cyber-cyan);
        vertical-align: middle;
        animation: terminalBlink 1s infinite;
        margin-left: 4px;
    }

    /* ==================== SKELETON SHIMMER LOADERS ==================== */
    .skeleton-box {
        background: linear-gradient(90deg, rgba(255, 255, 255, 0.04) 25%, rgba(99, 102, 241, 0.08) 50%, rgba(255, 255, 255, 0.04) 75%);
        background-size: 200% 100%;
        animation: shimmerSweep 2s infinite;
        border-radius: 8px;
    }
    .skeleton-metric {
        height: 90px;
        border-radius: var(--radius-lg);
        background: linear-gradient(90deg, rgba(14, 20, 32, 0.8) 25%, rgba(99, 102, 241, 0.06) 50%, rgba(14, 20, 32, 0.8) 75%);
        background-size: 200% 100%;
        animation: shimmerSweep 2.2s infinite;
        border: 1px solid var(--border-glass);
    }

    /* ==================== FEATURE CARDS GRID ==================== */
    .feature-card {
        background: var(--bg-surface-card);
        border: 1px solid var(--border-glass);
        border-radius: var(--radius-lg);
        padding: 24px 20px;
        text-align: center;
        transition: all 0.2s ease;
        animation: fadeInUp 0.5s ease-out both;
        min-height: 155px;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        position: relative;
        overflow: hidden;
    }
    .feature-card::before {
        content: '';
        position: absolute;
        inset: 0;
        background: radial-gradient(circle at 50% 0%, rgba(99, 102, 241, 0.06), transparent 70%);
        opacity: 0;
        transition: opacity 0.2s ease;
    }
    .feature-card:hover {
        transform: translateY(-4px);
        border-color: rgba(99, 102, 241, 0.3);
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.3);
    }
    .feature-card:hover::before {
        opacity: 1;
    }
    .feature-card .feature-icon {
        font-size: 2rem;
        margin-bottom: 12px;
        display: inline-block;
        transition: transform 0.2s ease;
    }
    .feature-card:hover .feature-icon {
        transform: scale(1.1);
    }
    .feature-card .feature-title {
        font-size: 0.95rem;
        font-weight: 600;
        color: var(--text-primary);
        margin-bottom: 6px;
        letter-spacing: -0.01em;
    }
    .feature-card .feature-desc {
        font-size: 0.8rem;
        color: var(--text-secondary);
        line-height: 1.45;
    }

    /* ==================== BUTTONS & INTERACTION ==================== */
    .stButton > button {
        background: rgba(99, 102, 241, 0.1) !important;
        color: var(--text-primary) !important;
        border: 1px solid rgba(99, 102, 241, 0.3) !important;
        border-radius: var(--radius-md) !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        letter-spacing: 0.01em !important;
        padding: 10px 24px !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2) !important;
    }
    .stButton > button:hover {
        background: rgba(99, 102, 241, 0.15) !important;
        border-color: rgba(99, 102, 241, 0.5) !important;
        transform: translateY(-1px) !important;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3) !important;
    }
    .stButton > button:active {
        transform: scale(0.98) !important;
    }

    /* Primary CTA Button */
    .btn-cyber-primary {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        background: var(--gradient-cyber);
        color: #0B1120 !important;
        font-weight: 600;
        font-size: 0.9rem;
        padding: 12px 28px;
        border-radius: var(--radius-md);
        border: none;
        box-shadow: 0 2px 8px rgba(99, 102, 241, 0.3);
        transition: all 0.2s ease;
        cursor: pointer;
        text-decoration: none;
    }
    .btn-cyber-primary:hover {
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.4);
        transform: translateY(-1px);
    }

    /* ==================== TABS STYLING ==================== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        background: var(--bg-surface-card) !important;
        border-radius: var(--radius-md) !important;
        padding: 4px !important;
        border: 1px solid var(--border-glass) !important;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: var(--radius-sm) !important;
        padding: 8px 16px !important;
        font-weight: 500 !important;
        font-size: 0.875rem !important;
        color: var(--text-secondary) !important;
        transition: all 0.2s ease !important;
    }
    .stTabs [aria-selected="true"] {
        background: rgba(99, 102, 241, 0.15) !important;
        color: var(--cyber-cyan) !important;
        font-weight: 600 !important;
        border: 1px solid rgba(99, 102, 241, 0.3) !important;
    }

    /* ==================== DATA TABLE STYLING ==================== */
    .stDataFrame {
        border-radius: var(--radius-lg) !important;
        border: 1px solid var(--border-glass) !important;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2) !important;
        overflow: hidden !important;
    }

    .stat-table {
        width: 100%;
        border-collapse: separate;
        border-spacing: 0;
        border-radius: var(--radius-md);
        overflow: hidden;
        animation: fadeInUp 0.5s ease-out both;
        background: var(--bg-surface-card);
        border: 1px solid var(--border-glass);
    }
    .stat-table th {
        background: rgba(99, 102, 241, 0.06);
        color: var(--cyber-cyan);
        padding: 12px 16px;
        text-align: left;
        font-family: var(--font-mono);
        font-weight: 600;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        border-bottom: 1px solid var(--border-glass);
    }
    .stat-table td {
        padding: 12px 16px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.04);
        color: var(--text-primary);
        font-size: 0.875rem;
    }
    .stat-table tr {
        transition: background 0.15s ease;
    }
    .stat-table tr:hover {
        background: rgba(99, 102, 241, 0.04);
    }
    .stat-table tr:last-child td {
        border-bottom: none;
    }

    /* ==================== PROGRESS BAR ==================== */
    .progress-bar-container {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 6px;
        overflow: hidden;
        height: 6px;
        margin: 6px 0;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    .progress-bar-fill {
        height: 100%;
        border-radius: 6px;
        transition: width 0.6s ease;
        position: relative;
        overflow: hidden;
    }
    .progress-bar-fill::after {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.3) 50%, transparent 100%);
        background-size: 200% 100%;
        animation: shimmerSweep 2s infinite;
    }

    /* ==================== HUD BADGES ==================== */
    .badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 4px 12px;
        border-radius: 16px;
        font-family: var(--font-mono);
        font-size: 0.7rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.04em;
        margin-right: 6px;
        margin-bottom: 4px;
    }
    .badge-primary, .badge-info {
        background: rgba(99, 102, 241, 0.1);
        color: var(--cyber-cyan);
        border: 1px solid rgba(99, 102, 241, 0.25);
    }
    .badge-secondary, .badge-accent {
        background: rgba(6, 182, 212, 0.1);
        color: var(--electric-indigo);
        border: 1px solid rgba(6, 182, 212, 0.25);
    }
    .badge-success {
        background: rgba(34, 197, 94, 0.1);
        color: #22C55E;
        border: 1px solid rgba(34, 197, 94, 0.25);
    }
    .badge-warning {
        background: rgba(245, 158, 11, 0.1);
        color: #F59E0B;
        border: 1px solid rgba(245, 158, 11, 0.25);
    }
    .badge-error {
        background: rgba(239, 68, 68, 0.1);
        color: #EF4444;
        border: 1px solid rgba(239, 68, 68, 0.25);
    }

    /* ==================== CALLOUT BOXES ==================== */
    .info-box, .warning-box, .success-box {
        border-radius: var(--radius-md);
        padding: 14px 18px;
        margin: 14px 0;
        animation: fadeInLeft 0.4s ease-out both;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
    }
    .info-box {
        background: rgba(99, 102, 241, 0.06);
        border-left: 3px solid var(--cyber-cyan);
        border-top: 1px solid rgba(99, 102, 241, 0.12);
        border-right: 1px solid rgba(99, 102, 241, 0.12);
        border-bottom: 1px solid rgba(99, 102, 241, 0.12);
    }
    .warning-box {
        background: rgba(245, 158, 11, 0.06);
        border-left: 3px solid var(--amber-warning);
        border-top: 1px solid rgba(245, 158, 11, 0.12);
        border-right: 1px solid rgba(245, 158, 11, 0.12);
        border-bottom: 1px solid rgba(245, 158, 11, 0.12);
    }
    .success-box {
        background: rgba(34, 197, 94, 0.06);
        border-left: 3px solid var(--emerald-success);
        border-top: 1px solid rgba(34, 197, 94, 0.12);
        border-right: 1px solid rgba(34, 197, 94, 0.12);
        border-bottom: 1px solid rgba(34, 197, 94, 0.12);
    }
    .info-box p, .warning-box p, .success-box p {
        margin: 0;
        font-size: 0.875rem;
        line-height: 1.55;
    }

    /* ==================== SIDEBAR ==================== */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #FFFFFF 0%, #F8FAFC 50%, #FFFFFF 100%) !important;
        border-right: 1px solid #E5E7EB !important;
        box-shadow: 2px 0 8px rgba(0, 0, 0, 0.06);
    }
    section[data-testid="stSidebar"] .block-container {
        padding-top: 1.2rem;
    }
    .sidebar-header {
        text-align: center;
        padding: 16px 8px 12px;
        animation: fadeInDown 0.5s ease-out both;
        position: relative;
    }
    .sidebar-logo {
        font-size: 2rem;
        margin-bottom: 6px;
        display: inline-block;
        color: var(--cyber-cyan);
    }
    .sidebar-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: var(--text-primary);
        letter-spacing: -0.01em;
    }
    .sidebar-subtitle {
        font-family: var(--font-mono);
        font-size: 0.65rem;
        color: var(--cyber-cyan);
        letter-spacing: 0.1em;
        text-transform: uppercase;
        margin-top: 2px;
        opacity: 0.85;
    }
    .sidebar-hud-status {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-family: var(--font-mono);
        font-size: 0.65rem;
        background: rgba(79, 70, 229, 0.08);
        border: 1px solid rgba(79, 70, 229, 0.2);
        color: var(--cyber-cyan);
        padding: 3px 10px;
        border-radius: 12px;
        margin-top: 8px;
    }

    /* ==================== DIVIDERS ==================== */
    .gradient-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent 0%, rgba(99, 102, 241, 0.3) 50%, transparent 100%);
        border: none;
        margin: 24px 0;
    }
    .gradient-divider-sm {
        height: 1px;
        background: linear-gradient(90deg, transparent 0%, rgba(99, 102, 241, 0.2) 50%, transparent 100%);
        border: none;
        margin: 12px 0;
    }

    /* ==================== SCROLLBARS ==================== */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: #F5F7FB; }
    ::-webkit-scrollbar-thumb {
        background: rgba(79, 70, 229, 0.2);
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(79, 70, 229, 0.35);
    }

    /* ==================== EXPANDER ==================== */
    .streamlit-expanderHeader {
        background: var(--bg-surface-card) !important;
        border: 1px solid var(--border-glass) !important;
        border-radius: var(--radius-md) !important;
        font-weight: 600 !important;
        font-size: 0.875rem !important;
        transition: all 0.2s ease !important;
    }
    details[open] .streamlit-expanderHeader {
        border-color: rgba(99, 102, 241, 0.3) !important;
        color: var(--cyber-cyan) !important;
    }

    /* ==================== HIDE STREAMLIT BRANDING ==================== */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    /* Keep header visible for sidebar toggle, but hide title */
    header [data-testid="stHeader"] > div {
        visibility: hidden;
    }
    /* Make the hamburger menu button visible */
    button[kind="header"] {
        visibility: visible !important;
        background: rgba(79, 70, 229, 0.1) !important;
        border: 1px solid rgba(79, 70, 229, 0.2) !important;
        color: #4F46E5 !important;
        border-radius: 8px !important;
        padding: 8px 12px !important;
        font-size: 14px !important;
        font-weight: 600 !important;
        transition: all 0.2s ease !important;
    }
    button[kind="header"]:hover {
        background: rgba(79, 70, 229, 0.15) !important;
        border-color: rgba(79, 70, 229, 0.3) !important;
        transform: translateY(-1px) !important;
    }

    /* ==================== RESPONSIVE ==================== */
    @media (max-width: 768px) {
        .hero-title { font-size: 2.2rem; }
        .hero-subtitle { font-size: 0.95rem; }
        .metric-card { padding: 16px; }
        .metric-card .metric-value { font-size: 1.6rem; }
        .section-header { font-size: 1.5rem; }
        .feature-card { min-height: auto; }
        .dropzone-cyber { padding: 30px 16px; }
    }
</style>
<!-- Subtle Ambient Background Light Orbs -->
<div class="cyber-ambient-orb-1"></div>
<div class="cyber-ambient-orb-2"></div>
"""
