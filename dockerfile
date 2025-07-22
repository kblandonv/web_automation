FROM python:3.10-slim

# 1) Instala Chromium, Chromium-Driver y librerías headless
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
  && rm -rf /var/lib/apt/lists/* \
  # 2) Asegura un symlink válido a /usr/bin/chromedriver
  && if [ -f /usr/lib/chromium/chromedriver ]; then \
         ln -sf /usr/lib/chromium/chromedriver /usr/bin/chromedriver; \
     fi \
  && if [ -f /usr/lib/chromium-browser/chromedriver ]; then \
         ln -sf /usr/lib/chromium-browser/chromedriver /usr/bin/chromedriver; \
     fi

# 3) Variables para Selenium
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

WORKDIR /app

# 4) Instala dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 5) Copia código y script de arranque
COPY . .
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

# 6) Expone el puerto interno
EXPOSE 8000

# 7) Arranca con tu wrapper
CMD ["/app/start.sh"]
