import calendar
from datetime import datetime
from django import forms


class DonationForm(forms.Form):
    """
    A form class to be used to take donor details and the donation amount
    """
    name = forms.CharField(label="Full Name", max_length=70, required=False)
    email = forms.EmailField(label="Email Address", max_length=320)
    donation_amount = forms.DecimalField(
        label="Donation Amount",
        min_value=0.50,
        max_value=100.00,
        required=True
    )


class PaymentForm(forms.Form):
    """ A form class to be used to take donor payment details """

    MONTH_CHOICES = [(m, calendar.month_name[m]) for m in range(1, 13)]
    YEAR_CHOICES = [(y, y) for y in range(
        datetime.now().year, datetime.now().year + 16)]

    credit_card_number = forms.CharField(
        label="Card Number", max_length=16, required=True)
    cvv = forms.CharField(
        label="Security Code (CVV)", max_length=3, required=True)
    expiry_month = forms.ChoiceField(
        label="Month", choices=MONTH_CHOICES, required=True)
    expiry_year = forms.ChoiceField(
        label="Year", choices=YEAR_CHOICES, required=True)
    stripe_id = forms.CharField(widget=forms.HiddenInput)
