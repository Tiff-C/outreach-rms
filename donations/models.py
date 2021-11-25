from django.db import models


class Donation(models.Model):
    """ A class to define the donations model """
    name = models.CharField("Full Name", max_length=70, blank=False)
    email = models.EmailField("Email Address", max_length=320, blank=False)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return f'{self.id}-{self.date}-{self.name}'
