from django.db import models
from carts.models import Cart
from orders.models import Order
from billing.models import Address, BillingProfile
from billing.forms import AddressForm
from django.shortcuts import redirect, render
from django.http import HttpRequest
from django.utils.http import is_safe_url
# Create your views here.


def create_shipping_add(request: HttpRequest):
    """
    A baics function view for handlig the post data
    of adding a new adrresss
    """

    # this is for returning to the calling page
    if is_safe_url(request.POST.get("next_", None), request.get_host()):
        next_path = request.POST.get("next_", None)
    else:
        next_path = None
    # using a model form for verifing the feilds
    form = AddressForm(request.POST or None)
    if form.is_valid():
        # if valid we create a new address filed
        add = form.save(commit=False)

    elif request.POST.get("radioBtns", None):
        # if user choosed an old address from the side view
        bill_pro, _ = BillingProfile.objects.new_or_get(request)
        try:
            add = Address.objects.get_or_create(id=request.POST.get("radioBtns"),
                                                billing_profile=bill_pro)
        except models.Model.DoesNotExist as e:
            print(f"id{request.POST.get('radioBtns')} not found")
            return redirect(next_path or "main")
        except:
            print(f"Unknow error post data {request.POST.get('radioBtns')}")
            return redirect(next_path or "main")

    else:
        # if no inforamtion is valid for creation return old page
        return redirect(next_path)
    add.address_type = request.POST.get('type', 'shipping')
    billing_profile, _ = BillingProfile.objects.new_or_get(request)
    if billing_profile is None:
        return redirect("cart:chackout")

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
