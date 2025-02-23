import re
import streamlit as st
import requests


WEBHOOK_URL = st.secrets ["WEBHOOK_URL"]

def is_valid_email(email):
    # Besic regex pettern for email validaion
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Submit")
    
        if submit_button:
            if not WEBHOOK_URL:
                st.error("Email serviece is not setup. Please try again later.", icon="📧")
                st.stop()
                
            if not name:
                st.error("Name is required.", icon="🚹")
                st.stop()
            
            if not email:
                st.error("Email is required.", icon="📨")
                st.stop()  
                
            if not is_valid_email(email):
                st.error("Invalid Email Address.", icon="📌")
                st.stop()
                
            if not message:
                st.error("Message is required.", icon="💬")
                st.stop()
                
            #--- Prepare the date pagload send it to the specified webhook_url
            data = {"email": email, "name": name, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)
            
            if response.status_code == 200:
                st.success("Your message has been sent successfully! 🎉", icon="🚀")
                st.balloons()
            else:
                st.error("Failed to send your message. Please try again later.", icon="🚫")
            
                
                
            