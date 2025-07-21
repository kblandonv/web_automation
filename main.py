# main.py

from fastapi import FastAPI
from api.search import router as search_router

app = FastAPI(
    title="Web Automation API",
    description="API para disparar la automatización Selenium",
    version="0.1.0"
)

# Incluye los endpoints definidos en api/search.py
app.include_router(search_router)
