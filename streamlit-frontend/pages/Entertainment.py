import streamlit as st
import base64

from utils.style import apply_base_style, render_sidebar
apply_base_style()

# Sidebar
with st.sidebar:

    font_size = render_sidebar()

st.markdown(
    "<h1 style='color: #154360;'>Game Zone</h1>", 
    unsafe_allow_html=True
)

games = [
    ("Fruit Ninja", "https://poki.com/en/g/fruit-ninja", "images/fruitninja.png"),
    ("Sudoku", "https://poki.com/en/g/sudoku-calendar", "images/sudoku.png"),
    ("Subway Surfers", "https://poki.com/en/g/subway-surfers", "images/subwaysurfers.png"),
    ("Ludo", "https://poki.com/en/g/ludo-multiplayer", "images/ludo.png"),
    ("Master Chess", "https://poki.com/en/g/master-chess", "images/chess.png"),
    ("Tic tac toe", "https://poki.com/en/g/tic-tac-toe", "images/tictac.png"),
    ("Sweet World", "https://poki.com/en/g/sweet-world", "images/sweetworld.png"),
    ("Bubble Shooter", "https://poki.com/en/g/space-bubbles", "images/bubbleshooter.png"),
    ("Pool club", "https://poki.com/en/g/pool-club", "images/poolclub.png")
]


def get_image_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{encoded}"

st.markdown("### ")

# Render cards in rows of 3
for i in range(0, len(games), 3):
    cols = st.columns(3)
    for j in range(3):
        if i + j < len(games):
            title, link, image_path = games[i + j]
            img_base64 = get_image_base64(image_path)

            with cols[j]:
                st.markdown(
                    f"""
                    <a href='{link}' target='_blank'>
                        <div class='note-card'>
                            <img src='{img_base64}' alt='{title} icon'/>
                            <div class='card-title' style='font-size:{font_size}px'>{title}</div>
                        </div>
                    </a>
                    """,
                    unsafe_allow_html=True
                )
