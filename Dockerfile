FROM cimg/python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt  

# Copiar correctamente la carpeta app y plantillas
COPY app /app/app
COPY app/templates /app/templates

EXPOSE 5000

# Ajuste en el comando CMD
CMD ["python", "-m", "app.main"]
