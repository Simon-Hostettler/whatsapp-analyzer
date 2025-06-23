import re
import os
import datetime
import pandas as pd


def create_folders_if_missing():
    for folder in ["/output", "/chat_logs"]:
        if not os.path.exists(os.getcwd() + folder):
            os.makedirs(os.getcwd() + folder)


def get_datetime(message):
    date = list(map(int, (message.split(",")[0][1:]).split(".")))
    time = list(map(int, (message.split("]")[0].split(",")[1]).split(":")))
    return datetime.datetime(
        day=date[0],
        month=date[1],
        year=date[2],
        hour=time[0],
        minute=time[1],
        second=time[2],
    )


def parse_chat_to_dataframe(filename):
    with open("./chat_logs/" + filename, "r") as file:
        text = file.read()

    chat_lines = re.sub(r"\n(?!\[)", " ", text).split("\n")

    filtered = list(
        filter(
            lambda line: (
                "sticker omitted" not in line
                and "image omitted" not in line
                and "Missed voice call" not in line
                and line.strip() != ""
            ),
            chat_lines,
        )
    )

    user1 = filtered[0].split("] ", 1)[1].split(":", 1)[0]
    user2 = None
    for line in filtered:
        name = line.split("] ", 1)[1].split(":", 1)[0]
        if name != user1:
            user2 = name
            break

    # Extract data into records
    data = []
    for line in filtered:
        try:
            _, msg_part = line.split("] ", 1)
            username, message = msg_part.split(":", 1)
            dt = get_datetime(line)
            data.append(
                {
                    "datetime": dt,
                    "username": username.strip(),
                    "message": message.strip(),
                }
            )
        except ValueError:
            continue

    df = pd.DataFrame(data)
    df["datetime"] = pd.to_datetime(df["datetime"])
    return (user1, user2, df)
