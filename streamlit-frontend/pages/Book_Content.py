import streamlit as st
import os

# ----------------------------
# Page Setup
# ----------------------------
st.set_page_config(page_title="Read Book", layout="wide")
if "font_size" not in st.session_state:
    st.session_state.font_size = 16
if "current_book" not in st.session_state:
    st.session_state.current_book = "Ramayana"

# ----------------------------
# Sidebar
# ----------------------------
with st.sidebar:
    if os.path.exists("images/logo.png"):
        st.image("images/logo.png", width=100)

    st.markdown("""
        <h2 style="text-align: center; color: #1e3a8a; font-family: 'Brush Script MT', 'Pacifico', cursive; font-size: 36px; margin-bottom: 0;">
            Saathi
        </h2>
        <p style="text-align: center; color: #2563eb; font-size: 14px; margin-top: 2px;">
            A companion app for senior citizens
        </p>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Styled menu buttons
    if st.button("💬 AI Chat", use_container_width=True):
        st.info("AI Chat is not implemented yet.") #repace this with st.swtichpage("page path")
    if st.button("📨 Messages", use_container_width=True):
        st.switch_page("pages/Messages_app.py")
    if st.button("🎬 Entertainment", use_container_width=True):
        st.warning("Entertainment is coming soon!") #repace this with st.swtichpage("page path")
    if st.button("📖 Mythology", use_container_width=True):
        st.switch_page("pages/Mythology_Homepage.py")
    if st.button("⏰ Reminders", use_container_width=True):
        st.warning("Reminder system in development.") #repace this with st.swtichpage("page path")

    st.markdown("---")
    st.markdown("**🆘 Help**")
    st.slider("Font size", min_value=12, max_value=32, value=st.session_state.font_size, key="font_size")
# ----------------------------
# Header
# ----------------------------
col1, col2 = st.columns([6, 1])
with col1:
    back_clicked = st.button("← Back", key="back_button", help="Return to Mythology page")
    if back_clicked:
        st.switch_page("pages/Mythology_Homepage.py")

with col2:
    st.button("🔊 Read aloud")

st.markdown(f"""
    <h1 style="color: #1e3a8a; font-size: {st.session_state.font_size + 6}px;">
        {st.session_state.current_book}
    </h1>
    <hr>
""", unsafe_allow_html=True)

# ----------------------------
# Book Text Content
# ----------------------------
st.markdown(f"""
    <div style="height: 500px; overflow-y: scroll; padding: 20px; background-color: #f8fafc; border-radius: 12px; font-size: {st.session_state.font_size}px; line-height: 1.6;">
        <p><strong>Chapter 1:</strong> Long ago in the kingdom of Ayodhya, there lived a wise and noble king named Dasharatha...</p>
        <p>He had three wives and four sons. The eldest, Rama, was the most virtuous and beloved by all.</p>
        <p>As time passed, plans were made for Rama to ascend the throne. However, fate had different plans...</p>
        <p>Kaikeyi, one of the queens, asked for Rama's exile and her son Bharata to be crowned instead.</p>
        <p>And so began the epic journey of Rama through forests, meeting sages, demons, and forming lasting bonds...</p>
        <p>[...continued...]</p>
    </div>
""", unsafe_allow_html=True)

# ----------------------------
# Footer
# ----------------------------
st.markdown("""
    <div style="margin-top: 30px; text-align: center; font-size: 14px; color: gray;">
        © 2025 Saathi App - Mythological Reading Experience
    </div>
""", unsafe_allow_html=True)
