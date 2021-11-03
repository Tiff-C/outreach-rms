from django import forms
from .models import School, Event


class Add_school(forms.ModelForm):
    class Meta:
        model = School
        fields = ['name', 'address_1', 'address_2', 'postcode', 'contact', 'phone', 'email']


class Add_event(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['school', 'date']