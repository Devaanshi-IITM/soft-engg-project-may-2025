import streamlit as st
from datetime import datetime
import os

# -------------------------------
# Page Settings
# -------------------------------
st.set_page_config(page_title="Messages", page_icon="📨", layout="wide")

# -------------------------------
# Constants
# -------------------------------
CURRENT_USER_ID = 1

contacts = [
    {"user_id": 2, "name": "Alice"},
    {"user_id": 3, "name": "Bob"},
]

test_messages = {
    2: [
        {"sender_id": 2, "message_text": "Hey there!", "timestamp": "10:00 AM"},
        {"sender_id": 1, "message_text": "Hi Alice, how are you?", "timestamp": "10:01 AM"},
        {"sender_id": 2, "message_text": "Doing well, thanks!", "timestamp": "10:03 AM"},
    ],
    3: [
        {"sender_id": 3, "message_text": "Did you see the news today?", "timestamp": "9:00 AM"},
        {"sender_id": 1, "message_text": "Yeah, pretty interesting stuff.", "timestamp": "9:05 AM"},
    ],
}

# -------------------------------
# Session State Init
# -------------------------------
if "chat_with" not in st.session_state:
    st.session_state.chat_with = None
if "font_size" not in st.session_state:
    st.session_state.font_size = 16

font_size = st.session_state.font_size

# -------------------------------
# Sidebar 
# -------------------------------
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

# -------------------------------
# Main Page Title
# -------------------------------
st.markdown(f"<h1 style='color: #1e3a8a; font-size: {font_size + 10}px;'>📨 Messages</h1>", unsafe_allow_html=True)

# -------------------------------
# Chat List View
# -------------------------------
if not st.session_state.chat_with:
    st.markdown(f"<h3 style='font-size: {font_size + 2}px;'>Chats</h3>", unsafe_allow_html=True)

    for user in contacts:
        last_msg = test_messages[user["user_id"]][-1]["message_text"] if test_messages.get(user["user_id"]) else "No messages yet."
        last_time = test_messages[user["user_id"]][-1]["timestamp"] if test_messages.get(user["user_id"]) else ""
        if st.button(f"{user['name']} - {last_msg}", use_container_width=True, key=f"user_{user['user_id']}"):
            st.session_state.chat_with = user
            st.rerun()
        st.markdown(f"""
            <div style='border: 1px solid #ccc; padding: 10px 15px; border-radius: 10px; margin-bottom: 10px;
            background-color: #f1f5f9; font-size: {font_size}px;'>
                <strong>{user['name']}</strong><br>
                <span style='color: #555;'>{last_msg}</span>
                <div style='text-align: right; font-size: {font_size - 4}px; color: gray;'>{last_time}</div>
            </div>
        """, unsafe_allow_html=True)

# -------------------------------
# Chat View
# -------------------------------
else:
    contact = st.session_state.chat_with

    # Back button
    if st.button("⬅ Back to Chats", key="back_to_chats"):
        st.session_state.chat_with = None
        st.rerun()

    st.markdown(f"<h3 style='color: #1e3a8a;'>Chat with {contact['name']}</h3>", unsafe_allow_html=True)

    # Chat messages
    st.markdown(f"<div style='max-height: 400px; overflow-y: auto; padding: 10px; background-color: #f8fafc; border-radius: 8px; margin-bottom: 80px;'>", unsafe_allow_html=True)

    messages = test_messages.get(contact["user_id"], [])
    for msg in messages:
        align = "right" if msg["sender_id"] == CURRENT_USER_ID else "left"
        bg_color = "#dcf8c6" if msg["sender_id"] == CURRENT_USER_ID else "#ffffff"
        border = "none" if msg["sender_id"] == CURRENT_USER_ID else "1px solid #ccc"
        st.markdown(f"""
            <div style='text-align: {align}; margin-bottom: 10px;'>
                <span style='background-color: {bg_color}; padding: 10px 15px; border-radius: 12px;
                    display: inline-block; max-width: 70%; border: {border}; font-size: {font_size}px;'>
                    {msg["message_text"]}
                </span><br>
                <small style='font-size: {font_size - 4}px;'>{msg["timestamp"]}</small>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    # Fixed reply bar
    st.markdown(f"""
        <style>
            .reply-box {{
                position: fixed;
                bottom: 15px;
                left: 380px;
                right: 30px;
                background-color: #f1f5f9;
                padding: 10px;
                box-shadow: 0 -2px 5px rgba(0,0,0,0.05);
                border-radius: 10px;
                z-index: 999;
            }}
        </style>
        <div class="reply-box">
    """, unsafe_allow_html=True)

    # Streamlit form inside the styled reply box
    with st.form("send_form", clear_on_submit=True):
        new_msg = st.text_input("Message", placeholder="Type your message...", label_visibility="collapsed")
        send = st.form_submit_button("Send")
        if send and new_msg.strip():
            test_messages[contact["user_id"]].append({
                "sender_id": CURRENT_USER_ID,
                "message_text": new_msg.strip(),
                "timestamp": datetime.now().strftime("%I:%M %p")
            })
            st.rerun()

    st.markdown("</div>", unsafe_allow_html=True)

