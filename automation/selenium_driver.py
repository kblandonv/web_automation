# automation/selenium_driver.py

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver(headless: bool = True) -> webdriver.Chrome:
    """
    Inicializa y devuelve un WebDriver de Chrome/Chromium,
    detectando dinámicamente la ruta del binario en el contenedor.
    """
    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Rutas donde buscar el binario de Chrome/Chromium
    candidates = [
        os.getenv("CHROME_BIN"),
        "/usr/bin/google-chrome",
        "/usr/bin/google-chrome-stable",
        "/usr/bin/chromium",
        "/usr/bin/chromium-browser",
    ]
    for p in candidates:
        if p and os.path.exists(p):
            options.binary_location = p
            break
    else:
        raise RuntimeError(
            f"Chrome binary no encontrado en rutas: {candidates}"
        )

    # Como usas webdriver-manager, Selenium Manager o el driver de apt
    # Si prefieres webdriver-manager:
    from webdriver_manager.chrome import ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    # O, si quieres usar el chromedriver de apt:
    # service = Service(os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver"))

    driver = webdriver.Chrome(service=service, options=options)
    return driver
