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
    path('<school_id>', views.school_details, name='school_details'),
    path('<event_id>', views.event_details, name='event_details'),
    path('edit_school/<school_id>', views.edit_school, name='edit_school'),
    path('delete_school/<school_id>', views.delete_school, name='delete_school'),
    path('edit_event/<event_id>', views.edit_event, name='edit_event'),
    path('delete_event/<event_id>', views.delete_event, name='delete_event'),
]
