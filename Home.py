import streamlit as st
import base64

# --- Set background image from local PNG file ---
def set_png_as_page_bg(png_file):
    with open(png_file, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

set_png_as_page_bg("images/background.png")  # <-- change this to your PNG filename

# --- Hide sidebar, hamburger, and set background ---
st.markdown("""
<style>
[data-testid="stSidebar"] {display: none !important;}
[data-testid="collapsedControl"] {display: none !important;}
header {visibility: hidden;}
.block-container {
    padding-top: 0rem !important;
    padding-bottom: 0rem !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
}
.custom-topbar {
    position: fixed;
    top: 0; left: 0; right: 0;
    height: 110px;
    background: #8a206f;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 10000;
    box-shadow: 0 2px 18px rgba(0,0,0,0.10);
}
.custom-topbar-title {
    color: #fff;
    font-size: 38px;
    font-weight: 800;
    letter-spacing: 2px;
    text-align: center;
    width: 100%;
    line-height: 110px;
    margin: 0;
    padding: 0;
    user-select: none;
}
.main-content-canvas {
    margin-top: 110px;
    min-height: calc(100vh - 110px);
    width: 100vw;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
}
.welcome-box {
    background: #13294b;
    color: #fff;
    font-size: 2.1rem;
    font-weight: 700;
    border-radius: 16px;
    padding: 18px 44px;
    margin-top: 32px;
    margin-bottom: 20px;
    box-shadow: 0 3px 12px rgba(19,41,75,0.10);
    text-align: center;
    display: inline-block;
    letter-spacing: 1px;
}
.choose-box {
    background: #13294b;
    color: #fff;
    font-size: 22px;
    font-weight: 600;
    border-radius: 16px;
    padding: 18px 44px;
    margin-top: 0px;
    margin-bottom: 38px;
    box-shadow: 0 3px 12px rgba(19,41,75,0.10);
    text-align: center;
    display: inline-block;
    letter-spacing: 1px;
}
/* Style all Streamlit buttons */
div.stButton > button {
    background: #8a206f !important;
    color: #fff !important;
    border: none !important;
    border-radius: 14px !important;
    font-size: 1.3rem !important;
    padding: 32px 60px !important;
    font-weight: 600 !important;
    box-shadow: 0 2px 8px rgba(138,32,111,0.08);
    transition: background 0.2s;
    min-width: 260px;
    min-height: 80px !important;
    text-align: center;
    cursor: pointer;
}
div.stButton > button:hover {
    background: #a63ba7 !important;
    color: #fff !important;
}
/* Chatbot styles */
.chatbot-float {
    position: fixed;
    bottom: 32px;
    left: 0;
    width: 100vw;
    display: flex;
    justify-content: center;
    z-index: 9999;
    pointer-events: none;
}
.chatbot-btn-wrap {
    pointer-events: all;
}
.chatbot-btn {
    background: #8a206f;
    color: #fff;
    border: none;
    border-radius: 50%;
    width: 120px;
    height: 120px;
    font-size: 60px;
    box-shadow: 0 2px 8px rgba(138,32,111,0.18);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: background 0.2s;
    margin-bottom: 10px;
}
.chatbot-btn:hover {
    background: #a63ba7;
    color: #fff;
}
.chatbot-window {
    width: 370px;
    background: #fff;
    border-radius: 16px;
    box-shadow: 0 4px 24px rgba(138,32,111,0.15);
    padding: 22px 18px 16px 18px;
    margin-bottom: 12px;
    color: #333;
    font-family: 'Segoe UI', 'Arial', sans-serif;
    pointer-events: all;
}
/* Dark blue background for chatbot heading */
.chatbot-title {
    background: #13294b;
    color: #fff;
    font-weight: 700;
    font-size: 18px;
    letter-spacing: 0.5px;
    margin-bottom: 8px;
    margin-top: 2px;
    padding: 10px 16px;
    border-radius: 12px;
    text-align: center;
}
.close-btn {
    background: #8a206f;
    color: #fff;
    border: none;
    border-radius: 50%;
    width: 32px;
    height: 32px;
    font-size: 18px;
    float: right;
    margin-top: -10px;
    margin-right: -10px;
    cursor: pointer;
    transition: background 0.2s;
}
.close-btn:hover {
    background: #a63ba7;
}
.chat-history {
    max-height: 180px;
    overflow-y: auto;
    margin-bottom: 10px;
    padding-right: 2px;
}
.chat-user {
    color: #fff;
    background: #8a206f;
    border-radius: 12px;
    padding: 6px 10px;
    margin-bottom: 3px;
    font-weight: 500;
    font-size: 15px;
}
.chat-bot {
    color: #fff;
    background: #a63ba7;
    border-radius: 12px;
    padding: 6px 10px;
    margin-bottom: 8px;
    font-size: 15px;
}
</style>
""", unsafe_allow_html=True)

# --- TOPBAR HTML ---
st.markdown("""
<div class="custom-topbar">
    <span class="custom-topbar-title">Regent Middle East</span>
</div>
""", unsafe_allow_html=True)

# --- MAIN CONTENT ---
st.markdown('<div class="main-content-canvas">', unsafe_allow_html=True)
st.markdown("""
<div style="display: flex; flex-direction: column; align-items: center;">
    <div class="welcome-box">Welcome!</div>
    <div class="choose-box">Choose your calculator:</div>
</div>
""", unsafe_allow_html=True)

row1_col1, row1_col2 = st.columns(2, gap="large")
row2_col1, row2_col2 = st.columns(2, gap="large")

with row1_col1:
    if st.button("💻 Level 2 Computing", key="lvl2comp"):
        st.switch_page("pages/1_Level_2_Computing.py")
with row1_col2:
    if st.button("💾 Level 3 Computing", key="lvl3comp"):
        st.switch_page("pages/2_Level_3_Computing.py")
with row2_col1:
    if st.button("📊 Level 2 Business", key="lvl2bus"):
        st.switch_page("pages/3_Level_2_Business.py")
with row2_col2:
    if st.button("📈 Level 3 Business", key="lvl3bus"):
        st.switch_page("pages/4_Level_3_Business.py")

st.markdown('</div>', unsafe_allow_html=True)

# --- Chatbot Logic ---
def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    if "hello" in user_input or "hi" in user_input:
        return "Hello! I can help you with questions about diploma grades, points, and grade thresholds."
    if "thanks" in user_input or "thank you" in user_input:
        return "You're welcome! Ask me anything about grades or points."
    if "p" in user_input:
        return "P means 'Pass' — minimum passing grade."
    if "m" in user_input:
        return "M means 'Merit' — above Pass, below Distinction."
    if "d*" in user_input or "d star" in user_input:
        return "D* means 'Distinction Star' — for exceptional performance."
    if "d" in user_input:
        return "D means 'Distinction' — highest standard grade."
    if "u" in user_input:
        return "U means 'Unclassified' — not enough points to pass."
    return "Sorry, I can help with grade thresholds, point calculations, and diploma questions. Try asking about Level 3 points or minimum for MM."

# Chatbot state
if "chatbot_open" not in st.session_state:
    st.session_state.chatbot_open = False
if "chatbot_history" not in st.session_state:
    st.session_state.chatbot_history = []
if "chatbot_input" not in st.session_state:
    st.session_state.chatbot_input = ""

def handle_chatbot_input():
    user_input = st.session_state.chatbot_input
    if user_input:
        response = chatbot_response(user_input)
        st.session_state.chatbot_history.append((user_input, response))
        st.session_state.chatbot_input = ""

st.markdown('<div class="chatbot-float">', unsafe_allow_html=True)
if not st.session_state.chatbot_open:
    if st.button("💬", key="open_chatbot", help="Open chatbot"):
        st.session_state.chatbot_open = True
else:
    st.markdown('<div class="chatbot-window">', unsafe_allow_html=True)
    close_col, title_col = st.columns([0.15, 0.85])
    with close_col:
        if st.button("✕", key="close_chatbot", help="Close chatbot"):
            st.session_state.chatbot_open = False
            st.rerun()
    with title_col:
        st.markdown('<div class="chatbot-title">🤖 Academic Chatbot</div>', unsafe_allow_html=True)
    st.markdown('<div class="chat-history">', unsafe_allow_html=True)
    for q, a in st.session_state.chatbot_history:
        st.markdown(f"<div class='chat-user'>You: {q}</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='chat-bot'>Bot: {a}</div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    st.text_input(
        "Ask me something:",
        key="chatbot_input",
        on_change=handle_chatbot_input,
        label_visibility="collapsed"
    )
    st.markdown('</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
