# main.py

from fastapi import FastAPI
from api.search import router as search_router
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="Web Automation API",
    description="API para disparar la automatización Selenium",
    version="0.1.0"
)

# Monta 'downloads/' en /downloads
app.mount(
    "/downloads",
    StaticFiles(directory="downloads"),
    name="downloads"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluye los endpoints definidos en api/search.py
app.include_router(search_router)
