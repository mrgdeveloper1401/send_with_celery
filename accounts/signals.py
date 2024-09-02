from django.db.models.signals import post_save
from django.dispatch import receiver

from accounts.models import User, SendNotification
from accounts.tasks import send_email_create_user


@receiver(post_save, sender=User)
def send_email_with_create_user(sender, instance, created, **kwargs):
    if created:
        SendNotification.objects.create(email=instance)
        send_email_create_user.delay([instance.email])
