from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models

from .school import School
from .schoolyear import SchoolYear
from .user import *


class Course(models.Model):
    name = models.CharField(max_length=50)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    SchoolYear = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# attenance report = student will see the number of attendance for every course
