from utils.style import apply_base_style, show_header
import streamlit as st

# Apply shared styling
apply_base_style()

# Welcome header
col1, col2 = st.columns([5, 1])
with col1:
    show_header("Welcome!")
with col2:
    st.image("https://img.icons8.com/ios-filled/50/user.png", width=40)

st.divider()

# Search bar
st.text_input("Search", placeholder="Search", label_visibility="collapsed")

# Font size slider
font_size = st.slider("Font size", 12, 28, 18)

# Cards — Clickable
cards = [
    ("Health & Reminders", "pages/health.py"),
    ("Mythology", "pages/mythology.py"),
    ("AI Assistant", "pages/ai_assistant.py"),
    ("Entertainment", "pages/entertainment.py"),
    ("Messages", "pages/messages.py"),
]

st.markdown("### ")

# Render cards in rows of 3
for i in range(0, len(cards), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(cards):
            title, link = cards[i + j]
            with cols[j]:
                st.markdown(
                    f"""<a href='/{link}' target='_self'>
                            <div class='note-card' style='font-size:{font_size}px'>
                                {title}
                            </div>
                        </a>""",
                    unsafe_allow_html=True
                )


# Help icon
st.markdown("""
<div class='help-icon'>
    <a href="#"><img src='https://img.icons8.com/ios-filled/30/help.png' title='Help'/></a>
    <span style='font-size: 14px;'>Help</span>
</div>
""", unsafe_allow_html=True)
