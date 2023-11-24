from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

from api.managers import CustomUserManager


# verificar por que nao funciona inheritance manager
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []  # removes email from REQUIRED_FIELDS

    groups = models.ManyToManyField(Group, related_name="customuser_groups")
    user_permissions = models.ManyToManyField(
        Permission, related_name="customuser_user_permissions"
    )

    class Meta:
        app_label = "api"
