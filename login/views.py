from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpRequest
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import LoginForm, RegisterForm
# Create your views here.

User = get_user_model()


class LoginView(View):
    """
    Base Login view
    """

    def get(self, request: HttpRequest):
        """
        Get methode will return the login
        HTML form
        """
        if request.user.is_authenticated:
            return redirect("products:featured_products")
        else:
            return render(request, "login.html")

    def post(self, request: HttpRequest):
        """
        POST methode will login the user
        and validate the form
        """
        post_dict = request.POST
        print(post_dict)
        if post_dict.get('register') is not None:
            print("register was clicked")
            return redirect("login:register")
        if post_dict is None:
            return redirect("login:Error")

        login_form = LoginForm(post_dict)
        if not login_form.is_valid():
            return redirect("login:Error")

        print(login_form.cleaned_data)
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("main")
        else:
            redirect(f"login:login id={5}")
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
        print(post_dict)
        if post_dict is None:
            return redirect("login:Error")

        login_form = RegisterForm(post_dict)
        if not login_form.is_valid():
            return redirect("login:Error")

        print(login_form.cleaned_data)

        return redirect("main")
