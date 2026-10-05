import streamlit as st
st.title("Welcome to my first app")
st.write("Hello")
name = st.text_input("Enter your name...")
message = st.chat_input("send a chat...")
st.write("Hello", name)
if st.button("Submit"):
    st.write("Hello", name)