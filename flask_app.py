# Import necessary libraries
from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
import streamlit as st

from langchain.schema import HumanMessage, SystemMessage, AIMessage
from langchain.chat_models import ChatOpenAI

from secret_key import openapi_key

# Set OpenAI API key
os.environ['OPENAI_API_KEY'] = openapi_key


app = Flask(__name__)

# Initialize Chat Model
chat = ChatOpenAI(temperature=0.6)

# Session State Initialization
app.config['flowmessages'] = [
    SystemMessage(content="Welcome! I'm TechAssist, your Tech AI assistant.")
]


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def ask_question():
    user_input = request.form.get('user_input')
    app.config['flowmessages'].append(HumanMessage(content=user_input))
    answer = chat(app.config['flowmessages'])
    app.config['flowmessages'].append(AIMessage(content=answer.content))
    return render_template('index.html', answer=answer.content)


if __name__ == '__main__':
    app.run(debug=True)
