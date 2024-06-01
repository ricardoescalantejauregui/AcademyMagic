# Usa una imagen base oficial de Python 3.11
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo de requisitos al directorio de trabajo
COPY requirements.txt requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el contenido de la aplicación al directorio de trabajo
COPY . .

# Expone el puerto en el que correrá la aplicación
#EXPOSE 5000
# Expone los puertos 80 y 443
EXPOSE 80
EXPOSE 443

# Establece la variable de entorno para Flask
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

# Corre el comando para iniciar la aplicación
CMD ["flask", "run"]
