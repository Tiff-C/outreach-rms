""" Imports for donations app urls """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.donations, name='donations'),
]
