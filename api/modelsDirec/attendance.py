from django.db import models


# many to many relation between student and course
class Attendance(models.Model):
    student = models.ForeignKey("api.Student", on_delete=models.CASCADE)
    course = models.ForeignKey("api.Course", on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.student.name


# attendance = teacher will mark the attendance of the student for every class,


# relation of number of attendance for every class
class AttendanceReport(models.Model):
    student = models.ForeignKey("api.Student", on_delete=models.CASCADE)
    course = models.ForeignKey("api.Course", on_delete=models.CASCADE)
    total_lecture = models.IntegerField()
    attendance = models.IntegerField(default=0)

    def __str__(self):
        return self.student.name
