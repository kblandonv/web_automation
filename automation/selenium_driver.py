# automation/selenium_driver.py

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver(headless: bool = True) -> webdriver.Chrome:
    """
    Inicializa Chrome usando el binario y driver instalados por APT.
    """
    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Ruta al ejecutable de Chromium dentro del contenedor
    options.binary_location = os.getenv("CHROME_BIN", "/usr/bin/chromium")

    # Usa el ChromeDriver del sistema
    driver_path = os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")
    service = Service(driver_path)

    driver = webdriver.Chrome(service=service, options=options)
    return driver
