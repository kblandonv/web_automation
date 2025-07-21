# Web Automation con Selenium y FastAPI

Automatiza búsquedas en Wikipedia, genera un PDF de la página resultante y empaqueta todo en un ZIP, todo a través de un endpoint HTTP construido con FastAPI.

---

## 📋 Requisitos

- Python ≥ 3.8  
- Google Chrome instalado  
- Conexión a Internet (para descargar ChromeDriver vía `webdriver-manager`)  

---

## 🚀 Instalación

1. **Clona el repositorio**  
   ```bash
   git clone https://github.com/tu-usuario/web_automation.git
   cd web_automation
   ```

2. **Crea y activa un entorno virtual**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # Linux / macOS
   venv\Scripts\activate     # Windows
   ```

3. **Instala las dependencias**  
   ```bash
   pip install -r requirements.txt
   ```

---

## 🗂️ Estructura de carpetas

```
web_automation/
├── api/
│   ├── __init__.py
│   └── search.py               ← Define el router `/search`
├── automation/
│   ├── __init__.py
│   ├── selenium_driver.py      ← Inicializa ChromeDriver
│   └── search.py               ← `perform_search(...)`
├── file_manager/
│   ├── __init__.py
│   ├── pdf_manager.py          ← `save_pdf_via_cdp(...)`
│   └── archive_manager.py      ← `compress_folder(...)`
├── utils/
│   ├── __init__.py
│   └── logger.py               ← Configura logging centralizado
├── test/
│   ├── __init__.py
│   ├── test_archive_manager.py
│   ├── test_logger.py
│   ├── test_pdf_manager.py
│   └── test_search.py          ← Integration-test sobre HTML local
├── main.py                     ← Arranca FastAPI y monta el router
├── requirements.txt            ← Lista de dependencias
└── README.md                   ← Este documento
```

---

## 🏃 Uso

1. **Arranca el servidor**  
   ```bash
   uvicorn main:app --reload
   ```

2. **Lanza una búsqueda**  
   En tu navegador o Postman, visita:
   ```
   http://127.0.0.1:8000/search?query=Python
   ```
   La respuesta JSON incluirá:
   - `result_title`: título de la página  
   - `result_url`: URL final  
   - `pdf_path`: ruta local al PDF generado  
   - `zip_path`: ruta al ZIP con el PDF  

3. **Revisa los archivos generados**  
   - `downloads/<término>/<término>_result.pdf`  
   - `downloads/<término>.zip`

---

## ✅ Tests

Se incluyen cuatro tests con **pytest**:

| Archivo                      | Qué prueba                                                         |
|------------------------------|--------------------------------------------------------------------|
| `test_archive_manager.py`    | Que `compress_folder()` genere un ZIP válido con archivos internos.|
| `test_pdf_manager.py`        | Que `save_pdf_via_cdp()` decodifique y escriba correctamente un PDF.|
| `test_logger.py`             | Que `get_logger()` sea idempotente y configure un `Logger`.       |
| `test_search.py`             | Integration-test: levanta un servidor HTTP local con un HTML estático y comprueba que `perform_search()` no falle. |

### Cómo ejecutar los tests

```bash
pytest -q
```

Deberías ver algo similar a:

```
....  
4 passed in 4.72s
```

---

## 📑 Ejecución de ejemplo

```bash
$ uvicorn main:app --reload
INFO:     Uvicorn running on http://127.0.0.1:8000
$ curl "http://127.0.0.1:8000/search?query=Python" | jq
{
  "query": "Python",
  "status": "ok",
  "result_title": "Python – Wikipedia",
  "result_url": "https://en.wikipedia.org/wiki/Python",
  "pdf_path": "downloads/Python/Python_result.pdf",
  "zip_path": "downloads/Python.zip"
}
```

- **PDF generado** en `downloads/Python/Python_result.pdf`  
- **ZIP empaquetado** en `downloads/Python.zip`

---
