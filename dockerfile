# Dockerfile

FROM python:3.10-slim

# 1) Pre-requisitos para agregar repositorio de Google
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
  && rm -rf /var/lib/apt/lists/*

# 2) Agregar llave y repositorio de Google Chrome
RUN wget -qO - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
  && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" \
     > /etc/apt/sources.list.d/google-chrome.list

# 3) Instalar Google Chrome Stable y librerías necesarias para headless
RUN apt-get update && apt-get install -y \
    google-chrome-stable \
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

# 4) Variables para Selenium
ENV CHROME_BIN=/usr/bin/google-chrome-stable
# Seguimos usando webdriver-manager o el chromedriver de apt si lo prefieres

WORKDIR /app

# 5) Instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 6) Copiar código y script de arranque
COPY . .
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# 7) Puerto interno
EXPOSE 8000

# 8) Arranque
CMD ["/app/start.sh"]
