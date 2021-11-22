""" Imports for the students app forms """
from django import forms
from .models import Student


class ReferralForm(forms.ModelForm):
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
        widgets = {
            'dob': forms.SelectDateWidget(years=range(1950, 2021)),
            'int_courses': forms.CheckboxSelectMultiple
        }


class StudentForm(forms.ModelForm):
    """ A form class to be used in the add_student view """
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
            'status',
            'int_courses',
            # 'enrol_num',
            # 'enrol_url',
            # 'courses',
        ]
        widgets = {
            'dob': forms.SelectDateWidget(years=range(1940, 2021)),
            'int_courses': forms.CheckboxSelectMultiple,
            'courses': forms.CheckboxSelectMultiple,
        }
