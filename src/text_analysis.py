import collections
import datetime
import emoji
import string
from itertools import chain


def remove_punctuation(message):
    return message.translate(str.maketrans("", "", string.punctuation))


def most_common_emojis(df, n=5):
    def emojis_per_message(text):
        return "".join(map(lambda d: d["emoji"][0], emoji.emoji_list(text)))

    all_emojis = "".join(df["message"].apply(emojis_per_message).tolist())
    return collections.Counter(all_emojis).most_common(n)


def most_common_words(df, n=10):
    clean_messages = (
        df["message"]
        .str.lower()
        .str.translate(str.maketrans("", "", string.punctuation))
    )
    words_series = clean_messages.str.split()
    all_words = list(chain.from_iterable(words_series))
    filtered_words = [w for w in all_words if w]

    return collections.Counter(filtered_words).most_common(n)


def num_messages(df):
    return len(df)


def avg_message_wc(df):
    def word_count(text):
        return len(text.split())

    return df["message"].apply(word_count).mean()


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
    return datetime.date(day=date[0], month=date[1], year=date[2])


def get_time(message):
    time = list(map(int, (message.split("]")[0].split(",")[1]).split(":")))
    return datetime.time(hour=time[0], minute=time[1], second=time[2])


def get_hour(message):
    return list(map(int, (message.split("]")[0].split(",")[1]).split(":")))[0]


def first_message_per_day(df):

    df["date"] = df["datetime"].dt.date
    df_sorted = df.sort_values(by="datetime")

    first_per_day = df_sorted.groupby("date").first().reset_index()

    first_user_counts = collections.Counter(first_per_day["username"])

    return dict(first_user_counts)


def messages_per_date(df):
    df["date"] = df["datetime"].dt.date

    date_counts = df["date"].value_counts().sort_index()

    return date_counts.to_dict()


def messages_per_hour(df):
    df["hour"] = df["datetime"].dt.hour

    message_counts = df["hour"].value_counts().sort_index()

    hour_dict = {hour: 0 for hour in range(24)}
    hour_dict.update(message_counts.to_dict())

    return hour_dict


def messages_per_weekday(df):
    df["weekday"] = df["datetime"].dt.weekday

    message_counts = df["weekday"].value_counts().sort_index()

    week_dict = {day: 0 for day in range(7)}
    week_dict.update(message_counts.to_dict())

    return week_dict


def messages_per_month(df):
    df["month"] = df["datetime"].dt.month - 1

    message_counts = df["month"].value_counts().sort_index()

    month_dict = {month: 0 for month in range(0, 12)}
    month_dict.update(message_counts.to_dict())

    return month_dict
