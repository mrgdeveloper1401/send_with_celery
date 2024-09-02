from celery import Celery
from os import environ


environ.setdefault("DJANGO_SETTINGS_MODULE", "send_email.settings")

app = Celery('send_email', broker='amqp://guest@localhost')

app.autodiscover_tasks()
app.config_from_object('django.conf:settings', namespace='CELERY')
