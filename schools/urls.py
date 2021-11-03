"""
Import required modules for schools urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('schools/', views.all_schools, name='schools'),
    path('events/', views.all_events, name='events'),
]
