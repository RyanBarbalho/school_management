from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import IsAuthenticated

from api.modelsDirec.school import SchoolTeachers
from api.modelsDirec.user import Student, Teacher
from api.permissions import IsPrincipal, IsTeacherOfSameSchool
from api.serializers.userSerializer import StudentSerializer, TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsPrincipal]

    def get_queryset(self):
        user = self.request.user
        school = SchoolTeachers.objects.get(teacher=user).school
        return Student.objects.filter(school=school)


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, IsPrincipal]
