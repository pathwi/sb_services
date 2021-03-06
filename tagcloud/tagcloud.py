import os
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np


def generate_tagcloud(heightGenerate, widthGenerate, minfont, maxfont, height, width, filename):
    this_file_path = os.path.abspath(__file__)
    BASE_DIR = os.path.dirname(this_file_path)
    ENTIRE_PROJECT_DIR = os.path.dirname(BASE_DIR)
    # Read json file
    with open(os.path.join(ENTIRE_PROJECT_DIR, "tag_word.json")) as tag:
        data = json.load(tag)

    if data['meta']['Status'] == "success":
        # Loop data to make word
        range_tag = {}
        for item in data['data']:
            read_word = str(item['Keyword']).encode('unicode-escape')
            replace_word = read_word.replace(b'\\u0e0d\\u0e39', b'\\uF70F\\u0E39')
            range_word = replace_word.decode('unicode-escape')
            range_tag[range_word] = item['Occurrences']

        # Set word color in Word cloud
        def random_color(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
            color_list = ["#ffffff", "#8ab168", "#a3d3d9", "#f0c648", "#f8555e"]
            return np.random.choice(color_list)

        # Generate word cloud with generate_from_frequencies
        wordcloud = WordCloud(
            font_path=os.path.join(ENTIRE_PROJECT_DIR, "font", "rsufont", "RSU_Regular.ttf"),
            regexp="[ก-๙a-zA-Z]+",
            prefer_horizontal=1,
            colormap='tab20c',
            relative_scaling=0.3,
            min_font_size=minfont,
            max_font_size=maxfont,
            background_color="#353F4C",
            width=widthGenerate,
            height=heightGenerate,
            max_words=50,
            scale=3,
            font_step=7,
            collocations=False,
            margin=30,
            color_func=random_color

        ).generate_from_frequencies(range_tag)

        # Generate word cloud to image
        plt.figure(figsize=(width, height), facecolor='#353F4C')
        plt.imshow(wordcloud)
        plt.axis('off')
        plt.tight_layout(pad=0)
        plt.savefig(os.path.join(ENTIRE_PROJECT_DIR, "images", filename + ".png"), dpi=100)

    else:
        print("Data from locobuzz is 0")
