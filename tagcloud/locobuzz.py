import requests
import json
import os
import datetime


def call_data_locobuzz():
    # URL LocoBuzz data
    url_locobuzz = "https://socialtest.locobuzz.com/Social/GetTagCloudData"

    # Header
    headers_token = "4BB74979-D528-41AB-8B50-3D48639B5D6F"

    # Set body
    sdate = int(datetime.datetime.now().strftime('%s')) - 10800
    edate = datetime.datetime.now().strftime('%s')
    BrandId = 600
    Nextpagetoken = ""
    KeywordType = "keyword"     # optional - supports  keyword or emoji

    header = {
        "auth-token": headers_token,
        "Content-Type": "application/json"
    }

    body = {
        "sdate": sdate,
        "edate": edate,
        "BrandId": BrandId,
        "Nextpagetoken": Nextpagetoken,
        "KeywordType": KeywordType
    }

    result = requests.post(url_locobuzz, data = json.dumps(body), headers = header)

    this_file_path = os.path.abspath(__file__)
    BASE_DIR = os.path.dirname(this_file_path)
    ENTIRE_PROJECT_DIR = os.path.dirname(BASE_DIR)

    # Write result to file
    with open(os.path.join(ENTIRE_PROJECT_DIR, "tag_word.json"), "w") as outfile:
        json.dump(result.json(), outfile)