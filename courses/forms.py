""" Imports for courses app forms """
from django import forms
from .models import Course


class Add_course(forms.ModelForm):
    """ A form for the add_course view """
    class Meta:
        """ Uses the imported courses model for Django form generation """
        model = Course
        fields = ['name']
