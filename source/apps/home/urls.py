from django.urls import path
from source.apps.home.views import (
    home,
    log_in,
    log_out
)

urlpatterns = (
    path(route="", view=home, name="home"),
    path(route="login/", view=log_in, name="login"),
    path(route="logout/", view=log_out, name="logout")
)
