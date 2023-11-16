from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView

from api.models import *
from api.permissions import *
from api.serializers import *


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [permissions.AllowAny]
    # get all schools anyone can do it
    # create school only principal can do it


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsTeacher, IsSameSchool, IsTeacherOfSameCourse]
    # teacher can only see students in his courses of same school


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.AllowAny]


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


# class CreateSchoolView(APIView):
#     def post(self, request, format=None):
#         data = self.request.data
#         User = get_user_model()
#         school, principal = User.objects.create_school(
#             school_name=data.get("school_name"),
#             school_address=data.get("school_address"),
#             school_phone=data.get("school_phone"),
#             principal_name=data.get("principal_name"),
#             principal_email=data.get("principal_email"),
#             principal_password=data.get("principal_password"),
#             principal_phone=data.get("principal_phone"),
#             principal_address=data.get("principal_address"),
#         )
#         return Response(
#             {"status": "School and Principal created"}, status=status.HTTP_201_CREATED
#         )


class PrincipalCreate(generics.CreateAPIView):
    name = "create-principal"
    serializer_class = PrincipalSerializer
    permission_classes = [permissions.AllowAny]


class LoginView(TokenObtainPairView):
    name = "login"
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]
