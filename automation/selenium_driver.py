# automation/selenium_driver.py

import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver(headless: bool = True) -> webdriver.Chrome:
    """
    Inicializa y devuelve un WebDriver de Chrome usando el binario y driver
    instalados en el sistema (útil para ejecutar dentro de contenedores Docker).

    - headless: si True, lanza Chrome en modo headless.
    """
    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    # Ruta al ejecutable de Chrome/Chromium dentro del contenedor o sistema
    chrome_bin = os.getenv("CHROME_BIN", "/usr/bin/chromium")
    options.binary_location = chrome_bin

    # Ruta al ChromeDriver instalado en el sistema
    driver_path = os.getenv("CHROMEDRIVER_PATH", "/usr/bin/chromedriver")
    service = Service(driver_path)

    driver = webdriver.Chrome(service=service, options=options)
    return driver
