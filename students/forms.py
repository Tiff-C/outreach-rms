""" Imports for the students app forms """
from django import forms
from .models import Student


class Add_student(forms.ModelForm):
    """ A form class to be used in the add_referral view """
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'address_1',
            'address_2',
            'postcode',
            'dob',
            'phone',
            'email',
            'school',
            'int_courses',
        ]
