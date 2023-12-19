from django.urls import path
from source.apps.trips.views import newly_order, process_order_payment

app_name = "trips"

urlpatterns = (
    path(route="newly_order/", view=newly_order, name="home_page"),
    path(route="paid_order/<int:pk>/", view=process_order_payment, name="home_page"),
)
