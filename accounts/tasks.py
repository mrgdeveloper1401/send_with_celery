from celery import shared_task
from os import environ
from django.core.mail import send_mail
from dotenv import load_dotenv


load_dotenv()
@shared_task
def send_email_create_user(recipient_list):
    try:
        title = 'پیام خوش اومدید'
        text = 'کاربر گرامی به سایت ما خوش اومدید'
        from_email = environ['DEFAULT_FROM_EMAIL']
        send_mail(title, text, from_email, recipient_list)
    except Exception as e:
        raise e
