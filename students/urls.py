""" Imports for students app urls """
from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.all_referrals, name='referrals'),
    path('students/new_referral', views.add_student, name='new_referral'),
]
