from django.http.response import Http404
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpRequest
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.utils.http import is_safe_url
from .forms import GuestEmailForm, LoginForm, RegisterForm
from .models import GuestEmail
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
        next_ = request.GET.get("next")
        msg = request.session.get("login_msg", None)
        try:
            del request.session['login_msg']
        except:
            pass

        return render(request, "login.html", {'next_': next_, 'msg': msg})

    def post(self, request: HttpRequest):
        """
        POST methode will login the user
        and validate the form
        """
        post_dict = request.POST
        next_ = request.POST.get("next_", None)
        if post_dict is None:
            return Http404("What are you doing?")  # redirect("login:Error")
        login_form = LoginForm(post_dict)
        if not login_form.is_valid():
            return Http404("What are you doing?")  # redirect("login:Error")
        username = login_form.cleaned_data['username']
        password = login_form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if next_ != "None" and is_safe_url(next_, request.get_host()) and 'login' not in next_:
                return redirect(next_)
            return redirect("main")
        request.session['login_msg'] = "username/password error"
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
        try:
            del request.session['username_msg']
            del request.session['register_msg']
        except:
            pass
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
        if request.user.is_authenticated:
            return redirect('main')
        context = {
            'username': request.session.get('username_msg', None),
            'email': request.session.get('register_msg', None),
        }
        try:
            del request.session['username_msg']
            del request.session['register_msg']
        except:
            pass
        return render(request, "register.html", context)

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
        print(register_form.cleaned_data)
        user, creted = User.objects.get_or_create(
            username=register_form.cleaned_data['username'])
        if creted and user.email != register_form.cleaned_data['email']:
            user.email = register_form.cleaned_data['email']
            user.set_password(register_form.cleaned_data['password'])
            user.first_name = register_form.cleaned_data['first_name']
            user.last_name = register_form.cleaned_data['last_name']
            user.save()
            login(request, user)
            if is_safe_url(next_, request.get_host()):
                return redirect(next_)
            else:
                return redirect("main")
        else:
            if not creted:
                request.session['username_msg'] = "username is used"
            if user.email == register_form.cleaned_data['email']:
                request.session['register_msg'] = "username is used"
            return redirect("login:register")


class GuestLogin(View):
    """
    Base Login view
    """

    def get(self, request: HttpRequest, *args, **kwargs):
        """
        Get methode will return the login
        HTML form
        """
        next_ = request.GET.get("next")
        return render(request, "login.html", {'next_': next_})

    def post(self, request: HttpRequest):
        """
        POST methode will login the user
        and validate the form
        """
        post_dict = request.POST
        next_ = request.POST.get("next_", None)
        if post_dict is None:
            return Http404("What are you doing?")  # redirect("login:Error")
        guest_form = GuestEmailForm(post_dict)
        if not guest_form.is_valid():
            return Http404("What are you doing?")  # redirect("login:Error")
        email = guest_form.cleaned_data['email']
        new_guest, _ = GuestEmail.objects.get_or_create(email=email)
        request.session['guest_id'] = new_guest.id
        if new_guest is not None:
            if next_ != "None" and is_safe_url(next_, request.get_host()) and 'login' not in next_:
                return redirect(next_)
            return redirect("main")
        return redirect("login:login")
