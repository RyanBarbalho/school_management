from django.core.exceptions import ObjectDoesNotExist
from rest_framework import permissions

from api.modelsDirec.school import SchoolTeachers
from api.modelsDirec.user import Teacher


class IsPrincipal(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        user_id = request.user.id
        view_name = view.__class__.__name__

        try:
            if view_name == "StudentViewSet":
                return Student.objects.filter(
                    id=user_id, school__isPrincipal=True
                ).exists()
            elif view_name == "TeacherViewSet":
                return SchoolTeachers.objects.filter(
                    teacher_id=user_id, isPrincipal=True
                ).exists()
        except ObjectDoesNotExist:
            raise Exception("User is not a principal")

        return False


# students related permissions
class IsTeacherOfSameSchool(permissions.BasePermission):
    def has_permission(self, request, view):
        teacher = request.user

        teacher_school = SchoolTeachers.objects.get(teacher=teacher).school
        student_school = request.data["school"]
        return teacher_school == student_school
