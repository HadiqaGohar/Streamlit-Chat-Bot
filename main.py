import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
# API_KEY = os.getenv("GEMINI_API_KEY")
API_KEY = st.secrets["google"]["api_key"] 

# Configure Gemini AI
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")  # Use an available model

# Streamlit UI
st.set_page_config(page_title="Gemini Chatbot", layout="centered")
st.title("🤖 Gemini AI Chatbot")

# Initialize chat history

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Handle user input
if hasattr(st, "chat_input"):
    user_input = st.chat_input("Type your message...")
else:
    user_input = st.text_input("Type your message...")

# Process user input
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Get AI response
    response = model.generate_content(user_input)
    bot_response = response.text if response else "Sorry, I couldn't understand that."

    # Add AI response to history
    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    with st.chat_message("assistant"):
        st.markdown(bot_response)


