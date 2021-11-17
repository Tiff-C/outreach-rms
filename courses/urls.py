"""
Import required modules for courses urls
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_courses, name='courses'),
    path('classes/', views.all_classes, name='classes'),
    path('add_course/', views.add_course, name='add_course'),
    path('add_class/', views.add_class, name='add_class'),
    path('<course_id>', views.course_details, name='course_details'),
    path('classes/<class_id>', views.class_details, name='class_details'),
    path('edit_course/<course_id>', views.edit_course, name='edit_course'),
    path('edit_class/<class_id>', views.edit_class, name='edit_class'),
    path(
        'delete_course/<course_id>',
        views.delete_course,
        name='delete_course'
    ),
    path('delete_class/<class_id>', views.delete_class, name='delete_class'),
]
