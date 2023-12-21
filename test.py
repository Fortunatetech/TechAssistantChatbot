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

# Page Header
st.title("TechAssist - Your Intelligent Tech Companion")
st.markdown(
    "Welcome to TechAssist, your go-to platform for tech-related queries. "
    "Ask us anything about technology, and we'll provide insightful answers!"
)

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

# Additional Information and Footer
st.sidebar.header("About TechAssist")
st.sidebar.markdown(
    "TechAssist is powered by state-of-the-art natural language processing models. "
    "Feel free to ask any tech-related questions, and we'll provide you with the best answers."
)

# Add any other information, links, or features that differentiate your chatbot from rivals
# Consider incorporating branding, real-time updates, or integration with additional services.

# Provide Contact or Support Information
st.sidebar.header("Contact Support")
st.sidebar.markdown(
    "For assistance or inquiries, reach out to our support teaNm at support@techassist.com."
)

# Disclaimer
st.sidebar.markdown(
    "TechAssist is an AI-powered chatbot designed to assist with general tech queries. "
    "For specific or critical issues, consult with a professional in the respective field."
)
