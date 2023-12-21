# Import necessary libraries
import os
from dotenv import load_dotenv
import streamlit as st

from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI

from secret_key import openapi_key

# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = openapi_key

# Streamlit UI Configuration
st.set_page_config(
    page_title="TechAssist Chatbot",
    page_icon=":robot_face:",
    layout="wide"
)

# Read HTML and CSS files
with open('templates/index.html', 'r') as html_file:
    html_content = html_file.read()

with open('templates/style.css', 'r') as css_file:
    css_content = css_file.read()

# Add custom CSS and HTML
st.markdown(f"""
    <style>
        {css_content}
    </style>
""", unsafe_allow_html=True)

# Display your custom HTML content
st.markdown(html_content, unsafe_allow_html=True)

# Initialize Chat Model
chat = ChatOpenAI(temperature=0.6)

# Session State Initialization
st.session_state['flowmessages'] = st.session_state.get('flowmessages', [
    SystemMessage(content="Welcome! I'm TechAssist, your Tech AI assistant.")
])

# User Input Section
user_input = st.text_input("Ask me anything about technology:", key="input")

# Handle User Interaction
if st.button("Ask the question"):
    st.session_state['flowmessages'].append(HumanMessage(content=user_input))
    answer = chat(st.session_state['flowmessages'])
    st.session_state['flowmessages'].append(AIMessage(content=answer.content))

    # Display Response
    st.subheader("TechAssist's Response:")
    st.write(answer.content)
