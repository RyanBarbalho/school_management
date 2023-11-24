from rest_framework import serializers

from api.modelsDirec.school import School, SchoolTeachers
from api.modelsDirec.user import Student, Teacher


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ("id", "email", "password", "name", "phone", "address")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    # quando teacher é criado, cria também o model SchoolTeachers relacionado a escola fornecida
    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.set_password(validated_data["password"])
        instance.save()

        return instance


class StudentSerializer(serializers.ModelSerializer):
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())

    class Meta:
        model = Student
        fields = ("id", "email", "name", "phone", "address", "school")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    # cria o model e a senha hashada é sobrescrita
    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.set_password(validated_data["password"])
        instance.save()
        return instance
