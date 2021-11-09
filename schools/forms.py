""" Imports for the schools app forms """
from django import forms
from .models import School, Event


class Add_school(forms.ModelForm):
    """ A form class to be used in the add_school view """
    class Meta:
        model = School
        fields = [
            'name',
            'address_1',
            'address_2',
            'postcode',
            'contact',
            'phone',
            'email',
        ]


class Add_event(forms.ModelForm):
    """ A form class to be used in the add_event view """
    class Meta:
        model = Event
        fields = ['school', 'date']
