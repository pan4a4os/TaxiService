from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

__all__ = ("RegisterForm",)


class RegisterForm(UserCreationForm):
    """Клас `RegisterForm`, який представляє форму для моделі реєстрації користувача."""

    username = forms.CharField(label="Псевдонім користувача")

    class Meta:
        """Необов'язковий клас `Meta` для параметризації та модифікації поведінки класу `RegisterForm`."""

        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")
