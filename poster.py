from PIL import Image, ImageDraw, ImageFont
from plotting import *
from text_analysis import *

title_font = ImageFont.truetype("fonts/helvetica.ttf", size=200)
subtitle_font = ImageFont.truetype("fonts/helvetica.ttf", size=80)
info_font = ImageFont.truetype("fonts/helvetica.ttf", size=50)

width = 2560
height = 5760

side_padding = 400

x_scale = 1000
y_scale = 750

scaled_res = (x_scale, y_scale)

y_offset = 100

img_offs_left = (width - 2 * x_scale) // 2
img_offs_right = int(1.5 * img_offs_left) + x_scale


def create_poster(user1, user2, u1_messages, u2_messages):
    prepare_figs(user1, user2, u1_messages, u2_messages)

    poster = Image.new("RGB", (width, height), color="#2e2e36")
    pdraw = ImageDraw.Draw(poster)

    cur_y = 250

    # draw name title
    pdraw.text(
        (side_padding, cur_y),
        font=title_font,
        fill="#8dd3c7",
        text=user1,
        stroke_width=4,
    )
    pdraw.text(
        (
            width
            - side_padding
            - pdraw.textlength(
                text=user2,
                font=title_font,
            ),
            cur_y,
        ),
        font=title_font,
        fill="#f59356",
        text=user2,
        stroke_width=4,
    )

    cur_y += 3 * y_offset
    # draw total messages information
    mpu1 = len(u1_messages)
    mpu2 = len(u2_messages)

    pdraw.text(
        (side_padding, cur_y),
        font=info_font,
        stroke_width=2,
        text=f"Total messages: {mpu1}",
    )
    pdraw.text(
        (
            width
            - side_padding
            - pdraw.textlength(text=f"Total messages: {mpu2}", font=info_font),
            cur_y,
        ),
        font=info_font,
        stroke_width=2,
        text=f"Total messages: {mpu2}",
    )

    cur_y += int(1.5 * y_offset)
    # draw average message length information
    avgl1 = avg_message_wc(u1_messages)
    avgl2 = avg_message_wc(u2_messages)

    pdraw.text(
        (side_padding, cur_y),
        font=info_font,
        stroke_width=2,
        text="Avg message length: {:.1f}".format(avgl1),
    )
    pdraw.text(
        (
            width
            - side_padding
            - pdraw.textlength(
                text="Avg message length: {:.1f}".format(avgl2), font=info_font
            ),
            cur_y,
        ),
        font=info_font,
        stroke_width=2,
        text="Avg message length: {:.1f}".format(avgl2),
    )

    cur_y += int(1.5 * y_offset)
    # draw most used emojis and words (2 rows)
    pdraw.text(
        (
            width / 2
            - pdraw.textlength(text="Most used emoji", font=subtitle_font) / 2,
            cur_y,
        ),
        font=subtitle_font,
        text="Most used emoji",
        stroke_width=2,
    )

    u1_mce = Image.open(f"output/{user1}_mc_emoji.png")
    u1_mce.thumbnail(scaled_res, Image.ANTIALIAS)
    u2_mce = Image.open(f"output/{user2}_mc_emoji.png")
    u2_mce.thumbnail(scaled_res, Image.ANTIALIAS)

    cur_y += y_offset

    poster.paste(u1_mce, (img_offs_left, cur_y))
    poster.paste(u2_mce, (img_offs_right, cur_y))

    cur_y += y_scale + y_offset

    pdraw.text(
        (
            width / 2
            - pdraw.textlength(text="Most used words", font=subtitle_font) / 2,
            cur_y,
        ),
        font=subtitle_font,
        text="Most used words",
        stroke_width=2,
    )

    cur_y += y_offset

    u1_mcw = Image.open(f"output/{user1}_mc_words.png")
    u1_mcw.thumbnail(scaled_res, Image.ANTIALIAS)
    u2_mcw = Image.open(f"output/{user2}_mc_words.png")
    u2_mcw.thumbnail(scaled_res, Image.ANTIALIAS)

    poster.paste(u1_mcw, (img_offs_left, cur_y))
    poster.paste(u2_mcw, (img_offs_right, cur_y))

    cur_y += y_scale + y_offset
    # draw messages over time and per hour (1 row)
    pdraw.text(
        (side_padding, cur_y),
        font=subtitle_font,
        text="Messages over time",
        stroke_width=2,
    )

    pdraw.text(
        (
            width
            - side_padding
            - pdraw.textlength(text="Messages per hour", font=subtitle_font),
            cur_y,
        ),
        font=subtitle_font,
        text="Messages per hour",
        stroke_width=2,
    )

    cur_y += y_offset

    mot = Image.open(f"output/mess_per_date_total.png")
    mot.thumbnail(scaled_res, Image.ANTIALIAS)
    mph = Image.open(f"output/messages_hour.png")
    mph.thumbnail(scaled_res, Image.ANTIALIAS)

    poster.paste(mot, (img_offs_left, cur_y))
    poster.paste(mph, (img_offs_right, cur_y))

    cur_y += y_scale + y_offset

    # draw messages per weekday and month (1 row)
    pdraw.text(
        (side_padding, cur_y),
        font=subtitle_font,
        text="Messages per weekday",
        stroke_width=2,
    )

    pdraw.text(
        (
            width
            - side_padding
            - pdraw.textlength(text="Messages per month", font=subtitle_font),
            cur_y,
        ),
        font=subtitle_font,
        text="Messages per month",
        stroke_width=2,
    )

    cur_y += y_offset

    mpw = Image.open(f"output/messages_weekday.png")
    mpw.thumbnail(scaled_res, Image.ANTIALIAS)
    mpm = Image.open(f"output/messages_month.png")
    mpm.thumbnail(scaled_res, Image.ANTIALIAS)

    poster.paste(mpw, (img_offs_left, cur_y))
    poster.paste(mpm, (img_offs_right, cur_y))

    cur_y += y_scale + y_offset

    # draw percentage of texts and first message percentage (1 row)
    pdraw.text(
        (side_padding, cur_y),
        font=subtitle_font,
        text="Percentage of texts",
        stroke_width=2,
    )

    pdraw.text(
        (
            width
            - side_padding
            - pdraw.textlength(text="Who writes first", font=subtitle_font),
            cur_y,
        ),
        font=subtitle_font,
        text="Who writes first",
        stroke_width=2,
    )

    fmp = Image.open(f"output/fm_pie_chart.png")
    fmp.thumbnail(scaled_res, Image.ANTIALIAS)
    mpu = Image.open(f"output/mpu_pie_chart.png")
    mpu.thumbnail(scaled_res, Image.ANTIALIAS)

    cur_y += y_offset
    poster.paste(mpu, (img_offs_left, cur_y))
    poster.paste(fmp, (img_offs_right, cur_y))

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
