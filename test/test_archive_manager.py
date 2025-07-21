import zipfile
from pathlib import Path
from file_manager.archive_manager import compress_folder

def test_compress_folder(tmp_path):
    # Prepara una carpeta con un archivo de prueba
    folder = tmp_path / "demo"
    folder.mkdir()
    (folder / "hola.txt").write_text("¡hola!")
    
    # Ruta del ZIP
    zip_path = tmp_path / "demo.zip"
    compress_folder(folder, zip_path)
    
    # Asegura que existe el ZIP
    assert zip_path.exists()
    
    # Verifica que dentro del ZIP esté "demo/hola.txt"
    with zipfile.ZipFile(zip_path, "r") as zf:
        assert "demo/hola.txt" in zf.namelist()
