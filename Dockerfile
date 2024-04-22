FROM python:3.9-slim AS base

RUN pip install --upgrade pip

RUN apt-get update && apt-get install -y cron

WORKDIR /app

COPY requirements.txt .

COPY app.env .

RUN pip install --no-cache-dir -r requirements.txt

FROM base AS dev

RUN pip install --no-cache-dir \
    pylint \
    pytest

COPY . .

RUN echo "* * * * * root . /app/app.env && /usr/local/bin/python /app/main.py > /proc/1/fd/1 2>/proc/1/fd/2" > /etc/cron.d/mycron && \
    chmod 0644 /etc/cron.d/mycron && \
    touch /var/log/cron.log && \
    crontab /etc/cron.d/mycron

CMD ["cron", "-f"]