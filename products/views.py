from carts.models import Cart
from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
# Create your views here.


class ProductListView(ListView):
    """
        A view for show all the products
    """
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """
            This function override the defult context constractor
            we use it for adding more data to context
        """
        context = super().get_context_data(**kwargs)
        context['nbar'] = 'products'
        return context


class ProductDetailView(DetailView):
    """
        A view for detailed of a product  
    """
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """
            This function override the defult context constractor
            we use it for adding more data to context
        """
        context = super().get_context_data(**kwargs)
        context['cart'], _ = Cart.objects.new_or_get(self.request)
        return context


class ProductFeaturedListView(ListView):
    """
        A view for show all the products
    """
    queryset = Product.objects.featured()

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """
            This function override the defult context constractor
            we use it for adding more data to context
        """
        context = super().get_context_data(**kwargs)
        return context


class ProductFeaturedDetailView(DetailView):
    """
        A view for detailed of a product  
    """
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        """
            This function override the defult context constractor
            we use it for adding more data to context
        """
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart.objects.new_or_get(self.request)
        return context
