import collections
import datetime
import emoji


def most_common_emojis(messages, n=5):
    def emojis_per_mess(message):
        return "".join(
            list(map(lambda dict: dict["emoji"][0], emoji.emoji_list(message)))
        )

    emojis = "".join(list(map(emojis_per_mess, messages)))
    return collections.Counter(emojis).most_common(n)


def num_messages(messages):
    return len(messages)


def avg_message_wc(messages):
    return sum(map(lambda mess: len(text_only(mess).split(" ")) - 1, messages)) / len(
        messages
    )


def text_only(message):
    return message.split(":")[3]


def get_datetime(message):
    date = list(map(int, (message.split(",")[0][1:]).split(".")))
    time = list(map(int, (message.split("]")[0].split(",")[1]).split(":")))
    return datetime.datetime(
        day=date[0],
        month=date[1],
        year=date[2] + 2000,
        hour=time[0],
        minute=time[1],
        second=time[2],
    )


def get_date(message):
    date = list(map(int, (message.split(",")[0][1:]).split(".")))
    return datetime.date(day=date[0], month=date[1], year=date[2] + 2000)


def get_time(message):
    time = list(map(int, (message.split("]")[0].split(",")[1]).split(":")))
    return datetime.time(hour=time[0], minute=time[1], second=time[2])


def messages_per_date(messages):
    return dict(collections.Counter(list(map(get_date, messages))))
