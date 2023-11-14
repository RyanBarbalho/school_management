from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models, transaction


class CustomUser(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=50)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)

    groups = models.ManyToManyField(Group, related_name="customuser_groups")
    user_permissions = models.ManyToManyField(
        Permission, related_name="customuser_user_permissions"
    )


class Principal(models.Manager):
    @transaction.atomic
    def create_school(
        self,
        school_name,
        school_address,
        school_phone,
        principal_name,
        principal_email,
        principal_password,
        principal_phone,
        principal_address,
    ):
        school = School(
            name=school_name,
            address=school_address,
            phone=school_phone,
        )
        school.save()

        principal = Principal.objects.create_user(
            name=principal_name,
            email=principal_email,
            password=principal_password,
            phone=principal_phone,
            address=principal_address,
            school=school,
        )
        return school, principal


class School(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.IntegerField()

    objects = Principal()

    class Meta:
        db_table = "schools"

    def __str__(self):
        return self.name


class Teacher(CustomUser):
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None
    )  # many to one relation between school and teacher
    # decidi fazer many to one pq um professor pode dar aula em mais de uma escola mas
    # n seria com a mesma conta no sistema

    def __str__(self):
        return self.name

    class Meta:
        db_table = "teachers"


class Student(CustomUser):
    semester = models.IntegerField()
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, default=None
    )  # many to one relation between school and student

    def __str__(self):
        return self.name

    class Meta:
        db_table = "students"


class Course(models.Model):
    name = models.CharField(max_length=50)

    semester = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    student = models.ManyToManyField(Student)

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


# relation of number of attendance for every class
class AttendanceReport(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    total_lecture = models.IntegerField()
    attendance = models.IntegerField(default=0)

    def __str__(self):
        return self.student.name


class PublicStatements(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
    sender = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=None)
    # many to one relation between school and public statements
    school = models.ForeignKey(School, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title
