from rest_framework import permissions

from api.modelsDirec.school import SchoolTeachers
from api.modelsDirec.user import Teacher

# is_principal


class IsPrincipal(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        user_id = int(request.META.get("HTTP_CLIENT_APP_ID", str(request.user.id)))
        return SchoolTeachers.objects.filter(
            teacher_id=user_id, isPrincipal=True
        ).exists()


# students related permissions
class IsTeacherOfSameSchool(permissions.BasePermission):
    def has_permission(self, request, view):
        teacher = request.user
        try:
            teacher_school = SchoolTeachers.objects.get(teacher=teacher).school
            student_school = request.data["school"]
            return teacher_school == student_school
        except SchoolTeachers.DoesNotExist:
            return False
