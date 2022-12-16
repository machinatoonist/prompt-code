# prompt-code
Calls the ChatGPT API to return a response to your free text prompt.

This repository can be used to launch your own Streamlit app that you can host on Streamlit Cloud.

First you will need to get your own personal API key via OpenAI. 

One caveat is that this application does not yet maintain session state in the way that you can in OpenAI's native app. The native OpenAI interface allows you to refer to previous queries as you would in a typical chat app. Even still, if you are careful in the way you craft your initial text prompt with this Streamlit app you can get some surprisingly thorough code suggestions.

The benefit of having using your own API key and application is that you will likely have fewer dropouts and the ability to make further customisations.  For example, in this demonstration you can alter the temperature of the model to see how the suggestions vary for the same text prompt.

Once you have an API key you can head over to Streamlit Cloud and launch the code directly from the GitHub repository or simply run the app locally using the command:

`streamlit run app.py`

