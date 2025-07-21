# file_manager/archive_manager.py

import shutil
from pathlib import Path

def compress_folder(folder_path: Path, zip_path: Path) -> None:
    """
    Comprime la carpeta `folder_path` en un ZIP ubicado en `zip_path`.
    """
    # Asegura que exista la carpeta padre de zip_path
    zip_path.parent.mkdir(parents=True, exist_ok=True)

    # Preparar base_name sin extensión
    base_name = str(zip_path.with_suffix(""))

    # Crea el .zip con el contenido de folder_path
    shutil.make_archive(
        base_name=base_name,
        format="zip",
        root_dir=str(folder_path.parent),
        base_dir=str(folder_path.name)
    )
