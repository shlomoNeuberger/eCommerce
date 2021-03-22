from login.models import GuestEmail
from django.http.response import Http404, HttpResponse
from products.models import Product
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.views import View
from random import randint
from .models import Cart
from orders.models import Order
from billing.models import Address, BillingProfile
from billing.forms import AddressForm
# Create your views here.


def cart_home(request: HttpRequest):
    """Shows the informaton of the cart in the session"""
    cart_obj, _ = Cart.objects.new_or_get(request)
    return render(request, "carts/home.html", {'cart': cart_obj})


def cart_update(request: HttpRequest):
    """function view for """
    cart_obj, _ = Cart.objects.new_or_get(request)
    slug = request.POST.get('product_slug', None)
    action = request.POST.get("remove", None) or request.POST.get("add", None)
    if slug:
        if action:
            product = Product.objects.get(slug=slug)
            cart_obj.products.remove(product)
        elif action:
            product = Product.objects.get(slug=slug)
            cart_obj.products.add(product)
        else:
            return HttpResponse("What are you trying to do", status=500)
    else:
        return HttpResponse("What are you trying to do", status=500)
    products_count = cart_obj.products.count()
    if products_count == 0:
        del request.session['cart_items']
    else:
        request.session['cart_items'] = products_count

    return redirect("cart:home")


class ChackoutView(View):
    """
    This is class based view becuse.
    We need a complete diffrent Behavior
    """

    def get(self, request: HttpRequest):
        # Rendering the chackout view
        cart_obj, created_cart = Cart.objects.new_or_get(request)
        order_obj = None
        bill_profile = None
        if request.user.is_authenticated:
            """Polling the billing from"""
            bill_profile, _ = BillingProfile.objects.get_or_create(
                user=request.user, email=request.user.email)
        elif request.session.get("guest_id", None):
            # Creating a new guest instance
            guest = GuestEmail.objects.get(id=request.session.get("guest_id"))
            # loading biiling profile for known email
            bill_profile, _ = BillingProfile.objects.get_or_create(
                email=guest.email)

        if created_cart or cart_obj.products.count() == 0:
            # this sholdn't happen but is protacting the worst user scanario
            return redirect("cart:home")
        else:
            order_obj, _ = Order.objects.new_or_get(
                cart=cart_obj, billing_profile=bill_profile)
        adress_qs = Address.objects.filter(billing_profile=bill_profile)
        context = {
            'order': order_obj,
            'bill_profile': bill_profile,
            'adress_qs': adress_qs,
        }

        return render(request, "carts/checkout.html", context)

    def post(self, request: HttpRequest):
        billing_profile, _ = BillingProfile.objects.new_or_get(request)
        cart, _ = Cart.objects.new_or_get(request)
        order, _ = Order.objects.new_or_get(billing_profile, cart)
        if order.is_ready():
            trnsaction_result = True  # Do transaction
            order.set_paid()
            print(request.session.values())
            try:
                del request.session['cart_id']
                del request.session['guest_id']
                del request.session['cart_items']
            except:
                pass
            return redirect("cart:done")
        return redirect('cart:chackout')


class ChackoutDone(View):
    def get(self, request: HttpRequest):
        return render(request, 'carts/thank_you.html', {})

    def post(self, request: HttpRequest):
        return render(request, 'carts/thank_you.html', {})
