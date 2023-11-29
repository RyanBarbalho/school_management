from rest_framework import generics, permissions, viewsets
from rest_framework.permissions import IsAuthenticated

from api.modelsDirec.course import *
from api.permissions import IsPrincipal
from api.serializers.courseSerializer import *


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, IsPrincipal]
