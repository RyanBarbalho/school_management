from rest_framework import permissions

from api.modelsDirec.school import SchoolTeachers
from api.modelsDirec.user import Teacher


class IsPrincipal(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        user_id = request.user.id
        view_name = view.__class__.__name__

        if view_name == "StudentViewSet":
            return (
                request.data["school"]
                == SchoolTeachers.objects.get(teacher=user_id).school.id
                and SchoolTeachers.objects.get(teacher=user_id).isPrincipal
            )
        else:
            return SchoolTeachers.objects.get(teacher=user_id).isPrincipal


# students related permissions
class IsTeacherOfSameSchool(permissions.BasePermission):
    def has_permission(self, request, view):
        teacher = request.user

        teacher_school = SchoolTeachers.objects.get(teacher=teacher).school
        student_school = request.data["school"]
        return teacher_school == student_school
