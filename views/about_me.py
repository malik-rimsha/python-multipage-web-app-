import streamlit as st

from forms.contact import contact_from

@st.dialog("Contact Me")
def show_contact_form():
    contact_from()

# -- HERO SECTION ---
col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
with col1:
    st.image("./assets/profile.jpg", width=230)

with col2:
    st.title("Malik Rimsha", anchor=False)
    st.write(
        "Skilled full-stack developer passionate about building interactive web applications, dynamic dashboards, and AI-driven solutions."
    )
    if st.button("📞Contact Me"):
        show_contact_form()
        
        #--- EXPERIENCE & QUALIFICATION ---
st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - Relevant Experience!
    - Academic Projects and Assignments
    - Hackathons and Competitions:
    - Participated in and completed several hackathons, including a 7-day e-commerce hackathon.
      Built interactive and scalable solutions like a marketplace.
    - E-Commerce Projects:
    - Developed an e-commerce website using Next.js, TypeScript, and Sanity CMS.
    - Implemented features such as dynamic routing, cart functionality, and API integrations.
    - Interactive Resume Builder:
    - Created an Interactive Resume Builder during a 24-hour hackathon.
    - Focused on user-friendly design and dynamic features.
    """
)

#---SKILLS---
st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Proficient in TypeScript (ES6+) for writing modern and maintainable code.
    - Skilled in developing web applications using Next.js with a focus on performance and SEO.
    - Strong knowledge of semantic HTML, modern CSS, and responsive design principles.
    - Experienced in version control with Git and collaborating on projects using GitHub.
    - Familiar with Bootstrap for rapid, responsive layout development.
    - Knowledgeable in Shadcn for creating customizable and reusable UI components
    """
)