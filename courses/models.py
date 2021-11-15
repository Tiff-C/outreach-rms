""" Imports for the courses app models """
from django.db import models

# Create your models here.


class Course(models.Model):
    """ A class to define the courses model """
    name = models.CharField('Course Name', max_length=128)

    def __str__(self):
        name = self.name
        return str(name)


class CourseClass(models.Model):
    """ A class to define the CourseClass model """
    name = models.CharField('Class Name', max_length=128)
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    date_from = models.DateField('Course Start Date')
    date_to = models.DateField('Course End Date')

    def __str__(self):
        name = self.name
        return str(name)
