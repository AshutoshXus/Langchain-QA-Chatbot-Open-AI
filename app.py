# Q&A Chatbot 
from langchain_community.llms import OpenAI
from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os

## Function to load OpenAI model and get reaponse

def get_openap_response(question):
    llm = OpenAI(openai_api_key=os.getenv("OPEN_API_KEY"),model_name="gpt-3.5-turbo-instruct", temperature=0.6)
    response = llm(question)
    return response


##initilisze our streamlit app

st.set_page_config(page_title="Q&A Demo")

st.header("Langchain Application")

input = st.text_input("Input: ", key="input")
response = get_openap_response(input)

submit = st.button("Ask the question")


## If ask button is clicked

if submit:
    st.subheader("The response is ")
    st.write(response)