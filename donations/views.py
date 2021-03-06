from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.conf import settings
from django.contrib import messages
from django.views.decorators.http import require_POST
import stripe
from .models import Donation
from .forms import DonationForm
#  import json


# copied and amended from Boutique Ado walkthrough.
# (https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/b5e178737596a1a1cf5be50345dc770b119918fd/checkout/views.py)


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'save_info': request.POST.get('save_info'),
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def donations(request):
    """
    A view to render the donation form. 
    If request = POST it will get the form data
    """
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    donation_form = DonationForm()

    if request.method == 'POST':
        form_data = {
            'full_name': request.POST.get('name'),
            'email': request.POST.get('email'),
            'donation_amount': request.POST.get('donation_amount'),
        }
        donation_form = DonationForm(form_data)
        # donation_form = DonationForm(request.POST)
        print(donation_form)

        if donation_form.is_valid():

            donation = donation_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            donation.stripe_pid = pid
            donation.save()

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('donation_success', args=[donation.id]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
            return redirect(reverse('donations'))
    else:
        print('stripe key:', stripe_public_key)
        total = 1 #  need to replace with a calculation of donation amount
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency='gbp',
        )

        print(intent)
        client_secret = intent.client_secret

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

    template = 'donations/donations.html'

    context = {
        'donation_form': donation_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': client_secret,
    }

    return render(request, template, context)

# still need to update checkout_success


def donation_success(request, donation_id):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    donation = get_object_or_404(
        Donation, pk=donation_id)
    messages.success(
        request, f'Donation of {donation.donation_amount} successfully processed! \
        A confirmation email will be sent to {donation.email}.')

    template = 'donations/donation_success.html'
    context = {
        'donation': donation,
    }

    return render(request, template, context)
