# Usa una imagen base oficial de Python
FROM python:3.11

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /code

# Copia el archivo de requisitos al contenedor
COPY requirements.txt .

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt



# Install Node.js and npm
RUN apt-get update && apt-get install -y curl \
&& curl -fsSL https://deb.nodesource.com/setup_22.x | bash - \
&& apt-get install -y nodejs


# Copia el código del proyecto al directorio de trabajo en el contenedor
COPY . /code/

# Ejecuta el comando para crear un nuevo proyecto Django
# RUN django-admin startproject password_generator .

# Expone el puerto que Django usa por defecto
# EXPOSE 8000

# Comando por defecto para ejecutar cuando se inicie el contenedor
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["python","manage.py","tailwind","start"]