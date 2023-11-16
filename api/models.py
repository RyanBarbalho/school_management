from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission
from django.db import models, transaction

from .managers import CustomUserManager


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

        principal = Teacher.objects.create_user(
            email=principal_email,
            password=principal_password,
            name=principal_name,
            phone=principal_phone,
            address=principal_address,
            is_principal=True,
            school=school,
        )

        return school, principal


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
    name = models.CharField(max_length=50, default="user")
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=50, null=True)
    is_principal = models.BooleanField(default=False)
    school = models.ForeignKey(School, on_delete=models.CASCADE, default=None)
    # decidi fazer many to one pq um professor pode dar aula em mais de uma escola mas
    # n seria com a mesma conta no sistema

    def __str__(self):
        return self.name

    class Meta:
        db_table = "teachers"


class Student(CustomUser):
    name = models.CharField(max_length=50, default="user")
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=50, null=True)
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
    School = models.ForeignKey(School, on_delete=models.CASCADE, default=None)

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


class PublicStatements(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
    sender = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=None)
    # many to one relation between school and public statements
    school = models.ForeignKey(School, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title


# grades
class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # first, second and last grade
    first_grade = models.IntegerField(blank=True, null=True)
    second_grade = models.IntegerField(blank=True, null=True)
    last_grade = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return (
            self.student.name
            + " "
            + self.course.name
            + " "
            + str(self.first_grade)
            + " "
            + str(self.second_grade)
            + " "
            + str(self.last_grade)
        )
