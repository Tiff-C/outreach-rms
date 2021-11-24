from django import forms
from .models import Order


class PaymentForm(forms.Form):
    """ A form class to be used to take donor payment details """

    MONTH_CHOICES = [(i, i) for i in range(1, 12)]
    YEAR_CHOICES = [(i, i) for i in range(2021, 2040)]

    card_number = forms.CharField(
        label="Card Number", max_length=16, required=False)
    cvv = forms.CharField(
        label="Security Code (CVV)", max_length=3, required=False)
    expiry_month = forms.ChoiceField(
        label="Month", choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(
        label="Year", choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widgets=forms.HiddenInput)


class OrderForm(forms.ModelForm):
    """ A form class to be used to take donor details """
    class Meta:
        model = Order
        fields = ['name', 'email']
