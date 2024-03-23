# whatsapp-analyzer

This python script analyses interactions between users from a given Whatsapp chatlog and stores results in an infographic.

# Installation

First, install the necessary packages with pip (preferrably in a venv):

```
$ pip install -r requirements.txt
```

If you are on MacOS, you will need to install a different backend for matplotlib to render emojis. This [blog post](https://towardsdatascience.com/how-i-got-matplotlib-to-plot-apple-color-emojis-c983767b39e0) describes how to install mplcairo on your system.

# Usage

How to export a Whatsapp chat history:

1. Go to a users profile
2. Scroll down and select 'Export Chat'
3. Select 'Without media'

This results in a zip file, which you can then extract, and paste the chats.txt into the `chat_logs` folder in the current directory. In the `main.py` file, simply change the string in `load_file("chat.txt")` to the name of your text file.

After running `main.py`, the results should be stored in `output/poster_$user1_$user2.pdf`
