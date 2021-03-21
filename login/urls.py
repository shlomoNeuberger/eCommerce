from django.urls import path
from .views import *

app_name = "login"

urlpatterns = [
    path('', LoginView.as_view()),
    path('login', LoginView.as_view(), name="login"),
    path('guest', GuestLogin.as_view(), name="guest"),
    path('login/<path:next_>', LoginView.as_view(), name="login"),
    path('register', RegisterView.as_view(), name="register"),
    path('logout', LogoutView.as_view(), name="logout"),
]
