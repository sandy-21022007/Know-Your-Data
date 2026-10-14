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
        /* Executive Dark Palette */
        --bg-void: #07090E;
        --bg-darker: #05070B;
        --bg-surface: rgba(12, 16, 26, 0.72);
        --bg-surface-elevated: rgba(18, 25, 40, 0.82);
        --bg-surface-card: rgba(14, 20, 32, 0.7);
        --bg-glass-heavy: rgba(7, 9, 14, 0.88);

        /* Luminous Cyber Accents */
        --cyber-cyan: #00F2FE;
        --electric-indigo: #4FACFE;
        --neon-violet: #8B5CF6;
        --emerald-success: #10B981;
        --amber-warning: #F59E0B;
        --crimson-error: #EF4444;

        /* Backward-compatible aliases */
        --primary: #00F2FE;
        --primary-dark: #00c4cf;
        --secondary: #4FACFE;
        --accent: #8B5CF6;
        --success: #10B981;
        --warning: #F59E0B;
        --error: #EF4444;

        /* Gradients */
        --gradient-cyber: linear-gradient(135deg, #00F2FE 0%, #4FACFE 100%);
        --gradient-neural: linear-gradient(135deg, #00F2FE 0%, #4FACFE 50%, #8B5CF6 100%);
        --gradient-emerald: linear-gradient(135deg, #10B981 0%, #059669 100%);
        --gradient-amber: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
        --gradient-glass-border: linear-gradient(135deg, rgba(0, 242, 254, 0.45), rgba(79, 172, 254, 0.1), rgba(139, 92, 246, 0.25));

        /* Borders & Glass */
        --border-glass: rgba(0, 242, 254, 0.14);
        --border-luminous: rgba(0, 242, 254, 0.4);
        --border-subtle: rgba(255, 255, 255, 0.08);

        /* Shadows & Glows */
        --glow-cyan: 0 0 25px rgba(0, 242, 254, 0.35);
        --glow-indigo: 0 0 25px rgba(79, 172, 254, 0.35);
        --glow-neural: 0 0 35px rgba(0, 242, 254, 0.2), 0 0 70px rgba(79, 172, 254, 0.1);
        --shadow-elevation: 0 20px 40px -15px rgba(0, 0, 0, 0.8), 0 0 1px 1px rgba(255, 255, 255, 0.06);

        /* Typography */
        --text-primary: #F8FAFC;
        --text-secondary: #94A3B8;
        --text-muted: #64748B;
        --font-sans: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
        --font-mono: 'JetBrains Mono', 'Fira Code', monospace;

        --radius-xl: 20px;
        --radius-lg: 16px;
        --radius-md: 12px;
        --radius-sm: 8px;
    }

    /* ==================== GLOBAL APP CANVAS ==================== */
    html, body, [class*="css"], .stApp {
        font-family: var(--font-sans);
        color: var(--text-primary);
        background-color: var(--bg-void) !important;
    }

    .stApp {
        background-color: #07090E !important;
        background-image: 
            radial-gradient(circle at 50% -10%, rgba(0, 242, 254, 0.09) 0%, transparent 45%),
            radial-gradient(circle at 85% 30%, rgba(79, 172, 254, 0.06) 0%, transparent 40%),
            radial-gradient(circle at 15% 70%, rgba(139, 92, 246, 0.05) 0%, transparent 40%),
            linear-gradient(rgba(0, 242, 254, 0.02) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 242, 254, 0.02) 1px, transparent 1px);
        background-size: 100% 100%, 100% 100%, 100% 100%, 40px 40px, 40px 40px;
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
            box-shadow: 0 0 20px rgba(0, 242, 254, 0.2), inset 0 0 15px rgba(0, 242, 254, 0.05);
            border-color: rgba(0, 242, 254, 0.3);
        }
        50% {
            box-shadow: 0 0 35px rgba(0, 242, 254, 0.45), inset 0 0 25px rgba(0, 242, 254, 0.15);
            border-color: rgba(0, 242, 254, 0.8);
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
        0%, 100% { transform: scale(0.92); opacity: 0.85; filter: drop-shadow(0 0 15px #00F2FE); }
        50%      { transform: scale(1.1); opacity: 1; filter: drop-shadow(0 0 35px #00F2FE) drop-shadow(0 0 60px #4FACFE); }
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
        background: radial-gradient(circle, rgba(0, 242, 254, 0.08) 0%, transparent 70%);
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
        background: radial-gradient(circle, rgba(79, 172, 254, 0.07) 0%, transparent 70%);
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
        font-size: 2rem;
        font-weight: 800;
        margin-bottom: 0.4rem;
        background: var(--gradient-cyber);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.025em;
        display: flex;
        align-items: center;
        gap: 12px;
        animation: fadeInLeft 0.5s ease-out both;
    }
    .section-subheader {
        font-size: 0.95rem;
        color: var(--text-secondary);
        margin-bottom: 1.6rem;
        font-weight: 400;
        letter-spacing: 0.01em;
        animation: fadeInLeft 0.5s ease-out 0.1s both;
    }

    /* ==================== GLASSMORPHISM PANELS ==================== */
    .glass-container, .cyber-panel {
        background: var(--bg-surface);
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        border: 1px solid var(--border-glass);
        border-radius: var(--radius-lg);
        padding: 24px;
        margin: 18px 0;
        box-shadow: 0 15px 35px -10px rgba(0, 0, 0, 0.7), inset 0 1px 0 rgba(255, 255, 255, 0.08);
        transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
        position: relative;
        overflow: hidden;
        animation: fadeInUp 0.5s ease-out both;
    }
    .glass-container:hover, .cyber-panel:hover {
        border-color: rgba(0, 242, 254, 0.35);
        box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.8), 0 0 20px rgba(0, 242, 254, 0.15);
    }

    /* ==================== 3D PERSPECTIVE METRIC CARDS ==================== */
    .metric-card {
        background: var(--bg-surface-card);
        border: 1px solid var(--border-glass);
        border-radius: var(--radius-lg);
        padding: 22px 20px;
        text-align: left;
        backdrop-filter: blur(20px);
        -webkit-backdrop-filter: blur(20px);
        transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
        animation: fadeInUp 0.55s ease-out both;
        position: relative;
        overflow: hidden;
        box-shadow: 0 12px 30px -10px rgba(0, 0, 0, 0.7), inset 0 1px 0 rgba(255, 255, 255, 0.08);
        perspective: 1000px;
        transform-style: preserve-3d;
    }
    .metric-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 2px;
        background: var(--gradient-cyber);
        box-shadow: 0 0 12px rgba(0, 242, 254, 0.7);
        opacity: 0.85;
        transition: opacity 0.3s ease;
    }
    .metric-card::after {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background: radial-gradient(400px circle at 50% 0%, rgba(0, 242, 254, 0.12), transparent 70%);
        opacity: 0;
        pointer-events: none;
        transition: opacity 0.35s ease;
    }
    .metric-card:hover {
        transform: translateY(-6px) scale(1.015);
        border-color: rgba(0, 242, 254, 0.45);
        box-shadow: 0 22px 50px -10px rgba(0, 0, 0, 0.85), 0 0 25px rgba(0, 242, 254, 0.25);
    }
    .metric-card:hover::after {
        opacity: 1;
    }
    .metric-card .metric-header-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 12px;
    }
    .metric-card .metric-icon-badge {
        width: 38px;
        height: 38px;
        border-radius: 10px;
        background: rgba(0, 242, 254, 0.08);
        border: 1px solid rgba(0, 242, 254, 0.2);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 1.25rem;
    }
    .metric-card .metric-delta-tag {
        font-family: var(--font-mono);
        font-size: 0.72rem;
        font-weight: 600;
        padding: 2px 8px;
        border-radius: 6px;
        background: rgba(16, 185, 129, 0.12);
        color: #10B981;
        border: 1px solid rgba(16, 185, 129, 0.25);
    }
    .metric-card .metric-value {
        font-family: var(--font-mono);
        font-size: 2.1rem;
        font-weight: 800;
        background: linear-gradient(180deg, #FFFFFF 0%, #E2E8F0 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        line-height: 1.2;
        letter-spacing: -0.03em;
        text-shadow: 0 2px 10px rgba(0, 0, 0, 0.5);
    }
    .metric-card .metric-label {
        font-size: 0.8rem;
        color: var(--text-secondary);
        margin-top: 6px;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.08em;
    }

    /* ==================== HERO SECTION ==================== */
    .hero-container {
        text-align: center;
        padding: 45px 20px 30px;
        animation: fadeIn 0.8s ease-out;
        position: relative;
    }
    .hero-hud-pill {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 6px 16px;
        border-radius: 30px;
        background: rgba(0, 242, 254, 0.06);
        border: 1px solid rgba(0, 242, 254, 0.25);
        color: var(--cyber-cyan);
        font-family: var(--font-mono);
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.06em;
        margin-bottom: 20px;
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.15);
        animation: fadeInDown 0.6s ease-out both;
    }
    .hero-hud-dot {
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: var(--cyber-cyan);
        box-shadow: 0 0 10px var(--cyber-cyan);
        animation: terminalBlink 1.4s infinite;
    }
    .hero-title {
        font-size: 3.8rem;
        font-weight: 900;
        background: var(--gradient-cyber);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin-bottom: 16px;
        animation: fadeInUp 0.7s ease-out both;
        line-height: 1.15;
        letter-spacing: -0.035em;
    }
    .hero-subtitle {
        font-size: 1.15rem;
        color: var(--text-secondary);
        max-width: 680px;
        margin: 0 auto 30px;
        animation: fadeInUp 0.7s ease-out 0.15s both;
        line-height: 1.6;
        font-weight: 400;
    }

    /* ==================== CYBER DRAG-AND-DROP INGESTION ZONE ==================== */
    .dropzone-cyber {
        position: relative;
        background: rgba(12, 17, 28, 0.75);
        border: 1px solid rgba(0, 242, 254, 0.28);
        border-radius: var(--radius-xl);
        padding: 50px 30px;
        text-align: center;
        backdrop-filter: blur(24px);
        -webkit-backdrop-filter: blur(24px);
        overflow: hidden;
        box-shadow: 0 20px 60px -15px rgba(0, 0, 0, 0.9), inset 0 0 30px rgba(0, 242, 254, 0.04);
        animation: pulseGlow 4s infinite, fadeInUp 0.7s ease-out 0.25s both;
        transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
    }
    .dropzone-cyber:hover {
        border-color: rgba(0, 242, 254, 0.7);
        transform: translateY(-3px);
    }
    /* Corner HUD brackets */
    .dropzone-cyber .hud-corner {
        position: absolute;
        width: 18px;
        height: 18px;
        border-color: var(--cyber-cyan);
        pointer-events: none;
    }
    .dropzone-cyber .hud-corner-tl { top: 12px; left: 12px; border-top: 2px solid var(--cyber-cyan); border-left: 2px solid var(--cyber-cyan); }
    .dropzone-cyber .hud-corner-tr { top: 12px; right: 12px; border-top: 2px solid var(--cyber-cyan); border-right: 2px solid var(--cyber-cyan); }
    .dropzone-cyber .hud-corner-bl { bottom: 12px; left: 12px; border-bottom: 2px solid var(--cyber-cyan); border-left: 2px solid var(--cyber-cyan); }
    .dropzone-cyber .hud-corner-br { bottom: 12px; right: 12px; border-bottom: 2px solid var(--cyber-cyan); border-right: 2px solid var(--cyber-cyan); }

    /* Laser Line Scanner Animation */
    .laser-scanner {
        position: absolute;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, transparent 0%, rgba(0, 242, 254, 0.8) 25%, #00F2FE 50%, rgba(79, 172, 254, 0.8) 75%, transparent 100%);
        box-shadow: 0 0 15px #00F2FE, 0 0 30px #4FACFE;
        pointer-events: none;
        animation: laserScan 2.8s cubic-bezier(0.4, 0, 0.2, 1) infinite;
        z-index: 2;
    }

    .dropzone-icon {
        font-size: 3.2rem;
        margin-bottom: 16px;
        display: inline-block;
        animation: float 3.5s ease-in-out infinite;
        filter: drop-shadow(0 0 20px rgba(0, 242, 254, 0.5));
    }
    .dropzone-title {
        color: #F8FAFC;
        font-size: 1.35rem;
        font-weight: 700;
        margin-bottom: 8px;
        letter-spacing: -0.01em;
    }
    .dropzone-subtitle {
        color: var(--text-secondary);
        font-size: 0.9rem;
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
        font-size: 0.72rem;
        font-weight: 600;
        padding: 4px 10px;
        border-radius: 6px;
        background: rgba(255, 255, 255, 0.04);
        color: #CBD5E1;
        border: 1px solid rgba(255, 255, 255, 0.08);
        letter-spacing: 0.04em;
    }

    /* Style Streamlit Native File Uploader to blend into Cyber Theme */
    [data-testid="stFileUploader"] {
        background: transparent !important;
        border: none !important;
        padding: 0 !important;
    }
    [data-testid="stFileUploader"] section {
        background: rgba(14, 20, 32, 0.6) !important;
        border: 1px dashed rgba(0, 242, 254, 0.3) !important;
        border-radius: var(--radius-lg) !important;
        padding: 24px !important;
        transition: all 0.3s ease !important;
    }
    [data-testid="stFileUploader"] section:hover {
        border-color: rgba(0, 242, 254, 0.8) !important;
        background: rgba(0, 242, 254, 0.05) !important;
        box-shadow: 0 0 25px rgba(0, 242, 254, 0.15) !important;
    }

    /* ==================== NEURAL CORE LOADING STATE ==================== */
    .neural-core-wrapper {
        text-align: center;
        padding: 40px 20px;
        position: relative;
    }
    .neural-rings-container {
        position: relative;
        width: 180px;
        height: 180px;
        margin: 0 auto 30px;
    }
    .neural-ring-outer {
        position: absolute;
        inset: 0;
        border: 2px dashed rgba(0, 242, 254, 0.4);
        border-radius: 50%;
        animation: spinClockwise 12s linear infinite;
        box-shadow: 0 0 25px rgba(0, 242, 254, 0.2);
    }
    .neural-ring-middle {
        position: absolute;
        inset: 20px;
        border: 2px dotted rgba(79, 172, 254, 0.6);
        border-radius: 50%;
        animation: spinCounterClockwise 8s linear infinite;
    }
    .neural-ring-inner {
        position: absolute;
        inset: 40px;
        border: 2px solid rgba(139, 92, 246, 0.5);
        border-top-color: transparent;
        border-radius: 50%;
        animation: spinClockwise 4s linear infinite;
    }
    .neural-core-center {
        position: absolute;
        inset: 60px;
        border-radius: 50%;
        background: radial-gradient(circle, #00F2FE 0%, #4FACFE 60%, #8B5CF6 100%);
        animation: corePulse 2s ease-in-out infinite;
        box-shadow: 0 0 35px #00F2FE;
    }

    /* Terminal Hacker Logs */
    .terminal-box {
        background: var(--bg-darker);
        border: 1px solid rgba(0, 242, 254, 0.2);
        border-radius: var(--radius-md);
        padding: 0;
        max-width: 680px;
        margin: 0 auto;
        box-shadow: 0 15px 40px rgba(0, 0, 0, 0.8), inset 0 0 15px rgba(0, 0, 0, 0.9);
        overflow: hidden;
        text-align: left;
    }
    .terminal-header {
        background: rgba(14, 20, 32, 0.8);
        border-bottom: 1px solid rgba(255, 255, 255, 0.06);
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
    .terminal-dot.green { background: #10B981; }
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
        color: #A7F3D0;
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
        background: linear-gradient(90deg, rgba(255, 255, 255, 0.04) 25%, rgba(0, 242, 254, 0.1) 50%, rgba(255, 255, 255, 0.04) 75%);
        background-size: 200% 100%;
        animation: shimmerSweep 1.8s infinite;
        border-radius: 8px;
    }
    .skeleton-metric {
        height: 90px;
        border-radius: var(--radius-lg);
        background: linear-gradient(90deg, rgba(14, 20, 32, 0.8) 25%, rgba(0, 242, 254, 0.08) 50%, rgba(14, 20, 32, 0.8) 75%);
        background-size: 200% 100%;
        animation: shimmerSweep 2s infinite;
        border: 1px solid var(--border-glass);
    }

    /* ==================== FEATURE CARDS GRID ==================== */
    .feature-card {
        background: var(--bg-surface-card);
        border: 1px solid var(--border-glass);
        border-radius: var(--radius-lg);
        padding: 24px 20px;
        text-align: center;
        transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
        animation: fadeInUp 0.5s ease-out both;
        min-height: 155px;
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        position: relative;
        overflow: hidden;
        perspective: 1000px;
    }
    .feature-card::before {
        content: '';
        position: absolute;
        inset: 0;
        background: radial-gradient(circle at 50% 0%, rgba(0, 242, 254, 0.08), transparent 70%);
        opacity: 0;
        transition: opacity 0.3s ease;
    }
    .feature-card:hover {
        transform: translateY(-8px) scale(1.02);
        border-color: rgba(0, 242, 254, 0.5);
        box-shadow: 0 20px 45px -10px rgba(0, 0, 0, 0.8), 0 0 30px rgba(0, 242, 254, 0.25);
    }
    .feature-card:hover::before {
        opacity: 1;
    }
    .feature-card .feature-icon {
        font-size: 2.2rem;
        margin-bottom: 12px;
        display: inline-block;
        transition: transform 0.3s ease;
    }
    .feature-card:hover .feature-icon {
        transform: scale(1.15) rotate(5deg);
    }
    .feature-card .feature-title {
        font-size: 1rem;
        font-weight: 700;
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
        background: linear-gradient(135deg, rgba(0, 242, 254, 0.12), rgba(79, 172, 254, 0.18)) !important;
        color: #F8FAFC !important;
        border: 1px solid rgba(0, 242, 254, 0.4) !important;
        border-radius: var(--radius-md) !important;
        font-weight: 600 !important;
        font-size: 0.92rem !important;
        letter-spacing: 0.02em !important;
        padding: 10px 24px !important;
        transition: all 0.25s cubic-bezier(0.16, 1, 0.3, 1) !important;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.1) !important;
    }
    .stButton > button:hover {
        background: var(--gradient-cyber) !important;
        color: #07090E !important;
        border-color: #00F2FE !important;
        transform: translateY(-2px) scale(1.02) !important;
        box-shadow: 0 8px 25px rgba(0, 242, 254, 0.45) !important;
    }
    .stButton > button:active {
        transform: scale(0.97) !important;
    }

    /* Primary CTA Button */
    .btn-cyber-primary {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 8px;
        background: var(--gradient-cyber);
        color: #07090E !important;
        font-weight: 700;
        font-size: 0.95rem;
        padding: 12px 28px;
        border-radius: var(--radius-md);
        border: none;
        box-shadow: 0 0 25px rgba(0, 242, 254, 0.4);
        transition: all 0.25s ease;
        cursor: pointer;
        text-decoration: none;
    }
    .btn-cyber-primary:hover {
        box-shadow: 0 0 40px rgba(0, 242, 254, 0.7);
        transform: translateY(-2px) scale(1.02);
    }

    /* ==================== TABS STYLING ==================== */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background: rgba(12, 16, 26, 0.8) !important;
        border-radius: var(--radius-md) !important;
        padding: 6px !important;
        border: 1px solid var(--border-glass) !important;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: var(--radius-sm) !important;
        padding: 10px 20px !important;
        font-weight: 600 !important;
        font-size: 0.9rem !important;
        color: var(--text-secondary) !important;
        transition: all 0.2s ease !important;
    }
    .stTabs [aria-selected="true"] {
        background: var(--gradient-cyber) !important;
        color: #07090E !important;
        font-weight: 700 !important;
        box-shadow: 0 4px 15px rgba(0, 242, 254, 0.35) !important;
    }

    /* ==================== DATA TABLE STYLING ==================== */
    .stDataFrame {
        border-radius: var(--radius-lg) !important;
        border: 1px solid var(--border-glass) !important;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6) !important;
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
        background: rgba(0, 242, 254, 0.08);
        color: var(--cyber-cyan);
        padding: 14px 18px;
        text-align: left;
        font-family: var(--font-mono);
        font-weight: 700;
        font-size: 0.82rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        border-bottom: 1px solid var(--border-glass);
    }
    .stat-table td {
        padding: 12px 18px;
        border-bottom: 1px solid rgba(255, 255, 255, 0.04);
        color: var(--text-primary);
        font-size: 0.88rem;
    }
    .stat-table tr {
        transition: background 0.2s ease;
    }
    .stat-table tr:hover {
        background: rgba(0, 242, 254, 0.04);
    }
    .stat-table tr:last-child td {
        border-bottom: none;
    }

    /* ==================== PROGRESS BAR ==================== */
    .progress-bar-container {
        background: rgba(255, 255, 255, 0.06);
        border-radius: 20px;
        overflow: hidden;
        height: 8px;
        margin: 6px 0;
        border: 1px solid rgba(255, 255, 255, 0.05);
    }
    .progress-bar-fill {
        height: 100%;
        border-radius: 20px;
        transition: width 1s cubic-bezier(0.16, 1, 0.3, 1);
        position: relative;
        overflow: hidden;
        box-shadow: 0 0 10px rgba(0, 242, 254, 0.5);
    }
    .progress-bar-fill::after {
        content: '';
        position: absolute;
        inset: 0;
        background: linear-gradient(90deg, transparent 0%, rgba(255, 255, 255, 0.4) 50%, transparent 100%);
        background-size: 200% 100%;
        animation: shimmerSweep 1.5s infinite;
    }

    /* ==================== HUD BADGES ==================== */
    .badge {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 4px 12px;
        border-radius: 20px;
        font-family: var(--font-mono);
        font-size: 0.74rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.06em;
        margin-right: 6px;
        margin-bottom: 4px;
    }
    .badge-primary, .badge-info {
        background: rgba(0, 242, 254, 0.12);
        color: var(--cyber-cyan);
        border: 1px solid rgba(0, 242, 254, 0.3);
        box-shadow: 0 0 12px rgba(0, 242, 254, 0.15);
    }
    .badge-secondary, .badge-accent {
        background: rgba(79, 172, 254, 0.12);
        color: var(--electric-indigo);
        border: 1px solid rgba(79, 172, 254, 0.3);
    }
    .badge-success {
        background: rgba(16, 185, 129, 0.12);
        color: #10B981;
        border: 1px solid rgba(16, 185, 129, 0.3);
    }
    .badge-warning {
        background: rgba(245, 158, 11, 0.12);
        color: #F59E0B;
        border: 1px solid rgba(245, 158, 11, 0.3);
    }
    .badge-error {
        background: rgba(239, 68, 68, 0.12);
        color: #EF4444;
        border: 1px solid rgba(239, 68, 68, 0.3);
    }

    /* ==================== CALLOUT BOXES ==================== */
    .info-box, .warning-box, .success-box {
        border-radius: var(--radius-md);
        padding: 16px 20px;
        margin: 14px 0;
        animation: fadeInLeft 0.4s ease-out both;
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
    }
    .info-box {
        background: rgba(0, 242, 254, 0.06);
        border-left: 3px solid var(--cyber-cyan);
        border-top: 1px solid rgba(0, 242, 254, 0.12);
        border-right: 1px solid rgba(0, 242, 254, 0.12);
        border-bottom: 1px solid rgba(0, 242, 254, 0.12);
    }
    .warning-box {
        background: rgba(245, 158, 11, 0.06);
        border-left: 3px solid var(--amber-warning);
        border-top: 1px solid rgba(245, 158, 11, 0.12);
        border-right: 1px solid rgba(245, 158, 11, 0.12);
        border-bottom: 1px solid rgba(245, 158, 11, 0.12);
    }
    .success-box {
        background: rgba(16, 185, 129, 0.06);
        border-left: 3px solid var(--emerald-success);
        border-top: 1px solid rgba(16, 185, 129, 0.12);
        border-right: 1px solid rgba(16, 185, 129, 0.12);
        border-bottom: 1px solid rgba(16, 185, 129, 0.12);
    }
    .info-box p, .warning-box p, .success-box p {
        margin: 0;
        font-size: 0.92rem;
        line-height: 1.55;
    }

    /* ==================== SIDEBAR ==================== */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #07090E 0%, #0B0F19 50%, #07090E 100%) !important;
        border-right: 1px solid var(--border-glass) !important;
        box-shadow: 10px 0 30px rgba(0, 0, 0, 0.6);
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
        font-size: 2.4rem;
        margin-bottom: 6px;
        display: inline-block;
        filter: drop-shadow(0 0 15px rgba(0, 242, 254, 0.5));
        animation: float 4s ease-in-out infinite;
    }
    .sidebar-title {
        font-size: 1.35rem;
        font-weight: 900;
        background: var(--gradient-cyber);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        letter-spacing: -0.02em;
    }
    .sidebar-subtitle {
        font-family: var(--font-mono);
        font-size: 0.7rem;
        color: var(--cyber-cyan);
        letter-spacing: 0.15em;
        text-transform: uppercase;
        margin-top: 2px;
        opacity: 0.85;
    }
    .sidebar-hud-status {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        font-family: var(--font-mono);
        font-size: 0.68rem;
        background: rgba(0, 242, 254, 0.08);
        border: 1px solid rgba(0, 242, 254, 0.2);
        color: var(--cyber-cyan);
        padding: 3px 10px;
        border-radius: 12px;
        margin-top: 8px;
    }

    /* ==================== DIVIDERS ==================== */
    .gradient-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent 0%, rgba(0, 242, 254, 0.5) 50%, transparent 100%);
        border: none;
        margin: 24px 0;
        box-shadow: 0 0 8px rgba(0, 242, 254, 0.3);
    }
    .gradient-divider-sm {
        height: 1px;
        background: linear-gradient(90deg, transparent 0%, rgba(0, 242, 254, 0.3) 50%, transparent 100%);
        border: none;
        margin: 12px 0;
    }

    /* ==================== SCROLLBARS ==================== */
    ::-webkit-scrollbar { width: 6px; height: 6px; }
    ::-webkit-scrollbar-track { background: #07090E; }
    ::-webkit-scrollbar-thumb {
        background: rgba(0, 242, 254, 0.25);
        border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
        background: rgba(0, 242, 254, 0.6);
        box-shadow: 0 0 10px #00F2FE;
    }

    /* ==================== EXPANDER ==================== */
    .streamlit-expanderHeader {
        background: var(--bg-surface-card) !important;
        border: 1px solid var(--border-glass) !important;
        border-radius: var(--radius-md) !important;
        font-weight: 600 !important;
        font-size: 0.95rem !important;
        transition: all 0.25s ease !important;
    }
    details[open] .streamlit-expanderHeader {
        border-color: rgba(0, 242, 254, 0.5) !important;
        color: var(--cyber-cyan) !important;
    }

    /* ==================== HIDE STREAMLIT BRANDING ==================== */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }

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
