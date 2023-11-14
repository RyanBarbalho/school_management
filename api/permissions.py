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


class IsTeacherOfSameCourse(permissions.BasePermission):
    """
    Custom permission to only allow teachers of the same course to interact with the students.
    """

    def has_object_permission(self, request, view, obj):
        # Check if the user is a teacher and if the student is in one of the teacher's courses.
        return (
            request.user.is_teacher and obj.course in request.user.course_set.all()
        )  # request.user.course_set.all() = reverse relatiion of course_set in teacher model
