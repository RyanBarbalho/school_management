from rest_framework import generics, permissions, status, viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from api.modelsDirec.school import *
from api.permissions import *
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
    permission_classes = [IsTeacher, IsSameSchool]

    def create(self, request, *args, **kwargs):
        request.data["sender"] = request.user.id
        request.data["school"] = request.user.school.id
        return super().create(request, *args, **kwargs)


class SchoolTeachersViewSet(viewsets.ModelViewSet):
    queryset = SchoolTeachers.objects.all()
    serializer_class = SchoolTeachersSerializer

    def create(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response(
                {"error": "User not authenticated"}, status=status.HTTP_403_FORBIDDEN
            )

        school_id = request.data["school"]
        teacher_id = request.data["teacher"]

        # check if the teacher is already in the school
        if SchoolTeachers.objects.filter(school=school_id, teacher=teacher_id).exists():
            return Response(
                {"error": "teacher already in the school"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # check if user is from same school
        if not SchoolTeachers.objects.filter(
            school=school_id, teacher=request.user
        ).exists():
            return Response(
                {"error": "user not from same school"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # check if user is principal
        if not SchoolTeachers.objects.filter(
            school=school_id, teacher=request.user, isPrincipal=True
        ).exists():
            return Response(
                {"error": "user not principal"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().create(request, *args, **kwargs)
