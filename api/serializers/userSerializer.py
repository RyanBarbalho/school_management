from rest_framework import serializers

from api.models.user import *


class TeacherSerializer(serializers.ModelSerializer):
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())

    class Meta:
        model = Teacher
        fields = ("id", "email", "password", "name", "phone", "address", "school")

    # cria o model e a senha hashada é sobrescrita
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
