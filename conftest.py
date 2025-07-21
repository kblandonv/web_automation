# conftest.py
import sys
from pathlib import Path

# Inserta la carpeta raíz del proyecto en sys.path
sys.path.insert(0, str(Path(__file__).parent))
