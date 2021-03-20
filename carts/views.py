from django.http.response import Http404
from products.models import Product
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpRequest
from random import randint
from .models import Cart
# Create your views here.


def cart_home(request: HttpRequest):
    cart_obj, _ = Cart.objects.new_or_get(request)
    print(cart_obj.products.all())
    return render(request, "carts/home.html", {'cart': cart_obj})


def cart_update(request: HttpRequest):
    cart_obj, _ = Cart.objects.new_or_get(request)
    slug = request.POST.get('product_slug', None)

    if request.POST.get('product_slug', None):
        if request.POST.get("remove"):
            product = Product.objects.get(slug=slug)
            cart_obj.products.remove(product)
        elif request.POST.get("add"):
            product = Product.objects.get(slug=slug)
            cart_obj.products.add(product)
    else:
        return Http404("What are you trying to do")
    products_count = cart_obj.products.count()
    if products_count == 0:
        del request.session['cart_items']
    else:
        request.session['cart_items'] = products_count

    return redirect("cart:home")