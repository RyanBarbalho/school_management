from rest_framework import serializers

from api.models import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            "id",
            "name",
            "email",
            "semester",
        )


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = (
            "id",
            "name",
            "email",
            "semester",
        )


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"


class AttendanceReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttendanceReport
        fields = "__all__"


class PublicStatementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicStatements
        fields = "__all__"
