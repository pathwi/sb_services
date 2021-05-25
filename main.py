import fastapi
import uvicorn

from tagcloud import tagcloud_api

api = fastapi.FastAPI()

@api.get('/')
def index():
    return {
        "message": "Hello",
        "status": "OK"
    }

def configure():
    api.include_router(tagcloud_api.router)

configure()

if __name__ == '__main__':
    uvicorn.run(api)