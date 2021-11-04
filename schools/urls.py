"""
Import required modules for schools urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('schools/', views.all_schools, name='schools'),
    path('events/', views.all_events, name='events'),
    path('schools/add_school', views.add_school, name='add_school'),
    path('schools/add_event', views.add_event, name='add_event'),
]
