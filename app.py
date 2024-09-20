import streamlit as st
from langchain_openai import OpenAI

# Add your OpenAI API Key
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

# Function to generate responses
def generate_response(input_text):
    try:
        llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
        response = llm(input_text)
        st.info(response)
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        st.error("Please check your OpenAI API key and ensure you have available credits.")

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
