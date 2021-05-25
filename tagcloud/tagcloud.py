import os
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np


def generate_tagcloud():
    # Read json file
    with open(os.path.expanduser('~/project_spacebar/sb_integrations/tag_word.json')) as tag:
        data = json.load(tag)

    if data['data'] is not None:
        # Loop data to make word
        range_tag = {}
        for item in data['data']:
            range_tag[item['Keyword']] = item['Occurences']

        # Set word color in Word cloud
        def random_color(word=None, font_size=None, position=None, orientation=None, font_path=None, random_state=None):
            color_list = ["#ffffff", "#8ab168", "#a3d3d9", "#f0c648", "#f8555e"]
            return np.random.choice(color_list)

        # Generate word cloud with generate_from_frequencies
        wordcloud = WordCloud(
            font_path=os.path.expanduser('~/project_spacebar/sb_integrations/font/Kanit/Kanit-Light.ttf'),
            regexp="[ก-๙a-zA-Z]+",
            prefer_horizontal=1,
            colormap='tab20c',
            relative_scaling=0.3,
            min_font_size=1.5,
            background_color="#353F4C",
            width=1230,
            height=425,
            max_words=20,
            scale=3,
            font_step=11,
            collocations=False,
            margin=2,
            color_func=random_color

        ).generate_from_frequencies(range_tag)

        # Generate word cloud to image
        plt.figure(figsize=(12.3, 4.25), facecolor='#353F4C')
        plt.imshow(wordcloud)
        plt.axis('off')
        plt.tight_layout(pad=0)
        plt.savefig(os.path.expanduser('~/project_spacebar/sb_integrations/images/' + 'tagcloud.png'), dpi=100)