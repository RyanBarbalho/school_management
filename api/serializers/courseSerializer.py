from rest_framework import serializers

from api.modelsDirec.course import *


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = "__all__"
