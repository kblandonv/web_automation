# file_manager/pdf_manager.py

import base64
from pathlib import Path
from selenium.webdriver.remote.webdriver import WebDriver

def save_pdf_via_cdp(driver: WebDriver, output_path: Path):
    """
    Usa la CDP de Chrome para generar un PDF de la página actual
    y lo guarda en output_path (Pathlib.Path).
    """
    # Genera el PDF (devuelve dict con clave "data" conteniendo base64)
    pdf_data = driver.execute_cdp_cmd(
        "Page.printToPDF",
        {
            "printBackground": True,
            # puedes añadir más opciones aquí (márgenes, escala, etc.)
        }
    )["data"]

    # Decodifica de base64 y escribe el archivo
    pdf_bytes = base64.b64decode(pdf_data)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(pdf_bytes)
