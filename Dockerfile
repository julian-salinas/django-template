FROM python:3.9.5

ENV PYTHONUNBUFFERED=1

WORKDIR /opt/

COPY . .

RUN apt -y update && \
    rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

RUN mkdir /opt/backend/backend/logs
RUN touch /opt/backend/backend/logs/general.log

# environment variables for local development
ENV POSTGRES_DB=database
ENV POSTGRES_USER=username
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_HOST=db

# keep it secret!
ENV SECRET_KEY='django-insecure-o1pb)sm48dar%4azjar+c@3hayr1$xeupn(mz!9z#bz!z05ol)'


ENV DEBUG=True

RUN python backend/manage.py collectstatic --noinput

CMD gunicorn --chdir /opt/backend backend.wsgi:application --bind 0.0.0.0:$PORT