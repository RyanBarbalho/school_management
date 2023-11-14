from rest_framework import serializers

from api.models import *

# responsible for creating school and principal


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = (
            "id",
            "name",
            "email",
            "semester",
        )
        extra_kwargs = {
            "password": {"write_only": True},
        }


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = (
            "id",
            "name",
            "email",
            "semester",
        )


""" responsible for creating school and principal """


class PrincipalSerializer(serializers.Serializer):
    school = SchoolSerializer()
    Principal = TeacherSerializer()

    def create(self, validated_data):
        school_data = validated_data["school"]
        principal_data = validated_data["principal"]

        school, principal = School.objects.create_school(
            school_name=school_data.get("name"),
            school_address=school_data.get("address"),
            school_phone=school_data.get("phone"),
            principal_name=principal_data.get("name"),
            principal_email=principal_data.get("email"),
            principal_password=principal_data.get("password"),
            principal_phone=principal_data.get("phone"),
            principal_address=principal_data.get("address"),
        )
        return {"school": school, "principal": principal}

    # por enquanto, não é necessário atualizar o principal
    def update(self, instance, validated_data):
        raise NotImplementedError("Cannot call update() on an account")


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


class GradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = "__all__"
