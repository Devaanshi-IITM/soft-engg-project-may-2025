#frontend code for login

import streamlit as st
import requests

BASE_URL = "http://localhost:8000"
HEADER_IMAGE_URL = "https://cdn-icons-png.flaticon.com/128/11647/11647318.png"

if "stage" not in st.session_state:
    st.session_state.stage = "otp-request"
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True

def set_theme():
    if st.session_state.dark_mode:
        st.markdown("""
            <style>
            body {
                background-color: #121212;
                color: #FFFFFF;
            }
            .stApp {
                background-color: #121212;
                color: #FFFFFF;
            }
            .login-box {
                background-color: #1E1E1E;
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 0 10px #00000055;
                max-width: 450px;
                margin: auto;
            }
            </style>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <style>
            .login-box {
                background-color: #f5f5f5;
                padding: 2rem;
                border-radius: 15px;
                box-shadow: 0 0 10px #cccccc55;
                max-width: 450px;
                margin: auto;
            }
            </style>
        """, unsafe_allow_html=True)

set_theme()

st.markdown(f"""
    <div style='text-align: center; margin-bottom: 20px;'>
        <img src="{HEADER_IMAGE_URL}" width="128" height="128" style='border-radius: 10px;'/>
    </div>
""", unsafe_allow_html=True)

st.sidebar.markdown("### Toggle Theme")
st.sidebar.toggle("Dark Mode", value=True, key="dark_mode", on_change=set_theme)

st.markdown("<h2 style='text-align:center;'>Welcome to Saathi</h2>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align:center;color:red;'>Sign-in with OTP</h5>", unsafe_allow_html=True)
with st.container():
    #st.markdown("<div class='login-box'>", unsafe_allow_html=True)

    if st.session_state.stage == "otp-request":
        email = st.text_input("Enter your Email ID", placeholder="myemail@gmail.com", key="email_input")
        if st.button("Send OTP"):
            res = requests.post(f"{BASE_URL}/request-otp", json={"email": email})
            if res.status_code == 200:
                st.session_state.email = email
                st.session_state.stage = "otp-verify"
                st.success("OTP sent to your email!")
            else:
                st.error("Failed to send OTP")

    if st.session_state.stage == "otp-verify":
        otp = st.text_input("Enter OTP", key="otp_input")
        if st.button("Verify OTP"):
            res = requests.post(f"{BASE_URL}/verify-otp", json={"email": st.session_state.email, "otp": otp})
            if res.status_code == 200:
                st.session_state.user = res.json()["user"]
                st.session_state.stage = "profile"
            else:
                st.error("Invalid or expired OTP")

    elif st.session_state.stage == "profile":
        st.subheader("Edit Your Profile")

        user = st.session_state.user
        name = st.text_input("Full Name", user.get("name", ""))
        dob = st.date_input("Date of Birth")
        gender = st.selectbox("Gender", ["", "Male", "Female", "Other", None],
                              index=["", "Male", "Female", "Other", None].index(user.get("gender", "")))
        mobile = st.text_input("Mobile Number (optional)", user.get("mobile", ""))

        if st.button("Update Profile"):
            res = requests.post(f"{BASE_URL}/update-profile", json={
                "email": st.session_state.email,
                "name": name,
                "dob": str(dob),
                "gender": gender,
                "mobile": mobile
            })
            if res.status_code == 200:
                st.success("Profile updated successfully")
            else:
                st.error("Failed to update profile")

    #st.markdown("</div>", unsafe_allow_html=True)
