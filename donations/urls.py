""" Imports for donations app urls """
from django.urls import path
from . import views

urlpatterns = [
    path('', views.donations, name='donations'),
    path('create_payment_intent/', views.donations, name='create_payment_intent'),
]
