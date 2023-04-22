from loading import *
from text_analysis import *
from plotting import *

if __name__ == "__main__":
    chat = load_file("nora.txt")
    user1, user2, u1_messages, u2_messages = split_user_messages(chat)
    print(most_common_emojis(u1_messages, 5))
    print(most_common_emojis(u2_messages, 5))
    print(user1, num_messages(u1_messages), avg_message_wc(u1_messages))
    print(user2, num_messages(u2_messages), avg_message_wc(u2_messages))
    print(get_date(u1_messages[0]))
    print(messages_per_date(u1_messages))
    u1_datedict = messages_per_date(u1_messages)
    u2_datedict = messages_per_date(u2_messages)
    plot_messages_date(user1, user2, u1_datedict, u2_datedict)
