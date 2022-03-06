// Copied from boutique ado and amended to suit my project
// https://github.com/Code-Institute-Solutions/boutique_ado_v1/blob/b5e178737596a1a1cf5be50345dc770b119918fd/checkout/static/checkout/js/stripe_elements.js

/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/

var stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
var clientSecret = $('#id_client_secret').text().slice(1, -1);
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var style = {
    base: {
        color: '#000',
        fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
        fontSmoothing: 'antialiased',
        fontSize: '16px',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
};
var card = elements.create('card', {style:style},);
card.mount('#card-element');


// Handle realtime validation errors on the card element
card.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('card-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

// Handle form submit
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true});
    $('#submit-button').attr('disabled', true);
    $('#payment-form').fadeToggle(100);
    $('#loading-overlay').fadeToggle(100);

    var saveInfo = Boolean($('#id-save-info').attr('checked'));
    // From using {% csrf_token %} in the form
    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    var url = '/donations/create_payment_intent/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.name.value),
                    email: $.trim(form.email.value),
                }
            },
            shipping: {
                name: $.trim(form.full_name.value),
                phone: $.trim(form.phone_number.value),
                address: {
                    line1: $.trim(form.street_address1.value),
                    line2: $.trim(form.street_address2.value),
                    city: $.trim(form.town_or_city.value),
                    country: $.trim(form.country.value),
                    postal_code: $.trim(form.postcode.value),
                    state: $.trim(form.county.value),
                }
            },
        }).then(function(result) {
            if (result.error) {
                var errorDiv = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorDiv).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-overlay').fadeToggle(100);
                card.update({ 'disabled': false});
                $('#submit-button').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function () {
        // just reload the page, the error will be in django messages
        //location.reload();
        console.log('oh no, I failed again')
    })
});




// // Copied from https://stripe.com/docs/payments/quickstart and amended to suit my project


// var stripe_public_key = $('#id_stripe_public_key').text().slice(1, -1);
// var stripe = Stripe(stripe_public_key);

// // The items the customer wants to buy
// const items = [{ id: "xl-tshirt" }];
      
// let elements;
      
// initialize();
// checkStatus();

// document
//     .querySelector("#payment-form")
//     .addEventListener("submit", handleSubmit);

// // Fetches a payment intent and captures the client secret
// async function initialize() {
//     const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
//     const response = await fetch("/create-payment-intent", {
//     method: "POST",
//     headers: { "Content-Type": "application/json" },
//     body: JSON.stringify({ items }),
//     });
//     const { clientSecret } = await response.json();

//     const appearance = {
//     theme: 'stripe',
//     };
//     elements = stripe.elements({ appearance, clientSecret });

//     const paymentElement = elements.create("payment");
//     paymentElement.mount("#payment-element");
// }

// async function handleSubmit(e) {
//     e.preventDefault();
//     setLoading(true);

//     const { error } = await stripe.confirmPayment({
//     elements,
//     confirmParams: {
//         // Make sure to change this to your payment completion page
//         return_url: "http://localhost:4242/checkout.html",
//     },
//     });

//     // This point will only be reached if there is an immediate error when
//     // confirming the payment. Otherwise, your customer will be redirected to
//     // your `return_url`. For some payment methods like iDEAL, your customer will
//     // be redirected to an intermediate site first to authorize the payment, then
//     // redirected to the `return_url`.
//     if (error.type === "card_error" || error.type === "validation_error") {
//     showMessage(error.message);
//     } else {
//     showMessage("An unexpected error occured.");
//     }

//     setLoading(false);
// }

// // Fetches the payment intent status after payment submission
// async function checkStatus() {
//     const clientSecret = new URLSearchParams(window.location.search).get(
//     "payment_intent_client_secret"
//     );

//     if (!clientSecret) {
//     return;
//     }

//     const { paymentIntent } = await stripe.retrievePaymentIntent(clientSecret);

//     switch (paymentIntent.status) {
//     case "succeeded":
//         showMessage("Payment succeeded!");
//         break;
//     case "processing":
//         showMessage("Your payment is processing.");
//         break;
//     case "requires_payment_method":
//         showMessage("Your payment was not successful, please try again.");
//         break;
//     default:
//         showMessage("Something went wrong.");
//         break;
//     }
// }

// // ------- UI helpers -------

// function showMessage(messageText) {
//     const messageContainer = document.querySelector("#payment-message");

//     messageContainer.classList.remove("hidden");
//     messageContainer.textContent = messageText;

//     setTimeout(function () {
//     messageContainer.classList.add("hidden");
//     messageText.textContent = "";
//     }, 4000);
// }

// // Show a spinner on payment submission
// function setLoading(isLoading) {
//     if (isLoading) {
//     // Disable the button and show a spinner
//     document.querySelector("#submit").disabled = true;
//     document.querySelector("#spinner").classList.remove("hidden");
//     document.querySelector("#button-text").classList.add("hidden");
//     } else {
//     document.querySelector("#submit").disabled = false;
//     document.querySelector("#spinner").classList.add("hidden");
//     document.querySelector("#button-text").classList.remove("hidden");
//     }
// }