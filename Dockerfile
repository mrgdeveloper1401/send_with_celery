FROM python:3.12-alpine

WORKDIR /home/app

COPY . .

RUN apk update && \
    apk upgrade -y && \
    apk add python3-pip \
    apk add gcc \
    apk ad libc-dev-bin \
    apk add postgresql \
    apk add libffi-dev \
    apk add build-essential \
    

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONOTWRITEBYTECODE=1
ENV DJANGO_SUPERUSER_PASSWORD=admin.1234

EXPOSE 8000

ENTRYPOINT [ "gunicorn", 'send_email.wsgi', '-b' ]
CMD [ "0.0.0.0:8000" ]