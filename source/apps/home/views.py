from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

__all__ = (
    "home",
    "log_in",
    "log_out"
)


def home(request) -> render:
    """"""

    return render(
        request=request,
        template_name="home/home.html",
        context={"title": "Головна"}
    )


def log_in(request) -> redirect or render:
    """"""

    if request.user.is_authenticated:
        return redirect(to="home")
    else:
        if request.method == "POST":
            _username: str = request.POST.get("username")

            user = authenticate(request, username=_username, password=request.POST.get("password"))
            if _username == "admin":
                return redirect(to="login_admin")
            elif user:
                login(request=request, user=user)
                return redirect(to="home")
            else:
                messages.warning(request=request, message="Ви невірно ідентифікували себе")

        return render(
            request=request,
            template_name="users/login.html",
            context={
                "title": "Вхід в систему"
            }
        )


def log_out(request) -> redirect:
    """"""

    logout(request=request)

    return redirect(to="login")
