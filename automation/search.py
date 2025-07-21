# automation/search.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver

def perform_search(
    driver: WebDriver,
    url: str,
    search_term: str,
    input_selector: tuple,
    timeout: int = 10
) -> None:
    """
    Navega a url, ingresa search_term en el campo de búsqueda
    y envía con Enter.
    """
    driver.get(url)
    wait = WebDriverWait(driver, timeout)

    # 1) Esperar y ubicar el campo de búsqueda
    search_input = wait.until(EC.presence_of_element_located(input_selector))
    search_input.clear()
    search_input.send_keys(search_term)

    # 2) Enviar el formulario directamente
    search_input.submit()