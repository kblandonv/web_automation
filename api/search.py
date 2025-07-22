# api/search.py

from fastapi import APIRouter
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pathlib import Path

from automation.selenium_driver import get_driver
from automation.search import perform_search
from file_manager.pdf_manager import save_pdf_via_cdp
from file_manager.archive_manager import compress_folder
from utils.logger import get_logger


router = APIRouter()
logger = get_logger(__name__)

@router.get("/health")
async def health():
    return {"status": "up"}

@router.get("/search")
async def search(query: str):
    logger.info(f"Iniciando búsqueda para: '{query}'")
    driver = get_driver(headless=True)
    try:
        # 1) Buscar en Wikipedia
        perform_search(
            driver=driver,
            url="https://en.wikipedia.org/",
            search_term=query,
            input_selector=(By.ID, "searchInput")
        )
        WebDriverWait(driver, 10).until(EC.title_contains(query))
        result_title = driver.title
        result_url = driver.current_url
        logger.info(f"Página encontrada: {result_url}")

        # 2) Guardar PDF
        downloads_dir = Path("downloads") / query
        pdf_path = downloads_dir / f"{query}_result.pdf"
        save_pdf_via_cdp(driver, pdf_path)
        logger.info(f"PDF guardado en: {pdf_path}")

        # 3) Comprimir carpeta
        zip_path = Path("downloads") / f"{query}.zip"
        compress_folder(downloads_dir, zip_path)
        logger.info(f"ZIP creado en: {zip_path}")

    except Exception as e:
        logger.error("Error en flujo de automatización", exc_info=True)
        return {
            "query": query,
            "status": "error",
            "message": str(e)
        }
    finally:
        driver.quit()
        logger.info("Navegador cerrado")

    return {
        "query": query,
        "status": "ok",
        "result_title": result_title,
        "result_url": result_url,
        "pdf_path": str(pdf_path),
        "zip_path": str(zip_path)
    }
