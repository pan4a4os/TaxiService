import random

import stripe
from django.conf import settings
from django.http import HttpResponseNotFound
from django.shortcuts import redirect, render
from source.apps.trips.forms import TripForm
from source.apps.trips.models import Trip
from source.apps.trips.tasks import send_notification_to_email

__all__ = ("newly_order", "process_order_payment")


def newly_order(request) -> render:
    """Контролер, який створює поїздку для конкретного користувача."""

    trip_form = TripForm(instance=request.user)

    if request.method == "POST":
        trip_form = TripForm(data=request.POST, instance=request.user)
        if trip_form.is_valid():
            trip_form.save()

            stripe.api_key = settings.STRIPE_SECRET_KEY

            _generated_price = random.randint(5000, 15000)
            _trip_representation: str = trip_form.instance.__str__()

            stripe_response = stripe.PaymentLink.create(
                line_items=[
                    {
                        "price": stripe.Price.create(
                            unit_amount=_generated_price,
                            currency="uah",
                            product=stripe.Product.create(
                                name=f"{_trip_representation} для {request.user.username}",
                                description="Оплата за подорож",
                            )["id"],
                        ).id,
                        "quantity": 1,
                    }
                ],
                metadata={"trip": _trip_representation},
                after_completion={
                    "type": "redirect",
                    "redirect": {
                        "url": (
                            f"http://127.0.0.1:8000/trips/paid_order/{trip_form.instance.pk}/?&price={_generated_price}"
                        )
                    },
                },
            )

            return redirect(to=stripe_response.url)

    return render(
        request=request,
        template_name="trips/newly_order.html",
        context={"title": "Замовити таксі", "trip_form": trip_form},
    )


def process_order_payment(request, pk: int) -> render:
    """
    Контролер, який оброляє зворотній виклик від Stripe,
    для встановлення оплаченого статусу поїздки та її показу користувачу.
    """

    _price: str = request.GET.get("price")
    if not _price:
        return HttpResponseNotFound(status=404)

    _trip = Trip.objects.filter(pk=pk)
    if not _trip.exists():
        return HttpResponseNotFound(status=404)

    trip = _trip.first()

    trip.price = int(_price) / 100
    trip.is_paid = True
    trip.save()

    send_notification_to_email.apply_async(
        args=(
            f"{trip.__str__()} для {trip.user.first_name} {trip.user.last_name}",
            (
                "Пункт відправлення: " + trip.origin + "\n"
                "Пункт призначення: " + trip.destination + "\n"
                "Ціна: " + str(trip.price) + "гривень\n"
                f"Дата та час запланованої поїздки: {trip.scheduled_date} {trip.scheduled_time}\n\n"
                "Таксі щойно прибула до пункту відправлення, гарної поїздки!"
            ),
            ("cutrys69@gmail.com",),
        ),
        countdown=random.randint(5, 10),
    )

    return render(
        request=request, template_name="trips/paid_order.html", context={"title": trip.__str__(), "trip": trip}
    )
