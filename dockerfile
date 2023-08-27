# Python Base Image
FROM python:3.11.4


# Creating Working 
WORKDIR /Mfinanzas_app
# 
COPY ./requirements.txt /requirements.txt

# Lo instalo en una ruta especifica porque es de donde se va a ejecutar
RUN pip install --no-cache-dir --upgrade -r /requirements.txt -t "/usr/lib/python3.11"

RUN apt-get update && apt-get -y install cron vim

COPY crontab /etc/cron.d/crontab

# Copio todo a la carpeta de la VM
ADD . /Mfinanzas_app


# Ejecuto el comando cron
RUN crontab /etc/cron.d/crontab

# Ejecuto el comando cron
CMD ["cron", "-f"]