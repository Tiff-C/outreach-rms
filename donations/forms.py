import calendar
from datetime import datetime
from django import forms

from django.forms import ModelForm
from .models import Donation


class DonationForm(forms.ModelForm):
    """
    A form class to be used to take donor details and the donation amount
    """

    class Meta:
        model = Donation
        fields = ('name', 'email', 'donation_amount',)

