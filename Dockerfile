FROM python:3.10-slim

# Instalar dependencias necesarias del sistema
RUN apt-get update && apt-get install -y \
    gcc python3-dev build-essential \
    git ffmpeg libsm6 libxext6 \
    && rm -rf /var/lib/apt/lists/*


WORKDIR /app

# Copiar archivo de dependencias e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el código fuente dentro de /app
COPY ./app /app

# Crear carpeta para imágenes si no existe
RUN mkdir -p /app/data/images

# Exponer puertos para FastAPI y FiftyOne
EXPOSE 8000
EXPOSE 5151

# Comando por defecto: lanzar FastAPI desde app.main
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"] 