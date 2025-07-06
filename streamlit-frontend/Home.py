from utils.style import apply_base_style, show_header, render_sidebar
import streamlit as st
import base64

# Apply shared styling
apply_base_style()

# Sidebar
with st.sidebar:

    font_size = render_sidebar()



# ---- MAIN CONTENT ----
st.markdown(f"""
    <h1 style='margin-bottom: 0; color: #154360;'><b>Saathi</b>
        <span style='font-size: {font_size * 0.8}px; font-family: cursive; color: #154360; margin-left: 8px;'>
            Your companion
        </span>
    </h1>""", unsafe_allow_html=True)

st.markdown(f"<p style='font-size: {font_size * 0.8}px;'>Selected font size: {font_size}px</p>", unsafe_allow_html=True)


st.divider()


# Cards
cards = [
    ("Health & Reminders", "health", "images/health.png"),
    ("Mythology", "Mythology_Homepage", "images/mythology.png"),
    ("AI Assistant", "ai_assistant", "images/ai_assistant.png"),
    ("Entertainment", "entertainment", "images/entertainment.png"),
    ("Messages", "Messages_app", "images/messages.png"),
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
                    <a href='{link}' target='_self'>
                        <div class='note-card'>
                            <img src='{img_base64}' alt='{title} icon'/>
                            <div class='card-title' style='font-size:{font_size}px'>{title}</div>
                        </div>
                    </a>
                    """,
                    unsafe_allow_html=True
                )
