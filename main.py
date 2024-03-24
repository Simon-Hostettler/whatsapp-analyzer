import matplotlib, mplcairo
import matplotlib.pyplot as plt
import seaborn as sns
from loading import *
from poster import *
from plt_stylesheet import stylesheet
from platform import system


if __name__ == "__main__":
    # change backend to render emojis correctly
    if system().lower() == "darwin":
        matplotlib.use("module://mplcairo.macosx")

    plt.rcParams.update(stylesheet)

    create_folders_if_missing()

    # load chat
    chat = load_file("_chat 11.txt")
    user1, user2, u1_messages, u2_messages = split_user_messages(chat)

    create_poster(user1, user2, u1_messages, u2_messages)
