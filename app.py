import streamlit as st
from transformers import pipeline

# Set page configuration
st.set_page_config(page_title="LLM Demo", page_icon="🤖")

# Add a title
st.title("🤖 Language Model Demo")

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="gpt3")

generator = load_model()

# Function to generate responses
def generate_response(input_text):
    try:
        response = generator(input_text, max_length=100, num_return_sequences=1)
        st.info(response[0]['generated_text'])
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

# Text area for user input
input_text = st.text_area("Enter your prompt here:", height=100)

# Generate response when button is clicked
if st.button("Generate Response"):
    if input_text:
        with st.spinner("Generating response..."):
            generate_response(input_text)
    else:
        st.warning("Please enter a prompt.")

# Add a footnote
st.caption("This is a demo application using a public GPT-2 model. Responses may vary in quality and appropriateness.")
