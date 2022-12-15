import streamlit as st
import openai


# Get API key from user
api_key = st.text_input("Enter your ChatGPT API key:", type="password")

# Get prompt from user
prompt = st.text_area("Enter your free text prompt:", 
                       placeholder="eg: 'write a python script to print hello world'",
                       height=200)

# Create a slider to control the temperature of the model
temperature = st.slider("Increase the temperature for more variations", 0.0, 1.0, value=0.5, step=0.1)

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
    engine="text-davinci-002",
    prompt=prompt,
    max_tokens=1024,
    n = 1,
    stop=None,
    temperature=temperature)
    
    # Display response
    st.code(response["choices"][0]["text"])
    
if __name__ == "__main__":
    st.header("ChatGPT Code Generator")
    st.text("Enter your ChatGPT API key and prompt to generate suggested code in any language you specify.")
    st.text("Note: Your API key is private and should not be shared with anyone.")

openai.Completion.create()