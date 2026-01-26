import streamlit as st
import requests

FLASK_API_URL = "http://127.0.0.1:5000/assist"

st.set_page_config(page_title="Personal Assistant", page_icon="🤖")

st.title("🤖 Personal Assistant")
st.write("Ask me anything!")

user_input = st.text_input("Your question:")

if st.button("Ask"):
    if user_input:
        response = requests.post(
            FLASK_API_URL,
            json={"message": user_input}
        )

        if response.status_code == 200:
            assistant_reply = response.json()["response"]
            st.success(assistant_reply)
        else:
            st.error("Error connecting to assistant")
    else:
        st.warning("Please enter a message")
