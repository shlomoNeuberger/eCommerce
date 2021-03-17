from django.urls import path
from .views import *

app_name = "login"

urlpatterns = [
    path('', LoginView.as_view(), name="login"),
    path('login', LoginView.as_view()),
    path('register', RegisterView.as_view(), name="register"),
]
