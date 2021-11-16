# Generated by Django 3.2.8 on 2021-11-15 19:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_rename_courses_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Class Name')),
                ('date_from', models.DateField(verbose_name='Course Start Date')),
                ('date_to', models.DateField(verbose_name='Course End Date')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.course')),
            ],
        ),
    ]