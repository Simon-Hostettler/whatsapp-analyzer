import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.font_manager import FontProperties
import matplotlib.dates as mdates
from collections import Counter
import numpy as np

title_padding = 15
title_weight = "bold"
output_dpi = 350
date_form = DateFormatter("%y-%m")


def plot_messages_date(user1, user2, u1_datedict, u2_datedict):
    plt.clf()

    dict1_sorted = sorted(u1_datedict.items())
    dict2_sorted = sorted(u2_datedict.items())
    u1_dates, u1_counter = zip(*dict1_sorted)
    u2_dates, u2_counter = zip(*dict2_sorted)

    plt.plot(u1_dates, u1_counter)
    plt.plot(u2_dates, u2_counter)
    plt.gca().xaxis.set_major_formatter(date_form)

    plt.savefig("output/mess_per_date.png", dpi=output_dpi)


def plot_messages_date_total(user1, user2, u1_datedict, u2_datedict):
    plt.clf()

    merged_dict = dict(Counter(u1_datedict) + Counter(u2_datedict))
    dict_sorted = sorted(merged_dict.items())
    dates, counter = zip(*dict_sorted)

    plt.plot(dates, counter)
    plt.gca().xaxis.set_major_formatter(date_form)

    plt.savefig("output/mess_per_date_total.png", dpi=output_dpi)


def plot_message_percentage(user1, user2, u1count, u2count):
    plt.clf()

    fig, ax = plt.subplots()
    ax.pie([u1count, u2count], labels=None, autopct="%1.1f%%")

    plt.savefig("output/mpu_pie_chart", dpi=output_dpi)


def plot_first_message_percentage(count_dict):
    plt.clf()

    fig, ax = plt.subplots()
    users = count_dict.keys()
    count = count_dict.values()
    ax.pie(count, labels=None, autopct="%1.1f%%")

    plt.savefig("output/fm_pie_chart", dpi=output_dpi)


def plot_messages_hour(user1, user2, hourcount1, hourcount2):
    plt.clf()

    hourcount1[24] = hourcount1[0]
    hourcount2[24] = hourcount2[0]
    hourcount1 = sorted(hourcount1.items())
    hourcount2 = sorted(hourcount2.items())
    _, count1 = zip(*hourcount1)
    _, count2 = zip(*hourcount2)

    norm_hours = list(map(lambda d: -(d / 24.0 * 2.0 * np.pi), range(0, 25)))

    fig, ax = plt.subplots(subplot_kw={"projection": "polar"})

    ax.plot(norm_hours, count1)
    ax.fill_between(norm_hours, count1, label="_nolegend_")
    ax.plot(norm_hours, count2)
    ax.fill_between(norm_hours, count2, label="_nolegend_")
    ax.set_xticks(norm_hours, list(map(lambda h: str(h) + ":00", range(0, 24))) + [""])
    ax.tick_params(axis="x", pad=20)
    ax.set_rticks([])
    ax.set_axisbelow(False)

    plt.tight_layout()

    plt.savefig("output/messages_hour", dpi=output_dpi)


def plot_messages_weekday(user1, user2, daycount1, daycount2):
    plt.clf()

    daycount1[7] = daycount1[0]
    daycount2[7] = daycount2[0]
    daycount1 = sorted(daycount1.items())
    daycount2 = sorted(daycount2.items())
    _, count1 = zip(*daycount1)
    _, count2 = zip(*daycount2)

    norm_days = list(map(lambda d: -(d / 7.0 * 2.0 * np.pi), range(0, 8)))

    fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
    ax.plot(norm_days, count1)
    ax.fill_between(norm_days, count1, label="_nolegend_")
    ax.plot(norm_days, count2)
    ax.fill_between(norm_days, count2, label="_nolegend_")
    ax.set_xticks(
        norm_days,
        [
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
            "",
        ],
    )
    ax.tick_params(axis="x", pad=20)
    ax.set_rticks([])
    ax.set_axisbelow(False)

    plt.tight_layout()

    plt.savefig("output/messages_weekday", dpi=output_dpi)


def plot_messages_month(user1, user2, monthcount1, monthcount2):
    plt.clf()

    monthcount1[12] = monthcount1[0]
    monthcount2[12] = monthcount2[0]
    monthcount1 = sorted(monthcount1.items())
    monthcount2 = sorted(monthcount2.items())
    _, count1 = zip(*monthcount1)
    _, count2 = zip(*monthcount2)

    norm_months = list(map(lambda d: -(d / 12.0 * 2.0 * np.pi), range(0, 13)))

    fig, ax = plt.subplots(subplot_kw={"projection": "polar"})
    ax.plot(norm_months, count1)
    ax.fill_between(norm_months, count1, label="_nolegend_")
    ax.plot(norm_months, count2)
    ax.fill_between(norm_months, count2, label="_nolegend_")
    ax.set_xticks(
        norm_months,
        [
            "January",
            "February",
            "March",
            "April",
            "May",
            "June",
            "July",
            "August",
            "September",
            "October",
            "November",
            "December",
            "",
        ],
    )
    ax.tick_params(axis="x", pad=20)
    ax.set_rticks([])
    ax.set_axisbelow(False)

    plt.tight_layout()

    plt.savefig("output/messages_month", dpi=output_dpi)


def plot_most_common_words(user, wordcount, color):
    plt.clf()

    words, count = zip(*wordcount)
    xticks = range(len(words))
    prop = FontProperties(size=11)

    plt.bar(xticks, count, color=color)
    plt.xticks(xticks, words, fontproperties=prop)

    plt.savefig("output/" + user + "_mc_words.png", dpi=output_dpi)


def plot_most_common_emoji(user, emojicount, color):
    plt.clf()

    emojis, count = zip(*emojicount)
    xticks = range(len(emojis))
    prop = FontProperties(fname="/System/Library/Fonts/Apple Color Emoji.ttc", size=25)

    plt.bar(xticks, count, color=color)
    plt.xticks(xticks, emojis, fontproperties=prop)

    plt.savefig("output/" + user + "_mc_emoji.png", dpi=output_dpi)
