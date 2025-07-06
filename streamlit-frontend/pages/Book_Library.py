import streamlit as st
import os

# ----------------------------
# Page Setup
# ----------------------------
st.set_page_config(page_title="Mythology Library", layout="wide")
if "font_size" not in st.session_state:
    st.session_state.font_size = 16
if "selected_category" not in st.session_state:
    st.session_state.selected_category = "Ramayana"
if "current_book" not in st.session_state:
    st.session_state.current_book = ""

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
    if st.button("← Back", key="back"):
        st.switch_page("pages/Mythology_Homepage.py")

with col2:
    pass  # You can add a "Refresh" or "Sort" button here later

st.markdown(f"""
    <h1 style="color: #1e3a8a; font-size: {st.session_state.font_size + 6}px;">
        {st.session_state.selected_category}
    </h1>
    <hr>
""", unsafe_allow_html=True)

# ----------------------------
# Search Bar
# ----------------------------
search_query = st.text_input("Search for books...", "").lower()

# ----------------------------
# Book List
# ----------------------------
books = [f"{st.session_state.selected_category} Book {i+1}" for i in range(8)]
filtered_books = [book for book in books if search_query in book.lower()]

st.markdown(f"<h3 style='font-size: {st.session_state.font_size}px;'>Available Books</h3>", unsafe_allow_html=True)
cols = st.columns(4)

for i, book in enumerate(filtered_books):
    with cols[i % 4]:
        st.image("https://via.placeholder.com/100", caption=book)
        if st.button(f"Read: {book}", key=f"book_btn_{i}"):
            st.session_state.current_book = book
            st.switch_page("pages/Book_Content.py")

# ----------------------------
# Footer
# ----------------------------
st.markdown("""
    <div style="margin-top: 30px; text-align: center; font-size: 14px; color: gray;">
        © 2025 Saathi App - Mythology Library
    </div>
""", unsafe_allow_html=True)
