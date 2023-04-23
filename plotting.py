import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.font_manager import FontProperties
import matplotlib.dates as mdates
from collections import Counter

title_padding = 15
title_weight = "bold"
output_dpi = 350


def plot_messages_date(user1, user2, u1_datedict, u2_datedict):
    plt.clf()

    dict1_sorted = sorted(u1_datedict.items())
    dict2_sorted = sorted(u2_datedict.items())
    u1_dates, u1_counter = zip(*dict1_sorted)
    u2_dates, u2_counter = zip(*dict2_sorted)

    plt.title("Messages per Day", weight=title_weight, pad=title_padding)
    plt.plot(u1_dates, u1_counter)
    plt.plot(u2_dates, u2_counter)
    plt.legend([user1, user2])

    plt.savefig("output/mess_per_date.png", dpi=output_dpi)


def plot_messages_date_total(user1, user2, u1_datedict, u2_datedict):
    plt.clf()

    merged_dict = dict(Counter(u1_datedict) + Counter(u2_datedict))

    dict_sorted = sorted(merged_dict.items())
    dates, counter = zip(*dict_sorted)

    plt.title("Messages per Day", weight=title_weight, pad=title_padding)
    plt.plot(dates, counter)

    plt.savefig("output/mess_per_date_total.png", dpi=output_dpi)


def plot_most_common_words(user, wordcount):
    plt.clf()

    words, count = zip(*wordcount)
    xticks = range(len(words))

    plt.title(user + "'s most used words", weight=title_weight, pad=title_padding)
    plt.bar(xticks, count)
    plt.xticks(xticks, words)

    plt.savefig("output/" + user + "_mc_words.png", dpi=output_dpi)


def plot_most_common_emoji(user, emojicount):
    plt.clf()

    emojis, count = zip(*emojicount)
    xticks = range(len(emojis))

    plt.title(user + "'s most used emojis", weight=title_weight, pad=title_padding)
    plt.bar(xticks, count)

    prop = FontProperties(fname="/System/Library/Fonts/Apple Color Emoji.ttc", size=18)

    plt.xticks(xticks, emojis, fontproperties=prop)

    plt.savefig("output/" + user + "_mc_emoji.png", dpi=output_dpi)
