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

    # Lista de posibles rutas al binario de Chrome/Chromium
    candidates = [
        os.getenv("CHROME_BIN"),
        "/usr/bin/chromium-browser",
        "/usr/bin/chromium",
        "/usr/bin/google-chrome",
    ]
    for path in candidates:
        if path and os.path.exists(path):
            options.binary_location = path
            break
    else:
        raise RuntimeError("Chrome binary no encontrado en ninguna ruta conocida")

    # Usa el driver instalado por APT
    driver_path = os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")
    service = Service(driver_path)

    driver = webdriver.Chrome(service=service, options=options)
    return driver
