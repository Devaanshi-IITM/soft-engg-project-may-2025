import streamlit as st

from utils.style import apply_base_style, render_sidebar
apply_base_style()

# Sidebar
with st.sidebar:

    font_size = render_sidebar()

st.title("Health")

# Menu
menu = st.radio(
    "Navigation",
    ("Appointments", "Reminders", "Records/Prescriptions"),
    label_visibility="collapsed" 
    )

# Search bar

st.markdown("&nbsp;", unsafe_allow_html=True) 
search = st.text_input("Search", placeholder="Search...")


if menu == "Appointments":
    st.markdown(f"<h3 style='font-size: {font_size}px;'>Upcoming Appointments</h3>", unsafe_allow_html=True)
    
    st.table({
        "Date & Time": ["", "", ""],
        "Consulting Doctor": ["", "", ""],
        "Patient Name": ["", "", ""],
        "Purpose": ["", "", ""],
        "Venue": ["", "", ""],
        "Other Info": ["", "", ""]
    })
    if st.button("Book new appointment"):
        with st.form("new_appointment_form"):
            date_time = st.text_input("Date & Time")
            Consulting_Doctor = st.text_input("Consulting Doctor")
            Patient_Name = st.text_input("Patient Name")
            Purpose = st.text_input("Purpose")
            Venue = st.text_input("Venue")
            other_info = st.text_input("Other Info")
            submitted = st.form_submit_button("Save")
            if submitted:
                st.success("Reminder added successfully!")

elif menu == "Reminders":
    st.markdown(f"<h3 style='font-size: {font_size}px;'>Set Reminders</h3>", unsafe_allow_html=True)
    
    st.table({
        "Reminder Text": ["", "", ""],
        "Frequency": ["", "", ""],
        "Timing": ["", "", ""]
    })

    if st.button("Add new reminder"):
        with st.form("new_reminder_form"):
            reminder_text = st.text_input("Reminder Text")
            frequency = st.text_input("Frequency")
            timing = st.text_input("Timing")
            submitted = st.form_submit_button("Save")
            if submitted:
                st.success("Reminder added successfully!")

elif menu == "Records/Prescriptions":
    st.markdown(f"<h3 style='font-size: {font_size}px;'>Medical Records & Prescriptions</h3>", unsafe_allow_html=True)
    
    st.table({
        "File": ["", "", ""],
        "Date": ["", "", ""],
        "Consulting Doctor": ["", "", ""],
        "Other Info": ["", "", ""]
    })

    if st.button("Add new record"):
        with st.form("new_record_form"):
            file = st.file_uploader("Attach File")
            date = st.date_input("Date")
            consulting_doctor = st.text_input("Consulting Doctor")
            other_info = st.text_input("Other Info")
            submitted = st.form_submit_button("Save")
            if submitted:

                st.success("Record added successfully!")