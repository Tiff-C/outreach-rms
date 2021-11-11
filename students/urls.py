""" Imports for students app urls """
from django.urls import path
from . import views

urlpatterns = [
    path('referrals/', views.all_referrals, name='referrals'),
    path('new_referral/', views.add_referral, name='new_referral'),
    path('<student_id>', views.referral_details, name='referral_details'),
]
