import streamlit as st
import openai


# Get API key from user
api_key = st.text_input("Enter your ChatGPT API key:", type="password")

# Get prompt from user
prompt = st.text_input("Enter your code prompt:", placeholder="write a python script to print hello world")

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
    temperature=0.5)
    
    # Display response
    st.code(response["choices"][0]["text"])
    
if __name__ == "__main__":
    st.title("ChatGPT Code Generator")
    st.write("Enter your ChatGPT API key and code prompt to generate Python code.")
    st.write("Note: Your API key is private and should not be shared with anyone.")
