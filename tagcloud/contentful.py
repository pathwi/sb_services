import requests
import json
import os
import datetime


def upload_image(filename, image_upload):
    this_file_path = os.path.abspath(__file__)
    BASE_DIR = os.path.dirname(this_file_path)
    ENTIRE_PROJECT_DIR = os.path.dirname(BASE_DIR)

    time_tagcloud = datetime.datetime.now()
    time_image = filename + str(time_tagcloud.strftime("%Y-%m-%dT%H%M%S%f")[:-3] + "Z")
    file_image_name = time_image + ".png"

    spaceId = "e7ee8kzf5re6"
    environmentId = "master"
    cma_token = "CFPAT-DTNsQqLMS0flsOmUKPsVrZIkwPfC_2jCkpXA9cV9cfw"

    url_upload = "https://upload.contentful.com/spaces/" + spaceId + "/uploads"
    header_upload = {
        "Content-Type": "application/octet-stream",
        "Authorization": "Bearer " + cma_token
    }
    body_upload = open(os.path.join(ENTIRE_PROJECT_DIR, "images", image_upload + ".png"), 'rb').read()

    request_upload = requests.post(url_upload, data=body_upload, headers=header_upload)
    response_upload = request_upload.json()


    url_create = "https://api.contentful.com/spaces/"+ spaceId + "/environments/" + environmentId + "/assets"
    herder_content_create = "application/vnd.contentful.management.v1+json"
    herder_create = {
        "Content-Type": herder_content_create,
        "Authorization": "Bearer " + cma_token
    }
    id_create = response_upload["sys"]["id"]
    body_create = {
      "fields": {
          "title": {
              "en-US": time_image
          },
          "file": {
              "en-US": {
                  "contentType": "image/png",
                  "fileName": file_image_name,
                  "uploadFrom": {
                      "sys": {
                        "type": "Link",
                        "linkType": "Upload",
                        "id": id_create
                      }
                  }
              }
          }
      }
    }

    request_crate = requests.post(url_create, data=json.dumps(body_create), headers=herder_create)
    response_create = request_crate.json()


    id_process = response_create["sys"]["id"]
    url_process = "https://api.contentful.com/spaces/" + spaceId + "/environments/" + environmentId + "/assets/" + id_process + "/files/en-US/process"
    herder_process = {
        "X-Contentful-Version": "",
        "Authorization": "Bearer " + cma_token
    }
    request_process = requests.put(url_process, headers=herder_process)


    url_publish = "https://api.contentful.com/spaces/" + spaceId + "/environments/" + environmentId + "/assets/" + id_process + "/published"
    asset_version = "2"
    herder_publish = {
        "X-Contentful-Version": asset_version,
        "Authorization": "Bearer " + cma_token
    }
    request_publish = requests.put(url_publish, headers=herder_publish)
