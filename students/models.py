""" Required imports for Students app models """
from django.db import models
from django.contrib.auth.models import User
from schools.models import School

# Create your models here.


class Student(models.Model):
    """ A class to define the student model """
    first_name = models.CharField('Forename', max_length=35,)
    last_name = models.CharField('Surname', max_length=35,)
    address_1 = models.CharField("Address line 1", max_length=128,)
    address_2 = models.CharField("Address line 2", max_length=128, blank=True)
    postcode = models.CharField("Postcode", max_length=12,)
    phone = models.CharField("Contact Phone", max_length=15, blank=True)
    email = models.EmailField("Contact Email", max_length=320, blank=True)
    school = models.ForeignKey(School, null=True, on_delete=models.SET_NULL)
    referred_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    referral_date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
