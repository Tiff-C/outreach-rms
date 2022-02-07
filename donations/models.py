from django.db import models


class Donation(models.Model):
    """ A class to define the donations model """
    name = models.CharField(
        "Full Name (Optional)",
        default="Anonymous",
        max_length=70,
        blank=True)
    email = models.EmailField("Email Address", max_length=320, blank=False)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)
    donation_amount = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return f"{self.name} donated {self.donation_amount}"
