import streamlit as st

def apply_base_style():
    st.set_page_config(layout="wide")
    st.markdown("""
        <style>
        .note-card {
            background-color: #fdd;
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 30px;
            height: 150px;
            text-align: center;
            font-family: 'Comic Sans MS', cursive;
            cursor: pointer;
            transition: transform 0.2s;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .note-card:hover {
            transform: scale(1.02);
            background-color: #fbb;
        }
        .help-icon {
            position: fixed;
            bottom: 20px;
            left: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

def show_header(page_title):
    st.title(f"{page_title}")
    st.markdown("")
