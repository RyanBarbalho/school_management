from rest_framework import serializers

from api.modelsDirec.school import School, SchoolTeachers
from api.modelsDirec.user import Student, Teacher


class TeacherSerializer(serializers.ModelSerializer):
    school_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Teacher
        fields = ("id", "email", "password", "name", "phone", "address", "school_id")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    # quando teacher é criado, cria também o model SchoolTeachers relacionado a escola fornecida
    def create(self, validated_data):
        print(f"validated_data before popping school_id: {validated_data}")
        school_id = validated_data.pop("school_id", None)
        print(f"school_id: {school_id}")  # Print school_id for debugging
        print(f"validated_data after popping school_id: {validated_data}")
        instance = super().create(validated_data)
        instance.set_password(validated_data["password"])
        instance.save()

        # create an instance of schoolteachers
        try:
            if school_id is not None:
                school = School.objects.get(id=school_id)
                schoolteachers = SchoolTeachers(
                    school=school,
                    teacher=instance,
                )
                schoolteachers.save()
        except:
            raise serializers.ValidationError("School does not exist")
        return instance


class StudentSerializer(serializers.ModelSerializer):
    school = serializers.PrimaryKeyRelatedField(queryset=School.objects.all())

    class Meta:
        model = Student
        fields = ("id", "email", "password", "name", "phone", "address", "school")
        extra_kwargs = {
            "password": {"write_only": True},
        }

    # cria o model e a senha hashada é sobrescrita
    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.set_password(validated_data["password"])
        instance.save()

        return instance
