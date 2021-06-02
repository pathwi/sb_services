import fastapi
import time
import logging
from fastapi_utils.tasks import repeat_every

from tagcloud import locobuzz, tagcloud, contentful, backgroud_image

logger = logging.getLogger(__name__)
router = fastapi.APIRouter()

# @router.get('/tagcloud')
@router.on_event("startup")
@repeat_every(seconds=3600, logger=logger, wait_first=True)
def get_tag_cloud():
    locobuzz.call_data_locobuzz()
    time.sleep(1)
    tagcloud.generate_tagcloud(425, 1230, 5, 65, 4.25, 12.3, "tagcloud-desktop")
    time.sleep(1)
    tagcloud.generate_tagcloud(270, 748, 1, 30, 2.7, 7.48, "tagcloud-mobile")
    time.sleep(2)
    backgroud_image.set_backgroud("tagcloud_frame_desktop", "tagcloud-desktop", 1230, 430, 25, 30, 27, 315, 485, "Spacebar-tagcloud-desktop")
    time.sleep(1)
    backgroud_image.set_backgroud("tagcloud_frame_mobile", "tagcloud-mobile", 748, 270, 10, 5, 16, 188, 292, "Spacebar-tagcloud-mobile")
    time.sleep(2)
    contentful.upload_image("Spacebar-tagcloud-desktop-", "Spacebar-tagcloud-desktop")
    time.sleep(1)
    contentful.upload_image("Spacebar-tagcloud-mobile-", "Spacebar-tagcloud-mobile")
    time.sleep(2)
    print("Tagcloud upload success")
    return {"Say": "Tagcloud"}