import streamlit as st
from ctransformers import AutoModelForCausalLM

# Set page configuration
st.set_page_config(page_title="GPT-3 Style Demo", page_icon="🤖")

# Add a title
st.title("🤖 GPT-3 Style Language Model Demo")

@st.cache_resource
def load_model():
    return AutoModelForCausalLM.from_pretrained(
        "TheBloke/Llama-2-7B-Chat-GGML",
        model_file="llama-2-7b-chat.ggmlv3.q4_0.bin",
        model_type="llama",
        max_new_tokens=256,
        temperature=0.7
    )

llm = load_model()

# Function to generate responses
def generate_response(input_text):
    try:
        response = llm(input_text)
        st.info(response)
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
st.caption("This is a demo application using a GPT-3 style model (Llama 2). Responses may vary in quality and appropriateness.")
