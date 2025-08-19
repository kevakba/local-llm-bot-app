import streamlit as st
import requests

MODEL = "llama2:latest"
OLLAMA_API = "http://localhost:11434/api/generate"

st.title("Simple Local Chatbot")

if "history" not in st.session_state:
    st.session_state.history = []

user_input = st.text_input("Enter your message:")

if user_input:
    st.session_state.history.append(f"User: {user_input}")

    prompt = "\n".join(st.session_state.history) + "\nAssistant:"

    response = requests.post(OLLAMA_API, json={"model": MODEL, "prompt": prompt, "stream": False})
    answer = response.json().get("response", "No response")

    st.session_state.history.append(f"Assistant: {answer}")

for line in st.session_state.history:
    st.write(line)
