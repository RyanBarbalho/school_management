from django.shortcuts import render
from rest_framework import viewsets

from api.models import *
from api.permissions import *
from api.serializers import *


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsPrincipal]


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsTeacher, IsSameSchool, IsTeacherOfSameCourse]
    # teacher can only see students in his courses of same school


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsPrincipal, IsSameSchool]


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsTeacher, IsSameSchool, IsTeacherOfSameCourse]
    #


class AttendanceReportViewSet(viewsets.ModelViewSet):
    queryset = AttendanceReport.objects.all()
    serializer_class = AttendanceReportSerializer
    permission_classes = [IsTeacher, IsSameSchool]


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsPrincipal, IsSameSchool]

    def create(self, request, *args, **kwargs):
        request.data["school"] = request.user.school.id
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_teacher:
            return Course.objects.filter(teacher=self.request.user.id)
        if self.request.user.is_student:
            return Course.objects.filter(student=self.request.user.id)

        return super().get_queryset()


class PublicStatementsViewSet(viewsets.ModelViewSet):
    queryset = PublicStatements.objects.all()
    serializer_class = PublicStatementsSerializer
    permission_classes = [IsTeacher, IsSameSchool]

    def create(self, request, *args, **kwargs):
        request.data["sender"] = request.user.id
        request.data["school"] = request.user.school.id
        return super().create(request, *args, **kwargs)


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsTeacher, IsSameSchool]

    # the student can only see his own grades
    def get_queryset(self):
        if self.request.user.is_student:
            return Grade.objects.filter(student=self.request.user.id)
        return super().get_queryset()
