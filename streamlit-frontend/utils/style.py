import streamlit as st

def apply_base_style():
    st.set_page_config(layout="wide")
    st.markdown("""
        <style>

        html, body, [data-testid="stAppViewContainer"], [data-testid="stAppViewBlockContainer"] {
            background-color: #fbeee6;
            min-height: 100vh;
        }

        [data-testid="stSidebar"] {
            background-color: #1a5276;
            padding: 20px;
        }

        [data-testid="stSidebar"] label {
            color: #fbeee6;   
            font-weight: bold;
        }

        

        .note-card {
            position: relative;
            aspect-ratio: 1 / 1;  
            height: auto;         
            width: 100%;         
            background-color: rgba(255, 255, 255, 0.8);
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 10px;
            text-align: center;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: pointer;
            transition: transform 0.2s;
            font-family: 'Comic Sans MS', cursive;
            margin-bottom: 15px;
            flex-direction: column;
            overflow: hidden;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        .note-card img {
            position: absolute; 
            top: 0; left: 0; right: 0; bottom: 0;
            width: 100%;
            height: 100%;
            object-fit: cover; 
        }
        .note-card .card-title {
            position: absolute; 
            bottom: 0;
            left: 0;
            width: 100%;
            background: rgba(0,0,0,0.5);
            color: #fff;
            text-align: center;
            padding: 8px;
            font-family: 'Comic Sans MS', cursive;
        }
        .note-card:hover {
            transform: scale(1.02);
            background-color: #fbb;
        }


        </style>
    """, unsafe_allow_html=True)

def show_header(page_title):
    st.markdown(f"<h3 style='margin-bottom: 0;'>{page_title}</h3>", unsafe_allow_html=True)

