import re
import os


def create_folders_if_missing():
    for folder in ["/output", "/chat_logs"]:
        if not os.path.exists(os.getcwd() + folder):
            os.makedirs(os.getcwd() + folder)


def load_file(filename):
    with open("./chat_logs/" + filename, "r") as file:
        text = file.read()
        # replace newlines in messages
        chat = re.sub("\n[^\[]", " ", text).split("\n")
        # remove sticker, image, voice call and empty messages
        filter_stickers = list(filter(lambda line: "sticker omitted" not in line, chat))
        filter_images = list(
            filter(lambda line: "image omitted" not in line, filter_stickers)
        )
        filter_vc = list(filter(lambda line: "Missed voice call" not in line, chat))
        filter_empty = list(filter(lambda line: line != "", filter_vc))
        return filter_empty


def split_user_messages(chat):
    user1 = (chat[0].split("] ", 1)[1]).split(":", 1)[0]
    user1_messages = list(filter(lambda line: ("] " + user1 + ":") in line, chat))
    user2_messages = list(filter(lambda line: ("] " + user1 + ":") not in line, chat))
    user2 = (user2_messages[0].split("] ", 1)[1]).split(":", 1)[0]
    return (user1, user2, user1_messages, user2_messages)
