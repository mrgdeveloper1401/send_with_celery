FROM python:3.12-alpine

WORKDIR /home/app

COPY . .

RUN apk update && \
    apk upgrade -y && \
    apk add pytohn3-pip

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN PYTHONUNBUFFERED=1
ENV DJANGO_SUPERUSER_PASSWORD=admin.1234


ENTRYPOINT [ "python3", 'send_email.wsgi', '-b' ]
CMD [ "0.0.0.0:8000" ]