""" Imports for the courses app models """
from django.db import models
from schools.models import School

# Create your models here.


class Course(models.Model):
    """ A class to define the courses model """
    name = models.CharField('Course Name', max_length=128)
    course_code = models.CharField("Course Code", max_length=10, null=True)

    def __str__(self):
        name = self.name
        return str(name)


class CourseClass(models.Model):
    """ A class to define the CourseClass model """
    DEFAULT_LOCATION_ID = 1

    name = models.CharField('Class Name', max_length=128)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    date_from = models.DateField('Course Start Date')
    date_to = models.DateField('Course End Date')
    location = models.ForeignKey(
        School, on_delete=models.PROTECT, default=DEFAULT_LOCATION_ID)

    def __str__(self):
        name = self.name
        return str(name)
