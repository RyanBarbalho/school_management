from rest_framework import generics, permissions, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from api.modelsDirec.school import *
from api.serializers.schoolSerializer import *


class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [permissions.AllowAny]
    # get all schools anyone can do it
    # create school only principal can do it


class PrincipalCreate(generics.CreateAPIView):
    name = "create-principal"
    serializer_class = PrincipalSerializer
    permission_classes = [permissions.AllowAny]


class PublicStatementsViewSet(viewsets.ModelViewSet):
    queryset = PublicStatements.objects.all()
    serializer_class = PublicStatementsSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        request.data["sender"] = request.user.id
        request.data["school"] = request.user.school.id
        return super().create(request, *args, **kwargs)


class SchoolTeachersViewSet(viewsets.ModelViewSet):
    queryset = SchoolTeachers.objects.all()
    serializer_class = SchoolTeachersSerializer
    permission_classes = [AllowAny]
