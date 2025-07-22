# Dockerfile

FROM python:3.10-slim

# 1) Instala Chromium, Chromium-Driver y librerías necesarias
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
  && \
  # Crea un symlink si es necesario (comprueba ruta real del paquete)
  ln -sf /usr/lib/chromium/chromedriver /usr/bin/chromedriver \
  && rm -rf /var/lib/apt/lists/*

# 2) Variables de entorno
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

WORKDIR /app

# 3) Instala dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4) Copia el código y start.sh
COPY . .
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

EXPOSE 8000

# 5) Arranca con tu wrapper
CMD ["/app/start.sh"]
