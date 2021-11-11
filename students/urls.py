""" Imports for students app urls """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_referrals, name='referrals'),
    path('new_referral/', views.add_referral, name='new_referral'),
]
