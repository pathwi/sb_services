import fastapi
import uvicorn

from tagcloud import tagcloud_api

app = fastapi.FastAPI()

@app.get('/')
def index():
    return {
        "message": "Hello",
        "status": "OK"
    }

def configure():
    app.include_router(tagcloud_api.router)

configure()

if __name__ == '__main__':
    uvicorn.run(app)