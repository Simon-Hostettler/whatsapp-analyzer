import matplotlib, mplcairo
import matplotlib.pyplot as plt
import seaborn as sns
from loading import *
from poster import *
from plt_stylesheet import stylesheet


if __name__ == "__main__":
    # change backend to render emojis correctly
    matplotlib.use("module://mplcairo.macosx")

    plt.rcParams.update(stylesheet)

    # load chat
    chat = load_file("chat2.txt")
    user1, user2, u1_messages, u2_messages = split_user_messages(chat)

    create_poster(user1, user2, u1_messages, u2_messages)
