# Generated by Django 4.2.5 on 2023-11-14 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_school_alter_student_options_alter_teacher_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicstatements',
            name='school',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.school'),
        ),
        migrations.AddField(
            model_name='publicstatements',
            name='sender',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='api.teacher'),
        ),
    ]
