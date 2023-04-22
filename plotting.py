import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import matplotlib.dates as mdates
import seaborn as sns


def plot_messages_date(user1, user2, u1_datedict, u2_datedict):
    dict1_sorted = sorted(u1_datedict.items())
    dict2_sorted = sorted(u2_datedict.items())
    u1_dates, u1_counter = zip(*dict1_sorted)
    u2_dates, u2_counter = zip(*dict2_sorted)

    sns.set_theme()

    plt.xlabel("Date")
    plt.ylabel("Messages")
    plt.title("Messages per Day")
    plt.plot(u1_dates, u1_counter)
    plt.plot(u2_dates, u2_counter)
    plt.legend([user1, user2])

    plt.savefig("output/mess_per_date.png", dpi=350)
