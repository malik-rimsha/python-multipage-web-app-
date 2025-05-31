import random
import time

import streamlit as st


# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "See my professional work and network on LinkedIn: https://www.linkedin.com/in/malik-rimsha-4319472ba?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app",
            "Explore my projects and source code on GitHub: https://github.com/malik-rimsha",
            "View my deployed websites and web apps on Netlify: https://app.netlify.com/teams/malik-rimsha/sites",
            "Discover my interactive apps and dashboards on Streamlit: https://share.streamlit.io/user/malik-rimsha",
            "Check out my published packages on NPM: https://www.npmjs.com/~malik-rimsha",
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})