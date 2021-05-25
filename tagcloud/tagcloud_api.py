import fastapi
import time

from tagcloud import locobuzz, tagcloud, contentful

router = fastapi.APIRouter()

@router.get('/tagcloud')
def get_tag_cloud():
    locobuzz.call_data_locobuzz()
    time.sleep(1)
    tagcloud.generate_tagcloud()
    time.sleep(2)
    contentful.upload_image()
    time.sleep(3)
    return {"Say": "Tagcloud" }