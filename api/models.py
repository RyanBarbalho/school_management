from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class CustomUser(AbstractUser, models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    
    groups = models.ManyToManyField(Group, related_name='customuser_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_user_permissions')

class Student(CustomUser):
    semester = models.IntegerField()
    
    def __str__(self):
        return self.name
    
class Teacher(CustomUser):
    
    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=50)
    
    semester = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)
    def __str__(self):
        return self.name
    
#many to many relation between student and course
class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)
    
    def __str__(self):
        return self.student.name
    
#relation of number of attendance for every class
class AttendanceReport(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    total_lecture = models.IntegerField()
    attendance = models.IntegerField()
    def __str__(self):
        return self.student.name
    
class PublicStatements(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
    def __str__(self):
        return self.title