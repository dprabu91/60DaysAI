import streamlit as st

st.title("Welcome to My Streamlit App")

name = st.text_input("Enter your name:")

if st.button("Submit"):
    if name:
        st.write(f"Hello, {name}! Welcome to the Streamlit app.")
    else:
        st.warning("Please enter your name before submitting.")
        