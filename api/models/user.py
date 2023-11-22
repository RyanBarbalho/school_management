from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.db.models import get_model

from api.managers import CustomUserManager

School = get_model("api", "School")


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

    # adicionei no tratamento do erro o custom_user❌❌❌❌


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
