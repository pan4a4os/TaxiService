from django.urls import path
from source.apps.home.views import (
    home,
    log_in,
    log_out
)

app_name = "home"

urlpatterns = (
    path(route="", view=home, name="home_page"),
    path(route="login/", view=log_in, name="login"),
    path(route="logout/", view=log_out, name="logout")
)
