
from .views import ProductDetailView, ProductListView
from django.urls import path, include
from django.contrib import admin

app_name = "products"
urlpatterns = [
    path("", ProductListView.as_view(), name="products"),
    path("<int:pk>", ProductDetailView.as_view(), name="product"),

]
