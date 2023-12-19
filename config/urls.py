from django.contrib import admin
from django.urls import include, path

urlpatterns = (
    path(route="admin/", view=admin.site.urls),
    path(
        route="",
        view=include(
            arg=("home.urls", "home"),
        ),
    ),
    path(
        route="trips/",
        view=include(
            arg=("trips.urls", "trips"),
        ),
    ),
)
