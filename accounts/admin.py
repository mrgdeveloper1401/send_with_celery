from typing import Any
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.db.models.query import QuerySet
from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _

from accounts.models import User, SendNotification, SendNotificationProxy


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_form_template = "admin/auth/user/add_form.html"
    change_user_password_template = None
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", 'email', "usable_password", "password1", "password2"),
            },
        ),
    )
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    search_fields = ("username", "first_name", "last_name", "email")
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


@admin.register(SendNotification)
class SendNotificationAdmin(admin.ModelAdmin):
    list_display = ('id', "email", "is_send")

    
    def get_queryset(self, request) -> QuerySet[Any]:
        return super().get_queryset(request).filter(is_send=True)


@admin.register(SendNotificationProxy)
class SendNotificationProxyAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'is_send']
    
    def get_queryset(self, request: HttpRequest) -> QuerySet[Any]:
        return super().get_queryset(request).filter(is_send=False)
