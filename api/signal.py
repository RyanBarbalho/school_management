from django.db.models.signals import m2m_changed
from django.dispatch import receiver

from .models import Course, Grade


# signal to create grade for every student inserted in a course
@receiver(m2m_changed, sender=Course.student.through)
def create_grade(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        for student_id in pk_set:
            Grade.objects.create(student_id=student_id, course=instance)


m2m_changed.connect(create_grade, sender=Course.student.through)
