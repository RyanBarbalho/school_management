from rest_framework import serializers

from api.models.course import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
