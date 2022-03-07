""" Imports for donations app urls """
from django.urls import path
from .webhooks import webhook
from . import views

urlpatterns = [
    path('', views.donations, name='donations'),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('donation_success/<donation_id>', views.donation_success, name='donation_success'),
    path('wh/', webhook, name='webhook'),
]
