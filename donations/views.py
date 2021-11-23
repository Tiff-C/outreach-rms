""" Imports for home app views """
from django.shortcuts import render


def donations(request):
    """ A view to return the donations page """

    return render(request, 'donations/donations.html')
