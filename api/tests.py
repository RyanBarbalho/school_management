from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from api.modelsDirec.school import School, SchoolTeachers
from api.modelsDirec.schoolyear import Grade
from api.modelsDirec.
from api.modelsDirec.user import Teacher
from api.serializers.userSerializer import TeacherSerializer

# class UsersManagersTests(TestCase):
#     def test_create_user(self):
#         User = get_user_model()
#         user = User.objects.create_user(email="normal@user.com", password="foo")
#         self.assertEqual(user.email, "normal@user.com")
#         self.assertTrue(user.is_active)
#         self.assertFalse(user.is_staff)
#         self.assertFalse(user.is_superuser)
#         try:
#             # username is None for the AbstractUser option
#             # username does not exist for the AbstractBaseUser option
#             self.assertIsNone(user.username)
#         except AttributeError:
#             pass
#         with self.assertRaises(TypeError):
#             User.objects.create_user()
#         with self.assertRaises(TypeError):
#             User.objects.create_user(email="")
#         with self.assertRaises(ValueError):
#             User.objects.create_user(email="", password="foo")

#     def test_create_superuser(self):
#         User = get_user_model()
#         admin_user = User.objects.create_superuser(
#             email="super@user.com", password="foo"
#         )
#         self.assertEqual(admin_user.email, "super@user.com")
#         self.assertTrue(admin_user.is_active)
#         self.assertTrue(admin_user.is_staff)
#         self.assertTrue(admin_user.is_superuser)
#         try:
#             # username is None for the AbstractUser option
#             # username does not exist for the AbstractBaseUser option
#             self.assertIsNone(admin_user.username)
#         except AttributeError:
#             pass
#         with self.assertRaises(ValueError):
#             User.objects.create_superuser(
#                 email="super@user.com", password="foo", is_superuser=False
#             )


class TeacherSerializerTest(TestCase):
    def setUp(self):
        self.school = School.objects.create(name="Test School", phone="1234567890")
        self.teacher_data = {
            "email": "test@example.com",
            "password": "testpassword",
            "name": "Test Teacher",
            "phone": "1234567890",
            "address": "Test Address",
            "school_id": self.school.id,
        }

    def test_create_teacher(self):
        serializer = TeacherSerializer(data=self.teacher_data)
        self.assertTrue(serializer.is_valid())
        teacher = serializer.save()
        self.assertEqual(Teacher.objects.count(), 1)
        self.assertEqual(SchoolTeachers.objects.count(), 1)
        self.assertEqual(teacher.email, self.teacher_data["email"])
        self.assertEqual(teacher.name, self.teacher_data["name"])
        self.assertEqual(str(teacher.phone), self.teacher_data["phone"])
        self.assertEqual(teacher.address, self.teacher_data["address"])
        self.assertTrue(teacher.check_password(self.teacher_data["password"]))
        self.assertTrue(
            SchoolTeachers.objects.filter(teacher=teacher, school=self.school).exists()
        )


class GradeViewSetTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.principal_user = User.objects.create_user(
            username="principal@example.com", password="password"
        )
        self.non_principal_user = User.objects.create_user(
            username="non_principal@example.com", password="password"
        )
        self.school_teacher = SchoolTeachers.objects.create(
            teacher=self.principal_user, isPrincipal=True
        )
        self.grade = Grade.objects.create(
            name="Grade 1", school=self.school_teacher.school
        )
