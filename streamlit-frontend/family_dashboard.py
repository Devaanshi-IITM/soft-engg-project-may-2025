import streamlit as st


# App title
st.set_page_config(page_title="Family Dashboard", layout="wide")

# Sidebar
with st.sidebar:
    st.markdown("## 👨‍👩‍👧‍👦 Family Dashboard")
    
    menu = st.radio(
        "Navigation",
        ("Appointments", "Reminders", "Records/Prescriptions"),
        label_visibility="collapsed"  # hides the 'Navigation' label
    )

# Top bar
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown("&nbsp;", unsafe_allow_html=True) 
    search = st.text_input("Search", placeholder="Search...")
with col2:
    st.write(f"Welcome **username!**")
    
# Pages
if menu == "Appointments":
    st.subheader("Upcoming Appointments")
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
    st.subheader("Existing Reminders")
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
    st.subheader("Medical Records / Prescriptions")
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


