import streamlit as st

 # ---PAGE SETUP---
about_page = st.Page(
    page="views/about_me.py",
    title="About Me",
    icon=":material/account_circle:",
    default=True,
)
project_1_page = st.Page(
    page="views/sales_dashboard.py",
    title="Sales Dashboard",
    icon=":material/bar_chart:",
)
project_2_page = st.Page(
    page="views/chatbot.py",
    title="Chatbot",
    icon=":material/smart_toy:",
)

# --- NAVIGATION SETUP [WITH SECTIONS] ---
pg = st.navigation(
    {
        "Info": [about_page],
        "Projects": [project_1_page, project_2_page],
    }
)

# ---SHARED ON ALL PAGES ---
#st.logo("./assets/Mr.png "),
st.sidebar.markdown("Made with ❤️ by [Malik](https://www.linkedin.com/in/malik-rimsha-4319472ba?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)")
# ---RUN NAVIGATION --- 
pg.run()