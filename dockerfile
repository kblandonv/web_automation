# Dockerfile

FROM python:3.10-slim

# Instala Chromium, ChromeDriver y librerías necesarias
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    fonts-liberation \
    libappindicator3-1 \
    libxrandr2 \
    libxss1 \
    xdg-utils \
    libnss3 \
    libgconf-2-4 \
  && rm -rf /var/lib/apt/lists/*

# Variables para detectar binario y driver dentro del contenedor
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

WORKDIR /app

# Instala dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación
COPY . .

# Expone el puerto interno en el que corre Uvicorn
EXPOSE 8000

# Arranca Uvicorn escuchando siempre en 0.0.0.0:8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--log-level", "info"]
