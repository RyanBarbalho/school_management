from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView

from api.viewsDirec.attendanceView import AttendanceReportViewSet, AttendanceViewSet
from api.viewsDirec.courseView import *
from api.viewsDirec.JWTView import CustomJWTView
from api.viewsDirec.schoolView import *
from api.viewsDirec.schoolYearView import *
from api.viewsDirec.userView import *

router = routers.DefaultRouter()
router.register(r"students", StudentViewSet)
router.register(r"teachers", TeacherViewSet)
router.register(r"attendances", AttendanceViewSet)
router.register(r"attendancereports", AttendanceReportViewSet)
router.register(r"schools", SchoolViewSet)
router.register(r"publicstatements", PublicStatementsViewSet)
router.register(r"schoolteachers", SchoolTeachersViewSet)
router.register(r"courses", CourseViewSet)
router.register(r"schoolyears", SchoolYearViewSet)
router.register(r"semesters", SemesterViewSet)
router.register(r"grades", GradeViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("principal", PrincipalCreate.as_view(), name=PrincipalCreate.name),
    path("login", CustomJWTView.as_view(), name="login"),
]
