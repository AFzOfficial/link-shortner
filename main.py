from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from settings import settings
from database import config
from routers import link, redirect
from models import base


base.Base.metadata.create_all(bind=config.engine)


app = FastAPI(
    title=settings.APP_NAME,

    docs_url=None if settings.DEBUG == False else '/admin/docs',
    redoc_url=None if settings.DEBUG == False else '/admin/redoc',
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(link.router, prefix=f"/{settings.API_PREFIX}", tags=["Links"])
app.include_router(redirect.router, prefix=f"", tags=["Redirect"])
