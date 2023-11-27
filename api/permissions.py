from rest_framework import permissions

from api.modelsDirec.school import SchoolTeachers
from api.modelsDirec.user import Teacher


# is_principal
# if is a principal, can view, add, change, delete
class IsPrincipal(permissions.BasePermission):
    def has_permission(self, request, view):
        return SchoolTeachers.objects.filter(
            school_id=request.user.school.id, teacher_id=request.user.id
        ).exists()


# if is a student, can only view
class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return Teacher.objects.filter(id=request.user.id).exists()


class IsSameSchool(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Only allow users from the same school to view or edit the object.
        return request.user.school == obj.school


class IsTeacherReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return (
                request.user
                and request.user.is_authenticated
                and request.user.is_teacher
            )

        return False


class StudentOfOfSameSchool(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return ()

        return False


class IsPrincipal(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        user_id = int(request.META.get("HTTP_CLIENT_APP_ID", str(request.user.id)))
        return SchoolTeachers.objects.filter(
            teacher_id=user_id, isPrincipal=True
        ).exists()
