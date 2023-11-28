from rest_framework import generics, permissions, viewsets

from api.modelsDirec.attendance import *
from api.serializers.attendanceSerializer import *


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.AllowAny]
    #


class AttendanceReportViewSet(viewsets.ModelViewSet):
    queryset = AttendanceReport.objects.all()
    serializer_class = AttendanceReportSerializer
    permission_classes = [permissions.AllowAny]
