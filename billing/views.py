from carts.models import Cart
from orders.models import Order
from billing.models import BillingProfile
from billing.forms import AddressForm
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.utils.http import is_safe_url
# Create your views here.


def create_shipping_add(request: HttpRequest):
    if is_safe_url(request.POST.get("next_", None), request.get_host()):
        next_path = request.POST.get("next_", None)
    else:
        next_path = None
    form = AddressForm(request.POST or None)
    if form.is_valid():
        add = form.save(commit=False)
        add.address_type = request.POST.get('type', 'shipping')
        billing_profile, _ = BillingProfile.objects.new_or_get(request)
        if billing_profile is None:
            return redirect("cart:chackout")
        else:
            add.billing_profile = billing_profile
            cart_obj, created_cart = Cart.objects.new_or_get(request)
            order_obj, _ = Order.objects.new_or_get(
                cart=cart_obj, billing_profile=billing_profile)
            if add.address_type == 'shipping':
                order_obj.shipping_address = add
            else:
                order_obj.billing_address = add
            add.save()
            order_obj.save()
            if next_path is not None and next_path != "None":
                return redirect(next_path)
    return redirect("main")
