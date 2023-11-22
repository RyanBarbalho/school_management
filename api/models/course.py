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


# many to many relation between student and course
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.student.name


# attendance = teacher will mark the attendance of the student for every class,


# relation of number of attendance for every class
class AttendanceReport(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    total_lecture = models.IntegerField()
    attendance = models.IntegerField(default=0)

    def __str__(self):
        return self.student.name


# attenance report = student will see the number of attendance for every course
