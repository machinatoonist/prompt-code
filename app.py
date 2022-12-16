import streamlit as st
import openai

# Title for app
st.title("OpenAI Code Suggestion App")

model_options = ["text-davinci-002", "text-davinci-003",
                 "text-embedding-ada-002", "babbage-code-search-code",
                 "ada-code-search-code", "text-similarity-davinci-001",
                 "code-davinci-002", "code-search-ada-text-001"
                 ]

with st.sidebar:
    # Create a slider to control the temperature of the model
    temperature = st.slider("Increase the temperature for wider variations", 
        min_value=0.0, 
        max_value=1.0, 
        value=0.5, 
        step=0.1)
    # Select box with options for model to use with default value  = "text-davinci-002"
    st.selectbox("Select model", model_options, index=2)
    
    # Get API key from user
    api_key = st.text_input("Enter your OpenAI API key:", type="password")

# Get prompt from user
prompt = st.text_area("Enter your free text prompt:", 
                    placeholder="eg: 'write a python script to print hello world'",
                    height=200)

# Set up request to ChatGPT API
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
data = {
    "prompt": prompt,
    "max_tokens": 2048
}

# Submit button
if st.button("Submit"):
    openai.api_key = api_key
    # Send request and get response
    response = openai.Completion.create(
        # engine="text-embedding-ada-002",
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n = 1,
        stop=None,
        temperature=temperature)
    
    # Display response
    st.code(response["choices"][0]["text"])

st.text("Get your own OpenAI API key at https://openai.com/api/")
