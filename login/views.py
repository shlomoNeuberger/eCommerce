from django.http.response import Http404
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpRequest
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.utils.http import is_safe_url
from .forms import LoginForm, RegisterForm
# Create your views here.

User = get_user_model()


class LoginView(View):
    """
    Base Login view
    """

    def get(self, request: HttpRequest, *args, **kwargs):
        """
        Get methode will return the login
        HTML form
        """
        print(next)
        return render(request, "login.html", {'next': next})

    def post(self, request: HttpRequest):
        """
        POST methode will login the user
        and validate the form
        """
        post_dict = request.POST
        next_ = request.POST.get("next", None)
        if post_dict is None:
            return Http404("What are you doing?")  # redirect("login:Error")
        login_form = LoginForm(post_dict)
        if not login_form.is_valid():
            return Http404("What are you doing?")  # redirect("login:Error")
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        print(username)
        if user is not None:
            login(request, user)
            if is_safe_url(next_, request.get_host()) and 'login' not in next_:
                return redirect(next_)
            return redirect("main")
        return redirect("login:login")


class LogoutView(View):
    """
    Base Login view
    """

    def get(self, request: HttpRequest):
        """
        Get methode will return the login
        HTML form
        """
        if request.user.is_authenticated:
            logout(request)
            return redirect("login:login")
        else:
            return render(request, "login.html")


class RegisterView(View):
    def get(self, request: HttpRequest):
        """
        Get methode will return the login
        HTML form
        """
        return render(request, "register.html")

    def post(self, request: HttpRequest):
        """
        POST methode will login the user
        and validate the form
        """
        post_dict = request.POST
        if post_dict is None:
            return Http404("What are you doing?")  # redirect("login:Error")

        register_form = RegisterForm(post_dict)
        if not register_form.is_valid():
            return Http404("What are you doing?")  # redirect("login:Error")

        next_ = request.POST.get("next", None)
        User.objects.create(**register_form.cleaned_data)
        if is_safe_url(next_, request.get_host()):
            return redirect(next_)
        else:
            return redirect("main")
