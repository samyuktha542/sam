import streamlit as st
import google.generativeai as genai


st.title("welcome to gemini chat")

genai.configure(api_key="AIzaSyDpus7h8UrNLhIvp2JKlJx9y5-bJh2jbZQ")

text = st.text_input("enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

response = chat.send_message(text)
st.write(response.text)