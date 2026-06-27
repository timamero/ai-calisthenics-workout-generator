from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .core import config

app = FastAPI()

origins = []

if config.settings.environment == "local":
    origins.append(config.settings.local_origin)
    origins.append(config.settings.local_web_origin)
if config.settings.environment == "production":
    origins.append(config.settings.production_origin)
    origins.append(config.settings.production_web_origin)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
