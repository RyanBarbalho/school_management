from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import IsAuthenticated

from api.modelsDirec.user import Student, Teacher
from api.permissions import IsPrincipal
from api.serializers.userSerializer import StudentSerializer, TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, IsPrincipal]

    # # teacher can only see students in his courses of same school
    # def get_queryset(self):
    #     user = self.request.user
    #     if user.is_principal:
    #         return Student.objects.all()
    #     else:
    #         return Student.objects.filter(course__teacher=user)


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, IsPrincipal]
