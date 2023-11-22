from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models

from api.managers import CustomUserManager

from .school import School


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


class Teacher(CustomUser):
    name = models.CharField(max_length=50, default="user")
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "teachers"


class Student(CustomUser):
    name = models.CharField(max_length=50, default="user")
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=50, null=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "students"
