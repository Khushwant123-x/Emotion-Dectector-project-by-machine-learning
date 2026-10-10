import streamlit as st
import pickle
import os
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Sentify AI • Emotion Intelligence",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom High-End Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@400;500;600;700;800;900&display=swap');

html, body, [class*="css"] {
    font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background: radial-gradient(circle at 10% 10%, rgba(99, 102, 241, 0.12) 0%, transparent 45%),
                radial-gradient(circle at 85% 25%, rgba(236, 72, 153, 0.08) 0%, transparent 40%),
                radial-gradient(circle at 50% 90%, rgba(16, 185, 129, 0.06) 0%, transparent 50%),
                #090d16 !important;
    color: #f1f5f9;
}

.block-container {
    padding-top: 1.8rem !important;
    padding-bottom: 2.5rem !important;
    max-width: 1200px !important;
}

.brand-banner {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 1.1rem 1.8rem;
    background: rgba(17, 24, 39, 0.65);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 18px;
    backdrop-filter: blur(16px);
    margin-bottom: 2rem;
    box-shadow: 0 4px 20px -2px rgba(0, 0, 0, 0.4);
}

.brand-logo {
    display: flex;
    align-items: center;
    gap: 12px;
}

.brand-logo-icon {
    width: 44px;
    height: 44px;
    background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    box-shadow: 0 0 16px rgba(168, 85, 247, 0.45);
}

.brand-logo-text {
    font-family: 'Outfit', sans-serif;
    font-weight: 800;
    font-size: 1.45rem;
    letter-spacing: -0.02em;
    background: linear-gradient(120deg, #ffffff 0%, #cbd5e1 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0;
    line-height: 1.1;
}

.brand-tagline {
    font-size: 0.78rem;
    color: #94a3b8;
    font-weight: 500;
    margin-top: 2px;
}

.live-status {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 14px;
    background: rgba(16, 185, 129, 0.12);
    border: 1px solid rgba(16, 185, 129, 0.3);
    border-radius: 9999px;
    font-size: 0.8rem;
    font-weight: 600;
    color: #34d399;
}

.status-dot {
    width: 8px;
    height: 8px;
    background: #10b981;
    border-radius: 50%;
    box-shadow: 0 0 8px #10b981;
}

.card-title {
    font-family: 'Outfit', sans-serif;
    font-weight: 700;
    font-size: 1.25rem;
    color: #f8fafc;
    margin-bottom: 0.3rem;
}

.card-subtitle {
    color: #94a3b8;
    font-size: 0.88rem;
    margin-bottom: 1.1rem;
}

.stTextArea textarea {
    background: rgba(11, 15, 25, 0.85) !important;
    color: #f8fafc !important;
    border: 1.5px solid rgba(99, 102, 241, 0.25) !important;
    border-radius: 16px !important;
    padding: 16px !important;
    font-size: 1.05rem !important;
    backdrop-filter: blur(12px) !important;
    transition: all 0.25s ease !important;
    box-shadow: inset 0 2px 4px rgba(0, 0, 0, 0.4) !important;
}

.stTextArea textarea:focus {
    border-color: #8b5cf6 !important;
    box-shadow: 0 0 0 3px rgba(139, 92, 246, 0.25), inset 0 2px 4px rgba(0, 0, 0, 0.4) !important;
}

.metrics-bar {
    display: flex;
    gap: 10px;
    margin: 8px 0 16px 0;
    flex-wrap: wrap;
}

.metric-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 5px 12px;
    background: rgba(255, 255, 255, 0.04);
    border: 1px solid rgba(255, 255, 255, 0.08);
    border-radius: 8px;
    font-size: 0.8rem;
    font-weight: 500;
    color: #94a3b8;
}

button[kind="primary"] {
    background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 50%, #ec4899 100%) !important;
    border: none !important;
    color: white !important;
    font-weight: 700 !important;
    padding: 0.75rem 1.8rem !important;
    border-radius: 14px !important;
    font-size: 1rem !important;
    letter-spacing: 0.02em !important;
    box-shadow: 0 4px 18px rgba(139, 92, 246, 0.4) !important;
    transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1) !important;
}

button[kind="primary"]:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 25px rgba(139, 92, 246, 0.6) !important;
}

button[kind="secondary"] {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255, 255, 255, 0.12) !important;
    color: #cbd5e1 !important;
    border-radius: 12px !important;
    font-weight: 600 !important;
    transition: all 0.2s ease !important;
}

