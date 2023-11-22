from rest_framework import serializers

from api.models.school import *

from .userSerializer import TeacherSerializer


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class PrincipalSerializer(serializers.Serializer):
    school = SchoolSerializer()
    teacher = TeacherSerializer()

    def create(self, validated_data):
        school_data = validated_data["school"]
        principal_data = validated_data["teacher"]

        school, teacher = School.objects.create_school(
            school_name=school_data.get("name"),
            school_address=school_data.get("address"),
            school_phone=school_data.get("phone"),
            principal_name=principal_data.get("name"),
            principal_email=principal_data.get("email"),
            principal_password=principal_data.get("password"),
            principal_phone=principal_data.get("phone"),
            principal_address=principal_data.get("address"),
        )
        return {"school": school, "teacher": teacher}


class PublicStatementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicStatements
        fields = "__all__"


class SchoolTeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SchoolTeachers
        fields = "__all__"
