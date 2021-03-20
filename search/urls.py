
from .views import *
from django.urls import path, include
from django.contrib import admin

app_name = "search"
urlpatterns = [
    path("", SearchListView.as_view(), name="search"),

]
