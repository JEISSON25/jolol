# Usa una imagen base de Python
FROM python:3.9-slim

# Configura variables de entorno para evitar que Python genere archivos .pyc y para que no se haga buffering en la salida
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Define el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos y lo instala
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto del código de la aplicación
COPY . /app/

# Ejecuta collectstatic (opcional si ya lo tienes preparado)
RUN python manage.py collectstatic --noinput

# Expone el puerto y define el comando por defecto (se puede cambiar a runserver en desarrollo)
CMD ["gunicorn", "sisvoteAdmin.wsgi:application", "--bind", "0.0.0.0:8013"]
