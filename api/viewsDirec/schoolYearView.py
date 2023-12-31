# schoolyear, smeester, grade
from rest_framework import generics, permissions, viewsets

from api.permissions import IsPrincipal
from api.serializers.schoolYearSerializer import *


class SchoolYearViewSet(viewsets.ModelViewSet):
    queryset = SchoolYear.objects.all()
    serializer_class = SchoolYearSerializer
    permission_classes = [IsPrincipal]
    # get all schools anyone can do it
    # create school only principal can do it


class SemesterViewSet(viewsets.ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer
    permission_classes = [IsPrincipal]


class GradeViewSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [IsPrincipal]
