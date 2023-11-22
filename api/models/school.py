from django.db import models, transaction

from api.models import Teacher


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

        principal = Teacher(
            email=principal_email,
            name=principal_name,
            phone=principal_phone,
            address=principal_address,
            is_active=True,
        )
        principal.set_password(principal_password)
        principal.save()

        school_teachers = SchoolTeachers(
            school=school,
            teacher=principal,
            isPrincipal=True,
        )
        school_teachers.save()

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


class PublicStatements(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)
    sender = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=None)
    # many to one relation between school and public statements
    school = models.ForeignKey(School, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.title


class SchoolTeachers(models.Model):
    school = models.ForeignKey(School, on_delete=models.CASCADE, default=None)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=None)
    isPrincipal = models.BooleanField(default=False)

    class Meta:
        db_table = "school_teachers"
