"""
Import required modules for courses urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_courses, name='courses'),
    path('add_course/', views.add_course, name='add_course'),
    path('<course_id>', views.course_details, name='course_details'),
]
