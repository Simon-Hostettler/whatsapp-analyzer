import matplotlib, mplcairo
import matplotlib.pyplot as plt
import seaborn as sns
from loading import *
from text_analysis import *
from plotting import *
from plt_stylesheet import stylesheet


if __name__ == "__main__":
    # change backend to render emojis correctly
    matplotlib.use("module://mplcairo.macosx")

    plt.rcParams.update(stylesheet)

    # load chat
    chat = load_file("nora.txt")
    user1, user2, u1_messages, u2_messages = split_user_messages(chat)

    # plot most used emojis
    u1_emojicount = most_common_emojis(u1_messages, 10)
    u2_emojicount = most_common_emojis(u2_messages, 10)
    plot_most_common_emoji(user1, u1_emojicount)
    plot_most_common_emoji(user2, u2_emojicount)

    # plot pie chart of percentage of messages per user
    u1_mess_count = num_messages(u1_messages)
    u2_mess_count = num_messages(u2_messages)
    plot_message_percentage(user1, user2, u1_mess_count, u2_mess_count)

    # plot messages over time
    u1_datedict = messages_per_date(u1_messages)
    u2_datedict = messages_per_date(u2_messages)
    plot_messages_date(user1, user2, u1_datedict, u2_datedict)
    plot_messages_date_total(user1, user2, u1_datedict, u2_datedict)

    # plot most used words
    u1_wordcount = most_common_words(u1_messages)
    u2_wordcount = most_common_words(u2_messages)
    plot_most_common_words(user1, u1_wordcount)
    plot_most_common_words(user2, u2_wordcount)

    # plot messages per weekday
    u1_daycount = messages_per_weekday(u1_messages)
    u2_daycount = messages_per_weekday(u2_messages)
    plot_messages_weekday(user1, user2, u1_daycount, u2_daycount)

    # plot messages per month
    u1_monthcount = messages_per_month(u1_messages)
    u2_monthcount = messages_per_month(u2_messages)
    print(u1_monthcount)
    plot_messages_month(user1, user2, u1_monthcount, u2_monthcount)

    # plot pie chart of percentage of who sent first message
    count_dict = first_message_per_day(u1_messages, u2_messages)
    print(count_dict)
    plot_first_message_percentage(count_dict)
