""" Imports for the courses app models """
from django.db import models

# Create your models here.


class Courses(models.Model):
    """ A class to define the courses model """
    name = models.CharField('Course Name', max_length=128)

    def __str__(self):
        return self.name
