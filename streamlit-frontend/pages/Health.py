import streamlit as st

from utils.style import apply_base_style, render_sidebar
apply_base_style()

# Sidebar
with st.sidebar:

    font_size = render_sidebar()

st.title("Health")
st.write("health page")