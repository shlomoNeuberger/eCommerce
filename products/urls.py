
from .views import *
from django.urls import path, include
from django.contrib import admin

app_name = "products"
urlpatterns = [
    path("", ProductListView.as_view(), name="products"),
    path("<int:pk>", ProductDetailView.as_view(), name="product"),
    path("<slug:slug>", ProductDetailView.as_view(), name="product"),
    path("featured/", ProductFeaturedListView.as_view(), name="featured_products"),
    path("featured/<int:pk>", ProductFeaturedDetailView.as_view()),
    path("featured/<slug:slug>", ProductFeaturedDetailView.as_view(),
         name="featured_product"),

]
