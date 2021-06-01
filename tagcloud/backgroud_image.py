import datetime
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os


def set_backgroud(image_f, image_t, width_thumbnail, height_thumbnail, width_paste, height_paste, font_size, text_width, text_height, image_out):
    this_file_path = os.path.abspath(__file__)
    BASE_DIR = os.path.dirname(this_file_path)
    ENTIRE_PROJECT_DIR = os.path.dirname(BASE_DIR)

    image_frame = Image.open(os.path.join(ENTIRE_PROJECT_DIR, "images", image_f + ".png"))
    image_tagcloud = Image.open(os.path.join(ENTIRE_PROJECT_DIR, "images", image_t + ".png"))
    image_tagcloud.thumbnail((width_thumbnail, height_thumbnail), Image.ANTIALIAS)
    # Input image
    image_output = image_frame.copy()
    image_output.paste(image_tagcloud, (width_paste, height_paste), image_tagcloud)
    # Input font
    font = ImageFont.truetype(os.path.join(ENTIRE_PROJECT_DIR, "font", "Poppins", "Poppins-ExtraLight.ttf"), font_size)
    time_capture = datetime.datetime.now()
    time_capture_str = str(time_capture.strftime("%B %d, %Y   |   %H:%M %p")).replace(' AM', ' am').replace(' PM', ' pm')
    draw = ImageDraw.Draw(image_output)
    draw.text((text_width, text_height), time_capture_str, font=font, fill=(53, 63, 76))
    image_output.save(os.path.join(ENTIRE_PROJECT_DIR, "images", image_out + ".png"), quality=100)