from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from .forms import DonationForm, PaymentForm
import stripe

stripe.api_key = settings.STRIPE_SECRET


def donations(request):
    """ A view to return the donations page """
    if request.method == 'POST':
        donation_form = DonationForm(request.POST)
        payment_form = PaymentForm(request.POST)
        if donation_form.is_valid() and payment_form.is_valid():
            donation = donation_form.save()
            total = 0

            total += donation.amount

            try:
                customer = stripe.Charge.create(
                    amount=(total * 100),
                    currency="GBP",
                    description=donation.name,
                    card=payment_form.cleaned_data['stripe_id'],
                )
            except stripe.error.CardError:
                messages.error(request, "Your Card Was Declined")

            if customer.paid:
                messages.success(
                    request,
                    "You have successfully paid, thank you for your donation."
                )
                return redirect('dontations')
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(
                request, "We were unable to take payment with that card")
    else:
        donation_form = DonationForm()
        payment_form = PaymentForm()
        context = {
            'donation_form': donation_form,
            'payment_form': payment_form,
            'publishable': settings.STRIPE_PUBLISHABLE
        }

    return render(request, 'donations/donations.html', context)
