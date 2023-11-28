from rest_framework import generics, permissions, viewsets

from api.modelsDirec.course import *
from api.permissions import IsPrincipal
from api.serializers.courseSerializer import *


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsPrincipal]

    def create(self, request, *args, **kwargs):
        request.data["school"] = request.user.school.id
        return super().create(request, *args, **kwargs)

    def get_queryset(self):
        if self.request.user.is_teacher:
            return Course.objects.filter(teacher=self.request.user.id)
        else:
            return Course.objects.filter(student=self.request.user.id)
