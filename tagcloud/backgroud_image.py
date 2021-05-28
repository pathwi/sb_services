import datetime
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os


def set_backgroud():
    this_file_path = os.path.abspath(__file__)
    BASE_DIR = os.path.dirname(this_file_path)
    ENTIRE_PROJECT_DIR = os.path.dirname(BASE_DIR)

    image_frame = Image.open(os.path.join(ENTIRE_PROJECT_DIR, "images", "tagcloud_frame.png"))
    image_tagcloud = Image.open(os.path.join(ENTIRE_PROJECT_DIR, "images", "tagcloud.png"))
    image_tagcloud.thumbnail((1230,430), Image.ANTIALIAS)
    # Input image
    image_output = image_frame.copy()
    image_output.paste(image_tagcloud, (25, 30), image_tagcloud)
    # Input font
    font = ImageFont.truetype(os.path.join(ENTIRE_PROJECT_DIR, "font", "Poppins", "Poppins-ExtraLight.ttf"), 27)
    time_capture = datetime.datetime.now()
    time_capture_str = str(time_capture.strftime("%B %d, %Y   |   %H:%M %p")).replace(' AM', ' am').replace(' PM', ' pm')
    draw = ImageDraw.Draw(image_output)
    draw.text((315, 485), time_capture_str, font=font, fill=(53, 63, 76))
    image_output.save(os.path.join(ENTIRE_PROJECT_DIR, "images", "Spacebar-tagcloud-desktop.png"), quality=100)