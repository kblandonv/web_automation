import threading
import http.server
import socketserver
import time
from pathlib import Path

import pytest
from automation.search import perform_search
from automation.selenium_driver import get_driver
from selenium.webdriver.common.by import By

# 1) Fixture que crea el HTML de prueba
@pytest.fixture(scope="session", autouse=True)
def fixture_html(tmp_path_factory):
    fixtures = tmp_path_factory.mktemp("fixtures")
    html = fixtures / "search.html"
    html.write_text(
        """
        <!doctype html>
        <html>
          <body>
            <form action="#" id="f">
              <input id="searchInput" name="q">
            </form>
          </body>
        </html>
        """
    )
    return fixtures

# 2) Fixture que levanta un servidor HTTP en background
@pytest.fixture(scope="session", autouse=True)
def http_server(fixture_html):
    cwd = Path.cwd()
    # cambiamos cwd al fixture para servir sólo ese directorio
    handler = http.server.SimpleHTTPRequestHandler
    port = 8001

    # Navegar al directorio de fixtures
    server = socketserver.TCPServer(("localhost", port), handler)
    th = threading.Thread(target=server.serve_forever, daemon=True)
    # Servir desde fixture_html:
    old_cwd = cwd
    try:
        # Ajustar working dir
        import os
        os.chdir(fixture_html)
        th.start()
        # Dar tiempo a arrancar
        time.sleep(0.1)
        yield f"http://localhost:{port}/search.html"
    finally:
        server.shutdown()
        th.join()
        os.chdir(old_cwd)

def test_perform_search_integration(http_server):
    url = http_server  # la URL que me da el fixture
    driver = get_driver(headless=True)
    try:
        # Ejecuto la búsqueda; si no explota, pasa el test
        perform_search(
            driver=driver,
            url=url,
            search_term="foo",
            input_selector=(By.ID, "searchInput")
        )
    finally:
        driver.quit()
