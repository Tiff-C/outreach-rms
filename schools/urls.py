"""
Import required modules for schools urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_schools, name='schools'),
    path('events/', views.all_events, name='events'),
    path('add_school/', views.add_school, name='add_school'),
    path('events/add_event/', views.add_event, name='add_event'),
]
