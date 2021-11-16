""" Imports for courses app forms """
from django import forms
from .models import Course, CourseClass


class CourseForm(forms.ModelForm):
    """ A form for the add_course view """
    class Meta:
        """ Uses the imported courses model for Django form generation """
        model = Course
        fields = ['name']


class CourseClassForm(forms.ModelForm):
    """ A form for the add_course view """
    class Meta:
        """ Uses the imported courses model for Django form generation """
        model = CourseClass
        fields = ['name', 'course', 'date_from', 'date_to']
        widgets = {
            'date_from': forms.SelectDateWidget,
            'date_to': forms.SelectDateWidget,
        }
