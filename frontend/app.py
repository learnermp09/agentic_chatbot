import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title = "LLM Chatbot",
    page_icon = "frontend/decodixAI.png"
)

st.title("✨LLM AI Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
prompt = st.chat_input("Ask me anything...")

if prompt:

    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

        # Call FastAPI
    try:

        response = requests.post(
            API_URL,
            json={
                "message": prompt
            },
            timeout=60
        )


        if response.status_code == 200:

            answer = response.json()["response"]

        else:

            answer = f"API Error: {response.status_code}"


    except requests.exceptions.RequestException as e:

        answer = f"Could not connect to FastAPI: {e}"


    # Display assistant response
    with st.chat_message("assistant"):
        st.markdown(answer)


    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
