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

ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

WORKDIR /app

# Instala dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación y el script de arranque
COPY . .
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# Expone el puerto interno
EXPOSE 8000

# Usa el script para arrancar
CMD ["/app/start.sh"]
