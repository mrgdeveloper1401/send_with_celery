from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    birth_date = models.DateTimeField(_("birth_date"), blank=True, null=True)

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")

    def __str__(self):
        return self.username


class SendNotification(models.Model):
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name='send_notification')
    is_send = models.BooleanField(default=False)
    
    def __str__(self):
        return self.email.email

    class Meta:
        db_table = 'send_notification'
        verbose_name = 'SendNotification'
        verbose_name_plural = 'SendNotifications'


class SendNotificationProxy(SendNotification):
    class Meta:
        proxy = True
        verbose_name_plural = _("Unsend Notifications")
        verbose_name = _('Unsend Notification')
