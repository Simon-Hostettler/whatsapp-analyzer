from PIL import Image, ImageDraw, ImageFont
from plotting import *
from text_analysis import *

title_font = ImageFont.truetype("fonts/helvetica.ttf", size=200)
subtitle_font = ImageFont.truetype("fonts/helvetica.ttf", size=80)
info_font = ImageFont.truetype("fonts/helvetica.ttf", size=50)


# resolution of poster
width = 2560
height = 5760

# text padding on sides
side_padding = 400

# scaled resolution of plots
x_scale = 1000
y_scale = 750
scaled_res = (x_scale, y_scale)

# distance between titles / plots
y_offset = 100

# x axis offsets of plots
img_offs_left = (width - 2 * x_scale) // 2
img_offs_right = int(1.5 * img_offs_left) + x_scale


def create_poster(user1, user2, u1_messages, u2_messages):
    prepare_figs(user1, user2, u1_messages, u2_messages)

    poster = Image.new("RGB", (width, height), color="#2e2e36")
    pdraw = ImageDraw.Draw(poster)

    cur_y = 250

    # draw name title
    cur_y = draw_title(pdraw, user1, user2, cur_y)

    # draw total messages information
    mpu1 = len(u1_messages)
    mpu2 = len(u2_messages)

    cur_y = draw_2_texts(
        pdraw, f"Total messages: {mpu1}", f"Total messages: {mpu2}", cur_y
    )

    # draw average message length information
    avgl1 = avg_message_wc(u1_messages)
    avgl2 = avg_message_wc(u2_messages)

    cur_y = draw_2_texts(
        pdraw,
        "Avg message length: {:.1f}".format(avgl1),
        "Avg message length: {:.1f}".format(avgl2),
        cur_y,
    )

    # draw most used emojis and words (2 rows)
    cur_y = draw_2_figs_1_title(
        poster,
        pdraw,
        "Most used emoji",
        f"output/{user1}_mc_emoji.png",
        f"output/{user2}_mc_emoji.png",
        cur_y,
    )

    cur_y = draw_2_figs_1_title(
        poster,
        pdraw,
        "Most used words",
        f"output/{user1}_mc_words.png",
        f"output/{user2}_mc_words.png",
        cur_y,
    )

    # draw messages over time and per hour (1 row)
    cur_y = draw_2_figs_2_titles(
        poster,
        pdraw,
        "Messages over time",
        "Messages per hour",
        "output/mess_per_date_total.png",
        "output/messages_hour.png",
        cur_y,
    )

    # draw messages per weekday and month (1 row)
    cur_y = draw_2_figs_2_titles(
        poster,
        pdraw,
        "Messages per weekday",
        "Messages per month",
        "output/messages_weekday.png",
        "output/messages_month.png",
        cur_y,
    )

    # draw percentage of texts and first message percentage (1 row)
    cur_y = draw_2_figs_2_titles(
        poster,
        pdraw,
        "Percentage of texts",
        "Who writes first",
        "output/fm_pie_chart.png",
        "output/mpu_pie_chart.png",
        cur_y,
    )

    poster.save("output/poster_" + user1 + "_" + user2 + ".pdf", quality=100)


