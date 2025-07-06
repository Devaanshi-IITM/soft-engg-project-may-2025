import streamlit as st

#---- Page Configuration ----

family_Page = st.Page(
    page="views/family_dashboard.py",
    title="Family Dashboard",
    icon="👪",
    default=True,
    #description="A dashboard for family members to view and manage their activities.",
)

ai_page = st.Page(
    page="views/ai_assistant.py",
    title="AI Dashboard",
    icon="🤖",
)   

#---- Page Navigation ----

page = st.navigation(pages=[family_Page, ai_page])       

# ---- logo shared by all pages ----

st.logo("assets/logo.png")
#---- Run the selected page ----
page.run()
