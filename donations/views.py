from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.conf import settings
from django.contrib import messages
from django.views.decorators.http import require_POST
import stripe
from .forms import DonationForm # PaymentForm
import json


def donations(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    donation_form = DonationForm(request.POST)

    if request.method == 'POST':

        if donation_form.is_valid():
            donation = donation_form
            total = 0
            total += donation.amount
        try:
            data = json.loads(request.data)
            # Create a PaymentIntent with the order amount and currency
            intent = stripe.PaymentIntent.create(
                amount=total,
                currency='gbp',
                automatic_payment_methods={
                    'enabled': True,
                },
            )
            return jsonify({
                'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return jsonify(error=str(e)), 403
    template = 'donations/donations.html'
    context = {
        'donation_form': donation_form,
        # 'payment_form': payment_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent,
    }

    return render(request, template, context)



# copied and amended from Boutique Ado walkthrough.
# (https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/b5e178737596a1a1cf5be50345dc770b119918fd/checkout/views.py)


# @require_POST
# def cache_checkout_data(request):
#     try:
#         pid = request.POST.get('client_secret').split('_secret')[0]
#         stripe.api_key = settings.STRIPE_SECRET_KEY
#         stripe.PaymentIntent.modify(pid, metadata={
#             'save_info': request.POST.get('save_info'),
#             'username': request.user,
#         })
#         return HttpResponse(status=200)
#     except Exception as e:
#         messages.error(request, 'Sorry, your payment cannot be \
#             processed right now. Please try again later.')
#         return HttpResponse(content=e, status=400)


# def donations(request):
#     stripe_public_key = settings.STRIPE_PUBLIC_KEY
#     stripe_secret_key = settings.STRIPE_SECRET_KEY

#     donation_form = DonationForm(request.POST)
#     # payment_form = PaymentForm(request.POST)

#     if request.method == 'POST':

#         if donation_form.is_valid():
#             donation = donation_form
#             total = 0
#             total += donation.amount

#             request.session['save_info'] = 'save-info' in request.POST
#             return redirect(reverse(
#                 'checkout_success', args=[donation.name]
#             ))
#         else:
#             messages.error(request, 'There was an error with your form. \
#                 Please double check your information.')

#         order_total = total
#         stripe_total = round(order_total * 100)
#         stripe.api_key = stripe_secret_key
#         intent = stripe.PaymentIntent.create(
#             amount=stripe_total,
#             currency=settings.STRIPE_CURRENCY,
#         )


#     if not stripe_public_key:
#         messages.warning(request, 'Stripe public key is missing. \
#             Did you forget to set it in your environment?')

#     template = 'donations/donations.html'
#     context = {
#         'donation_form': donation_form,
#         # 'payment_form': payment_form,
#         'stripe_public_key': stripe_public_key,
#         'client_secret': stripe_secret_key,
#     }

#     return render(request, template, context)


# def checkout_success(request, order_number):
#     """
#     Handle successful checkouts
#     """
#     save_info = request.session.get('save_info')
#     order = get_object_or_404(Order, order_number=order_number)
#     messages.success(request, f'Order successfully processed! \
#         Your order number is {order_number}. A confirmation \
#         email will be sent to {order.email}.')

#     if 'bag' in request.session:
#         del request.session['bag']

#     template = 'checkout/checkout_success.html'
#     context = {
#         'order': order,
#     }

#     return render(request, template, context)

# def donations(request):
#     """ A view to return the donations page """
#     if request.method == 'POST':
#         donation_form = DonationForm(request.POST)
#         payment_form = PaymentForm(request.POST)
#         if donation_form.is_valid() and payment_form.is_valid():
#             donation = donation_form.save()
#             total = 0
#             total += donation.amount

#             try:
#                 data = json.loads(request.data)
#                 # Create a PaymentIntent with the order amount and currency
#                 intent = stripe.PaymentIntent.create(
#                     amount=total,
#                     currency='gbp',
#                     automatic_payment_methods={
#                         'enabled': True,
#                     },
#                 )
#                 return jsonify({
#                     'clientSecret': intent['client_secret']
#                 })
#             except Exception as e:
#                 return jsonify(error=str(e)), 403

#             # customer = stripe.Customer.create(
#             #                 description="My First Test Customer"
#             #             )

#             # try:
#             #     stripe.PaymentIntent.create(
#             #         customer='customer',
#             #         currency="gbp",
#             #         amount=total,
#             #         payment_method_types=["card"],
#             #         setup_future_usage="on_session",
#             #     )
#             # except stripe.error.CardError:
#             #     messages.error(request, "Your Card Was Declined")

#             # try:
#             #     customer = stripe.Charge.create(
#             #         amount=(total * 100),
#             #         currency="GBP",
#             #         description=donation.name,
#             #         card=payment_form.cleaned_data['stripe_id'],
#             #     )
#             # except stripe.error.CardError:
#             #     messages.error(request, "Your Card Was Declined")

#             if customer.paid:
#                 messages.success(
#                     request,
#                     "You have successfully paid, thank you for your donation."
#                 )
#                 return redirect('dontations')
#             else:
#                 messages.error(request, "Unable to take payment")
#         else:
#             print(payment_form.errors)
#             messages.error(
#                 request, "We were unable to take payment with that card")
#     else:
#         donation_form = DonationForm()
#         payment_form = PaymentForm()

#     context = {
#         'donation_form': donation_form,
#         'payment_form': payment_form,
#         'Publishable': settings.STRIPE_PUBLISHABLE
#     }

#     return render(request, 'donations/donations.html', context)
