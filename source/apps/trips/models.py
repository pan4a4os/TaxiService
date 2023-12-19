from django.contrib.auth.models import User
from django.db import models

__all__ = ("Trip",)


class Trip(models.Model):
    """Клас `Trip`, який представляє модель поїздки."""

    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="trips", verbose_name="Користувач")
    origin = models.CharField(max_length=64, verbose_name="Пункт відправлення")
    destination = models.CharField(max_length=64, verbose_name="Пункт призначення")
    price = models.PositiveIntegerField(default=50, verbose_name="Ціна(грн)")
    is_paid = models.BooleanField(default=False, verbose_name="Оплачено")
    scheduled_time = models.TimeField(editable=True, verbose_name="Запланований час поїздки")
    scheduled_date = models.DateField(editable=True, verbose_name="Запланована дата поїздки")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    class Meta:
        """Необов'язковий клас `Meta` для параметризації та модифікації поведінки класу `Trip`."""

        verbose_name = "Поїздка"
        verbose_name_plural = "Поїздки"

    def __str__(self) -> str:
        """Перетворення об'єкта в рядкове представлення."""

        return "Поїздка №" + str(self.pk)
