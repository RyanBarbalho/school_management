from django.db import models

from api.models import CustomUser


class Teacher(CustomUser):
    name = models.CharField(max_length=50, default="user")
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=50, null=True)
    # schoolTeachers = models.ManyToManyField(
    #     School, through=SchoolTeachers, related_name="teachers"
    # )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "teachers"


class Student(CustomUser):
    name = models.CharField(max_length=50, default="user")
    phone = models.IntegerField(null=True)
    address = models.CharField(max_length=50, null=True)
    school = models.ForeignKey("api.School", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "students"
