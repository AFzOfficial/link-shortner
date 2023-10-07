from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from settings import settings
from database import config
from models import base


base.Base.metadata.create_all(bind=config.engine)


app = FastAPI(
    title=settings.APP_NAME,

    docs_url=None if settings.DEBUG == False else '/docs',
    redoc_url=None if settings.DEBUG == False else '/redoc',
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
