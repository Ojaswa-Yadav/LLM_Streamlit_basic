import streamlit as st
from langchain.llms import OpenAI

# Setting up the title for your app
st.title("LLM-App 🧠")

# API key input field
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")

# Function to generate a response from the OpenAI model
def generate_response(input_text):
    # Initializing the OpenAI model with the provided API key
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    # Generating and displaying the response
    response = llm(input_text)
    st.info(response)

# Input text box for the user to enter a prompt
input_text = st.text_area("Enter your prompt here:")

# Button to trigger the response generation
if st.button("Generate Response"):
    if openai_api_key:
        if input_text:
            generate_response(input_text)
        else:
            st.warning("Please enter a prompt.")
    else:
        st.warning("Please enter your OpenAI API Key.")

