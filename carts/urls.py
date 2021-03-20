
from .views import *
from django.urls import path
from django.contrib import admin

app_name = "cart"
urlpatterns = [
    path("", cart_home, name="home"),
    path("update", cart_update, name="update"),
    path("update/<slug:slug>", cart_update, name="update"),


]
