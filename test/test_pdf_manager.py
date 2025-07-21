import base64
from pathlib import Path
from file_manager.pdf_manager import save_pdf_via_cdp

class FakeDriver:
    def __init__(self, raw_bytes: bytes):
        # Simula el base64 que devolvería Chrome
        self._b64 = base64.b64encode(raw_bytes).decode()
    def execute_cdp_cmd(self, cmd, params):
        assert cmd == "Page.printToPDF"
        return {"data": self._b64}

def test_save_pdf_via_cdp(tmp_path):
    contenido = b"%PDF-1.4\n%..."
    # Simula un driver de Chrome con contenido PDF
    driver = FakeDriver(contenido)
    
    salida = tmp_path / "out" / "p.pdf"
    save_pdf_via_cdp(driver, salida)
    
    # Verifica que el PDF se haya escrito correctamente
    assert salida.exists()
    assert salida.read_bytes() == contenido
