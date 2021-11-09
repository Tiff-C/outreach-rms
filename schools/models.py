""" Imports for use in schools app models """
from django.db import models

# Create your models here.


class School(models.Model):
    """ A class to define the schools model """
    name = models.CharField(max_length=254)
    address_1 = models.CharField("Address line 1", max_length=128,)
    address_2 = models.CharField("Address line 2", max_length=128, blank=True)
    postcode = models.CharField("Postcode", max_length=12,)
    contact = models.CharField("Main Contact Name", max_length=70, blank=True)
    phone = models.CharField("Contact Phone", max_length=15, blank=True)
    email = models.EmailField("Contact Email", max_length=320, blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    """ A class to define the events model """
    school = models.ForeignKey(School, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return '%s %s' % (self.school, self.date)
