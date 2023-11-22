from django.db import models

from .course import Course
from .school import School
from .user import Student


class SchoolYear(models.Model):
    name = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    class Meta:
        db_table = "school_years"


class Semester(models.Model):
    name = models.CharField(max_length=50)
    school_year = models.ForeignKey(SchoolYear, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student)

    class Meta:
        db_table = "semesters"

    def __str__(self):
        return self.name


class SemesterCourse(models.Model):
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = "semester_courses"


class Grade(models.Model):
    firstGrade = models.DecimalField(max_digits=2, decimal_places=2)
    secondGrade = models.DecimalField(max_digits=2, decimal_places=2)
    finalGrade = models.DecimalField(max_digits=2, decimal_places=2)


# grades
class StudentSemester(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    Course = models.ForeignKey(Course, on_delete=models.CASCADE)

    class Meta:
        db_table = "student_semester_grades"

    def __str__(self):
        return (
            self.student.name
            + " "
            + self.semester.name
            + " "
            + self.Course.name
            + " "
            + str(self.grade.finalGrade)
        )
