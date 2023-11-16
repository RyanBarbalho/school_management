from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.DefaultRouter()
router.register("schools", views.SchoolViewSet)
router.register("students", views.StudentViewSet)
router.register("teachers", views.TeacherViewSet)
router.register("attendance", views.AttendanceViewSet)
router.register("attendance-report", views.AttendanceReportViewSet)
router.register("courses", views.CourseViewSet)
router.register("public-statements", views.PublicStatementsViewSet)
router.register("grades", views.GradeViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("principal", views.PrincipalCreate.as_view(), name=views.PrincipalCreate.name),
    path("api-token-auth", obtain_auth_token, name="api_token_auth"),
    path("login/", views.LoginView.as_view(), name="login"),
]