def prepare_figs(user1, user2, u1_messages, u2_messages):
    # plot most used emojis
    u1_emojicount = most_common_emojis(u1_messages, 10)
    u2_emojicount = most_common_emojis(u2_messages, 10)
    plot_most_common_emoji(user1, u1_emojicount, color="#8dd3c7")
    plot_most_common_emoji(user2, u2_emojicount, color="#f59356")

    # plot pie chart of percentage of messages per user
    u1_mess_count = num_messages(u1_messages)
    u2_mess_count = num_messages(u2_messages)
    plot_message_percentage(user1, user2, u1_mess_count, u2_mess_count)

    # plot messages over time
    u1_datedict = messages_per_date(u1_messages)
    u2_datedict = messages_per_date(u2_messages)
    plot_messages_date(user1, user2, u1_datedict, u2_datedict)
    plot_messages_date_total(user1, user2, u1_datedict, u2_datedict)

    # plot most used words
    u1_wordcount = most_common_words(u1_messages)
    u2_wordcount = most_common_words(u2_messages)
    plot_most_common_words(user1, u1_wordcount, color="#8dd3c7")
    plot_most_common_words(user2, u2_wordcount, color="#f59356")

    # plot messages per weekday
    u1_daycount = messages_per_weekday(u1_messages)
    u2_daycount = messages_per_weekday(u2_messages)
    plot_messages_weekday(user1, user2, u1_daycount, u2_daycount)

    # plot messages per month
    u1_monthcount = messages_per_month(u1_messages)
    u2_monthcount = messages_per_month(u2_messages)
    print(u1_monthcount)
    plot_messages_month(user1, user2, u1_monthcount, u2_monthcount)

    # plot pie chart of percentage of who sent first message
    count_dict = first_message_per_day(u1_messages, u2_messages)
    print(count_dict)
    plot_first_message_percentage(count_dict)

    # plot messages per hour
    u1_hourcount = messages_per_hour(u1_messages)
    u2_hourcount = messages_per_hour(u2_messages)
    plot_messages_hour(user1, user2, u1_hourcount, u2_hourcount)


def draw_2_figs_1_title(poster, pdraw, title, fig1_path, fig2_path, cur_y):
    pdraw.text(
        (
            width / 2 - pdraw.textlength(text=title, font=subtitle_font) / 2,
            cur_y,
        ),
        font=subtitle_font,
        text=title,
        stroke_width=2,
    )

    fig1 = Image.open(fig1_path)
    fig1.thumbnail(scaled_res, Image.ANTIALIAS)
    fig2 = Image.open(fig2_path)
    fig2.thumbnail(scaled_res, Image.ANTIALIAS)

    cur_y += y_offset

    poster.paste(fig1, (img_offs_left, cur_y))
    poster.paste(fig2, (img_offs_right, cur_y))

    cur_y += y_scale + y_offset

    return cur_y


def draw_2_figs_2_titles(poster, pdraw, title1, title2, fig1_path, fig2_path, cur_y):
    pdraw.text(
        (side_padding, cur_y),
        font=subtitle_font,
        text=title1,
        stroke_width=2,
    )

    pdraw.text(
        (
            text_offset_right(pdraw, title2, subtitle_font),
            cur_y,
        ),
        font=subtitle_font,
        text=title2,
        stroke_width=2,
    )

    cur_y += y_offset

    fig1 = Image.open(fig1_path)
    fig1.thumbnail(scaled_res, Image.ANTIALIAS)
    fig2 = Image.open(fig2_path)
    fig2.thumbnail(scaled_res, Image.ANTIALIAS)

    poster.paste(fig1, (img_offs_left, cur_y))
    poster.paste(fig2, (img_offs_right, cur_y))

    cur_y += y_scale + y_offset

    return cur_y


def draw_2_texts(pdraw, text1, text2, cur_y):
    pdraw.text(
        (side_padding, cur_y),
        font=info_font,
        stroke_width=2,
        text=text1,
    )
    pdraw.text(
        (
            text_offset_right(pdraw, text2, info_font),
            cur_y,
        ),
        font=info_font,
        stroke_width=2,
        text=text2,
    )

    cur_y += int(1.5 * y_offset)

    return cur_y


def draw_title(pdraw, name1, name2, cur_y):
    pdraw.text(
        (side_padding, cur_y),
        font=title_font,
        fill="#8dd3c7",
        text=name1,
        stroke_width=4,
    )
    pdraw.text(
        (
            text_offset_right(pdraw, name2, title_font),
            cur_y,
        ),
        font=title_font,
        fill="#f59356",
        text=name2,
        stroke_width=4,
    )

    cur_y += 3 * y_offset

    return cur_y


def text_offset_right(pdraw, text, font):
    return width - side_padding - pdraw.textlength(text=text, font=font)
