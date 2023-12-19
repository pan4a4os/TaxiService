import logging
from datetime import datetime

from django import forms
from django.contrib.auth.models import User
from source.apps.trips.models import Trip

__all__ = ("TripForm",)

logger = logging.getLogger(name=__name__)


class TripForm(forms.ModelForm):
    """Клас `Trip`, який представляє форму для моделі поїздки."""

    user = forms.ModelChoiceField(queryset=User.objects.all(), label="Користувач")
    scheduled_date = forms.DateField(label="Запланована дата поїздки", input_formats=("%m/%d/%Y",))

    class Meta:
        """Необов'язковий клас `Meta` для параметризації та модифікації поведінки класу `TripForm`."""

        model = Trip
        fields = ("user", "origin", "destination", "scheduled_time", "scheduled_date")
        widgets: dict[str : forms.TextInput] = {
            "origin": forms.TextInput(attrs={"type": "text", "placeholder": "Введіть пункт відправлення"}),
            "destination": forms.TextInput(attrs={"type": "text", "placeholder": "Введіть пункт призначення"}),
            "scheduled_time": forms.TimeInput(attrs={"placeholder": "00:00:00"}),
            "scheduled_date": forms.DateInput(attrs={"placeholder": "ММ/ДД/РРРР"}),
        }

    def __init__(self, *args, **kwargs) -> None:
        """"""

        super().__init__(*args, **kwargs)
        if hasattr(self.instance, "username"):
            self.fields["user"].choices = ((self.instance.pk, str(self.instance.username)),)
            self.instance = Trip()

    def is_valid(self) -> bool:
        """Повертає True, якщо форма не містить помилок, або False в іншому випадку."""

        _selected_date = self.data.get("scheduled_date")
        _selected_time = self.data.get("scheduled_time")

        if _selected_date and _selected_time:
            try:
                logger.info(msg=_selected_date)
                _selected_datetime = datetime.strptime(_selected_date + _selected_time, "%m/%d/%Y%H:%M:%S")
                if datetime.now() > _selected_datetime:
                    return False
            except ValueError:
                logger.info(msg="EXCEPTION")
                return False

        return super().is_valid()
