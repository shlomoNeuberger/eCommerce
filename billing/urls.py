
from .views import *
from django.urls import path
from django.contrib import admin

app_name = "bill"

urlpatterns = [
    path('shipping', create_shipping_add, name="address_shipping")
]
