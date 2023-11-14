from rest_framework import permissions


# is_principal
# if is a principal, can view, add, change, delete
class IsPrincipal(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and request.user.is_authenticated and request.user.is_principal
        )


# if is a student, can only view
class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated

        request.user and request.user.is_authenticated and request.user.is_teacher


class IsSameSchool(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated

        request.user and request.user.is_authenticated and request.user.is_same_school


# this is for attendances and classes, the student can only see his own attendances and classes
