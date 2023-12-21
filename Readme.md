# Conversational Q&A Chatbot

## Overview

This project is a simple conversational question and answer (Q&A) chatbot developed using OpenAI's language model. The chatbot utilizes the Streamlit framework for the user interface and communicates with the OpenAI API to generate responses.

## Features

- **Conversational Q&A:** Engage in natural language conversations with the chatbot.
- **Streamlit UI:** User-friendly interface for interaction.
- **OpenAI Integration:** Leverages OpenAI's language model for generating responses.
- **Dynamic Conversation Flow:** Maintains a flow of messages to simulate a conversation.

## Setup

### Requirements

Make sure you have the following installed:

- Python 3.x
- [Streamlit](https://streamlit.io/)
- [OpenAI Python API](https://beta.openai.com/docs/)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Fortunatetech/Simple-Conversational-chatbot-with-Streamlit.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. [Set up API key](https://platform.openai.com/docs/quickstart?context=python)

4. Run the application:

   ```bash
   streamlit run chatbot_app.py
   ```

## Usage

1. Access the chatbot through the provided Streamlit URL.
2. Enter your questions in the input field.
3. Click the "Ask the question" button to receive responses.

## Customization

- Adjust OpenAI model parameters in the code (e.g., temperature).
- Customize the initial system message and conversation flow.
