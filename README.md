# prompt-code
Calls the ChatGPT API to return a response to your free text prompt.

This repository can be used to launch your own Streamlit app that you can host on Streamlit Cloud.

First you will need to get your own personal API key via OpenAI. 

One caveat is that this application does not yet maintain session state in the way that you can in OpenAI's native app. The native OpenAI interface allows you to refer to previous queries as you would in a typical chat app. Even still, if you are careful in the way you craft your initial text prompt with this Streamlit app you can get some surprisingly thorough code suggestions.

The benefit of having using your own API key and application is that you will likely have fewer dropouts and the ability to make further customisations.  For example, in this demonstration you can alter the temperature of the model to see how the suggestions vary for the same text prompt.

Once you have an API key you can head over to Streamlit Cloud and launch the code directly from the GitHub repository or simply run the app locally using the command:

`streamlit run app.py`

Some example outputs is included. I suggest using version control to record the initial model output, settings and then any changes required to make it work as originally intended.

Here are some ways you might leverage ChatGPT to increase your coding efficiency and productivity:
- **Debugging suggested code** so that is works. Many times the suggested code is not going to work. You can simply copy and paste it into your favourite IDE and test it out. Often the code will work without alteration and other times it will need a few tweaks. If the code is way off target it probably better to improve your prompt and/or change the temperature and try again.
- **Understanding what functional code is doing** by asking ChatGPT how some pasted code works. If you have some code that works but you don't understand it you can paste it in as prompt text with a preface something like "explain how this code works step by step:" and see what happens.
- **Troubleshooting code that is not working** by asking ChatGPT to look for problems in pasted code. Pasting code and errors along with a request for help in debugging the code is another way ChatGPT might help.
- **Drafting starter code for any coding task** at hand in Python, R, SQL and most other languages you can think of. This was the first way I started to play with ChatGPT before I realised the other uses. I even tried using ChatGPT to write the code used to create the Streamlit app you see above with very little success. Naturally, it doesn't do a great job at this task because the current incarnation of the ChatGPT API did not exist in 2021 when the model was trained. I look forward to future model improvements that will no doubt take care of this apparent lack of self-awareness as more training examples of ChatAPI applications are published.
- **Creating new variations on code**. Carefully crafting your text prompt can yield very different results. For example, try adding the phrase "step by step instructions" to any request and see how the suggested code changes. Play with the temperature to get a variety of suggestions for each prompt. The higher the temperature the greater the variety.


