# automation/selenium_driver.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_driver(headless: bool = True) -> webdriver.Chrome:
    """
    Inicializa y devuelve un WebDriver de Chrome.
    headless=True para ejecución en segundo plano.
    """
    options = Options()
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    if headless:
        options.add_argument("--headless")
    options.add_argument("--window-size=1920,1080")
    # evita problemas de detección en algunos sitios:
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    return driver
