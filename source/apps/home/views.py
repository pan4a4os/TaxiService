from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from source.apps.home.forms import RegisterForm

__all__ = ("home", "log_in", "log_out", "sign_up")


def home(request) -> render:
    """Контролер, який відповідає за відображення головної сторінки."""

    return render(request=request, template_name="home/home.html", context={"title": "Головна"})


@csrf_exempt
def log_in(request) -> redirect or render:
    """Контролер, який відповідає за вхід користувача(або адміністратора) у систему."""

    if request.user.is_authenticated:
        return redirect(to="/", status=302)

    if request.method == "POST":
        user = authenticate(
            request=request, username=request.POST.get("username"), password=request.POST.get("password")
        )
        if not user:
            messages.warning(request=request, message="Ви невірно ідентифікували себе")

            return render(
                request=request, template_name="home/login.html", status=401, context={"title": "Вхід у систему"}
            )

        login(request=request, user=user)

        return redirect(to="/")

    return render(request=request, template_name="home/login.html", context={"title": "Вхід у систему"})


def log_out(request) -> redirect:
    """Контролер, який відповідає за вихід користувача із системи."""

    logout(request=request)

    return redirect(to="/login/")


def sign_up(request) -> redirect:
    """Контролер, який відповідає за реєстрацію(та автоматично авторизацію) користувача та вхід у систему."""

    if not request.user.is_authenticated:
        register_form = RegisterForm()

        if request.method == "POST":
            register_form = RegisterForm(data=request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request=request, message="Ви успішно зареєструвалися!")

                user = authenticate(
                    request=request, username=request.POST.get("username"), password=request.POST.get("password1")
                )
                if user:
                    login(request=request, user=user)

                return redirect(to="/")

        return render(
            request=request,
            template_name="home/sign_up.html",
            context={"title": "Register", "register_form": register_form},
        )

    return redirect(to="/")
