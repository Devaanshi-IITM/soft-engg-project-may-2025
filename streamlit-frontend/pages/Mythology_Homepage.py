import streamlit as st
import os

# ----------------------------
# Page Settings & State Init
# ----------------------------
st.set_page_config(page_title="Mythology", layout="wide")

# Initialize session state
if "selected_category" not in st.session_state:
    st.session_state.selected_category = None
if "selected_book" not in st.session_state:
    st.session_state.selected_book = None
if "font_size" not in st.session_state:
    st.session_state.font_size = 16

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
# Page Heading
# ----------------------------
st.markdown(f"""<h1 style='color: #1e3a8a; font-size: {st.session_state.font_size + 8}px;'>📖 Mythology</h1>""", unsafe_allow_html=True)

col1, col2 = st.columns([3, 2])

# ----------------------------
# Left Panel: Featured & Bookmarked
# ----------------------------
with col1:
    st.markdown(f"""<h3 style='font-size: {st.session_state.font_size + 2}px;'>Featured Books and Stories</h3>""", unsafe_allow_html=True)
    cols = st.columns(4)
    for i in range(4):
        with cols[i]:
            st.image("https://via.placeholder.com/80")
            if st.button(f"📘 Book {i+1}", key=f"book_{i+1}"):
                st.session_state.selected_book = f"Book {i+1}"
                st.switch_page("pages/Book_Content.py")

    st.markdown(f"""<h3 style='font-size: {st.session_state.font_size + 2}px;'>Bookmarked</h3>""", unsafe_allow_html=True)
    cols = st.columns(4)
    for i in range(4):
        with cols[i]:
            st.image("https://via.placeholder.com/80")
            if st.button(f"🔖 Bookmark {i+1}", key=f"bookmark_{i+1}"):
                st.session_state.selected_book = f"Bookmark {i+1}"
                st.switch_page("pages/Book_Content.py")

# ----------------------------
# Right Panel: Categories
# ----------------------------
with col2:
    st.markdown(f"""<h3 style='font-size: {st.session_state.font_size + 2}px;'>All categories</h3>""", unsafe_allow_html=True)
    categories = ["Ramayana", "Mahabharata", "Bhagwad Gita", "Other texts"]
    for cat in categories:
        if st.button(cat, use_container_width=True, key=f"cat_{cat}"):
            st.session_state.selected_category = cat
            st.switch_page("pages/Book_Libarary.py")
