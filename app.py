import streamlit as st
from transformers import pipeline

# Set page configuration
st.set_page_config(page_title="Advanced LLM Demo", page_icon="🚀")

# Add a title
st.title("🚀 Advanced Language Model Demo")

@st.cache_resource
def load_model():
    return pipeline("text2text-generation", model="facebook/bart-large-cnn")

generator = load_model()

# Function to generate responses
def generate_response(input_text):
    try:
        response = generator(input_text, max_length=150, num_return_sequences=1)
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



# Add some usage tips
st.sidebar.header("Usage Tips")
st.sidebar.write("""
- For best results, provide clear and detailed prompts.
- The model is particularly good at summarization and rephrasing.
- Try asking it to explain concepts or generate short articles.
- Remember, while advanced, it may still produce unexpected results.
""")
