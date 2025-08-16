# Usar una imagen base de Python 3.11.12
FROM python:3.11.12-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requisitos primero para aprovechar la caché de Docker
COPY requirements.txt .

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos
COPY . .

# Exponer el puerto que usa la aplicación
EXPOSE 5001

# Comando para ejecutar la aplicación
CMD ["python", "flask_api.py"]