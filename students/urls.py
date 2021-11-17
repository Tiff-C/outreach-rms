""" Imports for students app urls """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_students, name='students'),
    path('referrals/', views.all_referrals, name='referrals'),
    path('new_referral/', views.add_referral, name='new_referral'),
    path('add_student/<student_id>', views.add_student, name='add_student'),
    path(
        'referrals/<student_id>',
        views.referral_details,
        name='referral_details'
    ),
    path(
        '<student_id>',
        views.student_details,
        name='student_details'
    ),
    path(
        'edit_referral/<student_id>',
        views.edit_referral,
        name='edit_referral'
    ),
    path(
        'edit_student/<student_id>',
        views.edit_student,
        name='edit_student'
    ),
    path(
        'delete_referral/<student_id>',
        views.delete_referral,
        name='delete_referral'
    ),
    path(
        'delete_student/<student_id>',
        views.delete_student,
        name='delete_student'
    ),
]
