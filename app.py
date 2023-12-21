# # Conversational Q&A Chatbot
# import os
# from dotenv import load_dotenv
# import streamlit as st

# from langchain.schema import HumanMessage, SystemMessage, AIMessage
# from langchain.chat_models import ChatOpenAI

# from secret_key import openapi_key
# import os
# os.environ['OPENAI_API_KEY'] = openapi_key

# # Streamlit UI
# st.set_page_config(page_title="Conversational Q&A Chatbot")
# st.header("Hey, Let's Chat")

# load_dotenv()

# chat = ChatOpenAI(temperature=0.6)

# if 'flowmessages' not in st.session_state:
#     st.session_state['flowmessages'] = [
#         SystemMessage(content="Yor are a Tech AI assitant")
#     ]

# # Function to load OpenAI model and get respones


# def get_chatmodel_response(question):

#     st.session_state['flowmessages'].append(HumanMessage(content=question))
#     answer = chat(st.session_state['flowmessages'])
#     st.session_state['flowmessages'].append(AIMessage(content=answer.content))
#     return answer.content


# input = st.text_input("Input: ", key="input")
# response = get_chatmodel_response(input)

# submit = st.button("Ask the question")

# # If ask button is clicked

# if submit:
#     st.subheader("The Response is")
#     st.write(response)
