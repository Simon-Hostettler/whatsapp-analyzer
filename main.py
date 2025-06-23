import matplotlib, mplcairo
import matplotlib.pyplot as plt
import seaborn as sns
from src.loading import *
from src.poster import *
from src.plt_stylesheet import stylesheet
from platform import system


def main():
    # change backend to render emojis correctly
    if system().lower() == "darwin":
        matplotlib.use("module://mplcairo.macosx")

    plt.rcParams.update(stylesheet)

    create_folders_if_missing()

    user1, user2, data = parse_chat_to_dataframe("xxx")

    create_poster(user1, user2, data)


if __name__ == "__main__":
    main()
