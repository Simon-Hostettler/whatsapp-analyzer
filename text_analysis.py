import collections
import datetime
import emoji
import string


def most_common_emojis(messages, n=5):
    # string containing only the emojis in the message
    def emojis_per_mess(message):
        return "".join(
            list(map(lambda dict: dict["emoji"][0], emoji.emoji_list(message)))
        )

    # string containing all emojis in the messages
    emojis = "".join(list(map(emojis_per_mess, messages)))
    return collections.Counter(emojis).most_common(n)


def most_common_words(messages, n=10):
    # remove metadata and punctuation, then split into words by whitespace
    words = sum(
        list(
            map(
                lambda mess: remove_punctuation(text_only(mess)).lower().split(" "),
                messages,
            )
        ),
        [],
    )

    # filter empty words
    drop_empty = list(filter(lambda s: s != "", words))
    return collections.Counter(drop_empty).most_common(n)


def remove_punctuation(message):
    return message.translate(str.maketrans("", "", string.punctuation))


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


def first_message_per_day(u1_messages, u2_messages):
    messages = u1_messages + u2_messages
    messages_by_day = {}
    for m in messages:
        date = get_date(m)
        if date not in messages_by_day.keys():
            messages_by_day[date] = [m]
        else:
            messages_by_day[date].append(m)
    messages_by_day = list(
        map(
            lambda ml: sorted(ml, key=(lambda x: get_time(x))),
            messages_by_day.values(),
        )
    )
    wrote_first = list(map(lambda ml: get_user(ml[0]), messages_by_day))
    return dict(collections.Counter(wrote_first))


def get_user(message):
    return (message.split("] ", 1)[1]).split(":", 1)[0]


def messages_per_date(messages):
    return dict(collections.Counter(list(map(get_date, messages))))


def messages_per_weekday(messages):
    day_dict = dict(
        collections.Counter(list(map(lambda mess: get_date(mess).weekday(), messages)))
    )
    # fill in missing days in dictionary
    day_dict = {i: 0 if i not in day_dict.keys() else day_dict[i] for i in range(0, 7)}
    return day_dict


def messages_per_month(messages):
    month_dict = dict(
        collections.Counter(list(map(lambda mess: get_date(mess).month - 1, messages)))
    )
    # fill in missing months in dictionary
    month_dict = {
        i: 0 if i not in month_dict.keys() else month_dict[i] for i in range(0, 12)
    }
    return month_dict
