from utils.style import apply_base_style, show_header
import streamlit as st
import base64

# Apply shared styling
apply_base_style()

# Navbar
with st.sidebar:
    st.markdown("<h1 style='color: #fbeee6;'>Welcome!</h1>", unsafe_allow_html=True)

    # Font size slider
    font_size = st.slider("Font size", 12, 28, 18)

    # Logout button
    if st.button("Logout"):
        st.session_state.logged_in = False
        st.experimental_rerun()


# ---- MAIN CONTENT ----
st.markdown(f"""
    <h1 style='margin-bottom: 0; color: #1a5276;'><b>Saathi</b>
        <span style='font-size: {font_size * 0.8}px; font-family: cursive; color: #1a5276; margin-left: 8px;'>
            Your companion
        </span>
    </h1>""", unsafe_allow_html=True)

st.markdown(f"<p style='font-size: {font_size * 0.8}px;'>Selected font size: {font_size}px</p>", unsafe_allow_html=True)


st.divider()


# Cards
cards = [
    ("Health & Reminders", "pages/Health.py", "images/health.png"),
    ("Mythology", "pages/Mythology_Homepage.py", "images/mythology.png"),
    ("AI Assistant", "pages/AI_assistant.py", "images/ai_assistant.png"),
    ("Entertainment", "pages/Entertainment.py", "images/entertainment.png"),
    ("Messages", "pages/Messages_app.py", "images/messages.png"),
]

st.markdown("### ")

def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{encoded}"


# Render cards in rows of 3
for i in range(0, len(cards), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(cards):
            title, link, image_path = cards[i + j]
            img_base64 = get_image_base64(image_path)

            with cols[j]:
                st.markdown(
                    f"""
                    <a href='/{link}' target='_self'>
                        <div class='note-card'>
                            <img src='{img_base64}' alt='{title} icon'/>
                            <div class='card-title' style='font-size:{font_size}px'>{title}</div>
                        </div>
                    </a>
                    """,
                    unsafe_allow_html=True
                )
