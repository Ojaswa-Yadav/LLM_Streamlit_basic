import streamlit as st
from langchain.llms import OpenAI

# Add your OpenAI API Key
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

# Function to generate responses
def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    response = llm(input_text)
    st.info(response)

# Text area for user input
input_text = st.text_area("Enter your prompt here:")

# Generate response when button is clicked
if st.button("Generate Response"):
    if openai_api_key:
        if input_text:
            generate_response(input_text)
        else:
            st.warning("Please enter a prompt.")
    else:
        st.warning("Please enter your OpenAI API Key.")
