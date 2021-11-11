"""
Import required modules for home app urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]
