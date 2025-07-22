# Dockerfile

FROM python:3.10-slim

# 1) Instala Chromium, ChromeDriver y librerías necesarias para headless
RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    fonts-liberation \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libdrm2 \
    libgbm1 \
    libgtk-3-0 \
    libpango-1.0-0 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxrandr2 \
    libxss1 \
    libxtst6 \
    xdg-utils \
    libnss3 \
    libgconf-2-4 \
  && rm -rf /var/lib/apt/lists/*

# 2) Variables de entorno para Selenium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

# 3) Directorio de trabajo
WORKDIR /app

# 4) Instala dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5) Copia el código y el script de arranque
COPY . .
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# 6) Expone el puerto en el que Uvicorn escucha
EXPOSE 8000

# 7) Arranca tu aplicación con el wrapper
CMD ["/app/start.sh"]