button[kind="secondary"]:hover {
    background: rgba(255, 255, 255, 0.1) !important;
    color: #ffffff !important;
    border-color: rgba(255, 255, 255, 0.25) !important;
}

.hero-emotion-box {
    text-align: center;
    padding: 2.4rem 2rem;
    background: radial-gradient(circle at 50% 30%, var(--glow-bg, rgba(99, 102, 241, 0.25)) 0%, rgba(15, 23, 42, 0.85) 85%);
    border: 1.5px solid var(--border-glow, rgba(99, 102, 241, 0.4));
    border-radius: 24px;
    box-shadow: 0 20px 45px -10px var(--shadow-glow, rgba(0, 0, 0, 0.5));
    margin-bottom: 1rem;
}

.emotion-badge-avatar {
    width: 110px;
    height: 110px;
    margin: 0 auto 1.2rem auto;
    border-radius: 50%;
    background: rgba(15, 23, 42, 0.7);
    border: 3px solid var(--accent-color, #6366f1);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 4rem;
    box-shadow: 0 0 35px var(--accent-color, #6366f1);
}

.emotion-hero-title {
    font-family: 'Outfit', sans-serif;
    font-size: 2.6rem;
    font-weight: 900;
    letter-spacing: -0.02em;
    text-transform: capitalize;
    margin: 0;
    line-height: 1.1;
    color: var(--accent-color, #ffffff);
}

.hero-confidence-pill {
    display: inline-block;
    margin-top: 10px;
    padding: 6px 18px;
    border-radius: 9999px;
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);
    font-size: 0.95rem;
    font-weight: 700;
    color: #ffffff;
}

.emotion-quote-box {
    margin-top: 1.2rem;
    font-style: italic;
    color: #cbd5e1;
    font-size: 0.95rem;
    line-height: 1.5;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    padding-top: 1rem;
}

.empty-state-box {
    text-align: center;
    padding: 4.5rem 2rem;
    background: rgba(15, 23, 42, 0.4);
    border: 2px dashed rgba(255, 255, 255, 0.08);
    border-radius: 20px;
}

.empty-icon {
    font-size: 3.5rem;
    margin-bottom: 0.8rem;
}
</style>
""", unsafe_allow_html=True)

# Path and Resource Cache
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@st.cache_resource
def load_ml_assets():
    model_path = os.path.join(BASE_DIR, "emotion_model.pkl")
    vec_path = os.path.join(BASE_DIR, "tfidf_vectorizer.pkl")
    map_path = os.path.join(BASE_DIR, "emotion_mapping.pkl")

    with open(model_path, "rb") as f:
        model = pickle.load(f)
    with open(vec_path, "rb") as f:
        vectorizer = pickle.load(f)
    with open(map_path, "rb") as f:
        emotion_map = pickle.load(f)

    return model, vectorizer, emotion_map

try:
    model, vectorizer, emotion_map = load_ml_assets()
except Exception as e:
    st.error(f"Error loading models: {e}")
    st.stop()

# Visual configuration per emotion
CONFIG_EMOTIONS = {
    "joy": {
        "emoji": "😄",
        "title": "Joy & Happiness",
        "color": "#10B981",
        "glow_bg": "rgba(16, 185, 129, 0.25)",
        "border_glow": "rgba(16, 185, 129, 0.5)",
        "shadow_glow": "rgba(16, 185, 129, 0.35)",
        "tone": "Vibrantly Positive",
        "quote": "“Joy is not in things; it is in us. Smiles radiate and create light for everyone.”"
    },
    "love": {
        "emoji": "💖",
        "title": "Love & Affection",
        "color": "#EC4899",
        "glow_bg": "rgba(236, 72, 153, 0.25)",
        "border_glow": "rgba(236, 72, 153, 0.5)",
        "shadow_glow": "rgba(236, 72, 153, 0.35)",
        "tone": "Warm & Loving",
        "quote": "“To love and be loved is to feel the sun from both sides.”"
    },
    "surprise": {
        "emoji": "😲",
        "title": "Surprise & Wonder",
        "color": "#8B5CF6",
        "glow_bg": "rgba(139, 92, 246, 0.25)",
        "border_glow": "rgba(139, 92, 246, 0.5)",
        "shadow_glow": "rgba(139, 92, 246, 0.35)",
        "tone": "Intrigue & Wonder",
        "quote": "“Life is full of wonderful surprises waiting around every corner.”"
    },
    "fear": {
        "emoji": "😨",
        "title": "Fear & Anxiety",
        "color": "#F59E0B",
        "glow_bg": "rgba(245, 158, 11, 0.25)",
        "border_glow": "rgba(245, 158, 11, 0.5)",
        "shadow_glow": "rgba(245, 158, 11, 0.35)",
        "tone": "Caution & Tension",
        "quote": "“Fear does not stop death; it stops life. Take courage and step forward.”"
    },
    "anger": {
        "emoji": "😡",
        "title": "Anger & Frustration",
        "color": "#EF4444",
        "glow_bg": "rgba(239, 68, 68, 0.25)",
        "border_glow": "rgba(239, 68, 68, 0.5)",
        "shadow_glow": "rgba(239, 68, 68, 0.35)",
        "tone": "High Agitation",
        "quote": "“Holding onto anger is like drinking poison and expecting the other person to die.”"
    },
    "sadness": {
        "emoji": "😢",
        "title": "Sadness & Grief",
        "color": "#06B6D4",
        "glow_bg": "rgba(6, 182, 212, 0.25)",
        "border_glow": "rgba(6, 182, 212, 0.5)",
        "shadow_glow": "rgba(6, 182, 212, 0.35)",
        "tone": "Melancholy & Sorrow",
        "quote": "“Heavy hearts, like heavy clouds in the sky, are best relieved by letting a little water.”"
    }
}

# State initialization
if "user_query" not in st.session_state:
    st.session_state.user_query = ""
if "trigger_analysis" not in st.session_state:
    st.session_state.trigger_analysis = False
if "history" not in st.session_state:
    st.session_state.history = []

def select_preset(text_value):
    st.session_state.user_query = text_value
    st.session_state.trigger_analysis = True

# Brand Header Banner (No leading whitespace)
brand_html = (
'<div class="brand-banner">'
'<div class="brand-logo">'
'<div class="brand-logo-icon">🎭</div>'
'<div>'
'<h1 class="brand-logo-text">SENTIFY AI</h1>'
'<div class="brand-tagline">Natural Language Emotion Detection Engine</div>'
'</div>'
'</div>'
'<div class="live-status">'
'<div class="status-dot"></div>'
'<span>Model Ready (v2.4)</span>'
'</div>'
'</div>'
)
st.markdown(brand_html, unsafe_allow_html=True)

# Sidebar (Optional History)
if st.session_state.history:
    with st.sidebar:
        st.markdown("### 🕒 Session History")
        for idx, item in enumerate(reversed(st.session_state.history[-5:])):
            st.markdown(
                f"**{item['emoji']} {item['emotion'].capitalize()}** ({item['conf']:.1f}%)\n\n"
                f"> *\"{item['text'][:40]}...\"*"
            )
        if st.button("🗑️ Clear History", use_container_width=True):
            st.session_state.history = []
            st.rerun()

# 2-Column Responsive Layout
col_left, col_right = st.columns([1.1, 1], gap="large")

with col_left:
    st.markdown('<div class="card-title">✍️ Enter Statement or Phrase</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-subtitle">Type your text below or click any sample prompt to run instant semantic analysis.</div>', unsafe_allow_html=True)

    # Preset Quick Samples
    st.markdown("<div style='font-size:0.78rem; font-weight:700; color:#818cf8; letter-spacing:0.05em; text-transform:uppercase; margin-bottom:8px;'>⚡ 1-Click Instant Samples:</div>", unsafe_allow_html=True)
    p_col1, p_col2 = st.columns(2)
    with p_col1:
        st.button(
            "🎉 Dream job offer!",
            use_container_width=True,
            on_click=select_preset,
            args=("I just got my dream job offer today and I can't stop celebrating!",)
        )
        st.button(
            "💔 Feeling so lonely",
            use_container_width=True,
            on_click=select_preset,
            args=("I feel so lonely sitting alone in this empty room missing everything we had.",)
        )
        st.button(
            "😡 Terrible rude service",
            use_container_width=True,
            on_click=select_preset,
            args=("This is the worst customer service ever, completely incompetent and rude!",)
        )
    with p_col2:
        st.button(
            "❤️ You mean everything to me",
            use_container_width=True,
            on_click=select_preset,
            args=("You are the sweetest, kindest human being and I cherish every second with you.",)
        )
        st.button(
            "😲 Totally unexpected surprise",
            use_container_width=True,
            on_click=select_preset,
            args=("I was completely stunned when I walked into the dark room and everyone shouted surprise!",)
        )
        st.button(
            "😨 Terrified about the exam",
            use_container_width=True,
            on_click=select_preset,
            args=("My heart is pounding and I'm terrified that I might fail this critical test tomorrow.",)
        )

    # Main Text Area
    user_input = st.text_area(
        label="Input Content",
        value=st.session_state.user_query,
        placeholder="Type or paste any text here (e.g. 'I am so excited about this weekend trip with my best friends!')...",
        height=150,
        label_visibility="collapsed"
    )
    st.session_state.user_query = user_input

    # Real-Time Statistics
    words_list = user_input.strip().split() if user_input.strip() else []
    w_count = len(words_list)
    c_count = len(user_input)
    r_time = max(1, round(w_count / 200 * 60)) if w_count > 0 else 0

    metric_html = (
        '<div class="metrics-bar">'
        f'<span class="metric-badge">📝 {w_count} Words</span>'
        f'<span class="metric-badge">🔤 {c_count} Characters</span>'
        f'<span class="metric-badge">⚡ ~{r_time}s Read Time</span>'
        '</div>'
    )
    st.markdown(metric_html, unsafe_allow_html=True)

    # Action Buttons
    b_col1, b_col2 = st.columns([2.5, 1])
    with b_col1:
        submit_btn = st.button("🚀 Analyze Emotion", type="primary", use_container_width=True)
    with b_col2:
        clear_btn = st.button("↺ Clear", use_container_width=True)
        if clear_btn:
            st.session_state.user_query = ""
            st.session_state.trigger_analysis = False
            st.rerun()

with col_right:
    st.markdown('<div class="card-title">🎯 AI Emotion Classification</div>', unsafe_allow_html=True)
    st.markdown('<div class="card-subtitle">Real-time model inferences and predicted emotional state.</div>', unsafe_allow_html=True)

    should_run = submit_btn or st.session_state.trigger_analysis
    
    if should_run and user_input.strip():
        st.session_state.trigger_analysis = False

        with st.spinner("Analyzing semantics & sentiment vectors..."):
            vec = vectorizer.transform([user_input])
            probabilities = model.predict_proba(vec)[0]
            pred_idx = np.argmax(probabilities)
            pred_label = emotion_map[pred_idx]
            conf = probabilities[pred_idx] * 100
            
            emotion_info = CONFIG_EMOTIONS.get(pred_label, {
                "emoji": "✨",
                "title": pred_label.capitalize(),
                "color": "#8b5cf6",
                "glow_bg": "rgba(139, 92, 246, 0.2)",
                "border_glow": "rgba(139, 92, 246, 0.4)",
                "shadow_glow": "rgba(0,0,0,0.5)",
                "tone": "Neutral",
                "quote": ""
            })

            # Append to session history (avoid duplicates)
            if not st.session_state.history or st.session_state.history[-1]['text'] != user_input:
                st.session_state.history.append({
                    "text": user_input,
                    "emotion": pred_label,
                    "emoji": emotion_info["emoji"],
                    "conf": conf,
                    "color": emotion_info["color"]
                })

        # Hero Emotion Result Banner (Constructed cleanly without leading indentation)
        result_card_html = (
            f'<div class="hero-emotion-box" style="'
            f'--glow-bg: {emotion_info["glow_bg"]}; '
            f'--border-glow: {emotion_info["border_glow"]}; '
            f'--shadow-glow: {emotion_info["shadow_glow"]}; '
            f'--accent-color: {emotion_info["color"]};">'
            f'<div class="emotion-badge-avatar">{emotion_info["emoji"]}</div>'
            f'<h2 class="emotion-hero-title">{pred_label}</h2>'
            f'<div style="color: #94a3b8; font-weight: 600; font-size: 0.95rem; margin-top: 4px;">{emotion_info["tone"]}</div>'
            f'<div class="hero-confidence-pill">Confidence: <strong>{conf:.1f}%</strong></div>'
            f'<div class="emotion-quote-box">{emotion_info["quote"]}</div>'
            f'</div>'
        )
        st.markdown(result_card_html, unsafe_allow_html=True)

    elif should_run and not user_input.strip():
        st.warning("⚠️ Please provide text input before analyzing.")
    else:
        empty_html = (
            '<div class="empty-state-box">'
            '<div class="empty-icon">🔮</div>'
            '<h3 style="color:#e2e8f0; font-weight:800; margin-bottom:6px; font-family:\'Outfit\';">Ready for Analysis</h3>'
            '<p style="color:#64748b; font-size:0.92rem; max-width:80%; margin:0 auto;">'
            'Select any of the <b>1-Click Instant Samples</b> on the left or type your own phrase to observe neural classification in real-time.'
            '</p>'
            '</div>'
        )
        st.markdown(empty_html, unsafe_allow_html=True)