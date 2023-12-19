from django.contrib import admin
from source.apps.trips.models import Trip


@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    """Інкапсулює всі опції адміністрування та функціональність для `Trip` моделі."""

    list_display = (
        "id",
        "user",
        "origin",
        "destination",
        "price",
        "is_paid",
        "scheduled_time",
        "scheduled_date",
        "date_created",
    )
