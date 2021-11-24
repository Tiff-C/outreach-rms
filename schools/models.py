""" Imports for use in schools app models """
from django.db import models
from django.contrib.auth.models import User

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
        return str(self.name)


class Event(models.Model):
    """ A class to define the events model """
    name = models.CharField(max_length=254)
    school = models.ForeignKey(School, null=True, on_delete=models.SET_NULL)
    date = models.DateField(auto_now=False, auto_now_add=False)
    start_time = models.TimeField("Event Start Time")
    staff = models.ManyToManyField(User, verbose_name="Staff Attending Event")

    def __str__(self):
        name = self.name
        date = self.date
        formatted_date = date.strftime('%d/%m/%y')

        return f'{name} - {formatted_date}'
