from django import forms
from .models import Courses


class Add_course(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['name']
