from django.core.mail import send_mail
from os import environ


def send_email(recipient_list):
    title = 'test send email with celery'
    text = 'کاربر گرامی به سایت ما خوش اومدید'
    from_to = environ['DEFUALT_FROM_EMAIL']
    send_mail(title, text, from_to, recipient_list)
