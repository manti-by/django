FROM python:3.8-slim

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends vim

COPY requirements.txt /tmp/requirements.txt
RUN pip install --trusted-host pypi.org --no-cache-dir --upgrade pip && \
    pip install --trusted-host pypi.org --no-cache-dir -r /tmp/requirements.txt

RUN apt-get autoremove -y --purge && \
    apt-get clean -y

WORKDIR /app
CMD python manage.py runserver 0.0.0.0:8000