from ecommerce.utils import unique_order_generator
from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from carts.models import Cart
from django.db.models.signals import post_save, pre_save
from math import fabs, fsum
from billing.models import Address, BillingProfile
# Create your models here.

ORDERS_STATUS_CHOICES = (
    ('created', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
    ('cancel', 'Cancel'),
)


class OrderManager(models.Manager):
    def new_or_get(self, billing_profile: BillingProfile, cart: Cart):
        created = False
        qs = self.get_queryset().filter(
            billing_profile=billing_profile,
            cart=cart,
            active=True,
            status="created"
        )
        if qs.count() >= 1:
            obj = qs.first()
            qs.update(active=False)
            obj.active = True
            obj.save()
        else:
            obj, created = self.model.objects.get_or_create(
                billing_profile=billing_profile,
                cart=cart,
                active=True,
                status="created"
            )
        return obj, created


class Order(models.Model):
    order_id = models.CharField(max_length=120, blank=True, unique=True)
    shipping_address = models.ForeignKey(
        Address, related_name="shpping_address", blank=True, null=True, on_delete=SET_NULL)
    billing_address = models.ForeignKey(
        Address, related_name="billing_address", blank=True, null=True, on_delete=SET_NULL)
    cart = models.ForeignKey(Cart, on_delete=SET_NULL, null=True)
    status = models.CharField(
        max_length=120, default='created', choices=ORDERS_STATUS_CHOICES)
    total = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    shipping_total = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2)
    billing_profile = models.ForeignKey(
        BillingProfile, null=True, on_delete=SET_NULL)
    active = models.BooleanField(default=True)

    objects = OrderManager()

    def __str__(self) -> str:
        return f'{self.order_id}'

    def update_total(self):
        total = self.cart.total
        shipping_total = self.shipping_total
        new_total = fsum([total, shipping_total])
        self.total = new_total
        self.save()
        return new_total

    def is_ready(self):
        shipping_address = self.shipping_address
        billing_address = self.billing_address
        billing_profile = self.billing_profile
        cart = self.cart
        total = self.total
        if shipping_address and billing_address and billing_profile and cart and total:
            return True
        else:
            return False

    def set_paid(self):
        if self.is_ready():
            self.status = "paid"
            self.save()

def Order_pre_save_orderID_gen(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_generator(instance)


def post_save_update_order(sender, instance, *args, **kwargs):
    cart_obj = instance
    cart_id = cart_obj.id

    qs = Order.objects.filter(cart__id=cart_id)
    if qs.count() == 1:
        order_obj = qs.first()
        order_obj.update_total()


def post_save_order(sender, instance, created, *args, **kwargs):
    if created:
        instance.update_total()


pre_save.connect(Order_pre_save_orderID_gen, sender=Order)
post_save.connect(post_save_update_order, sender=Cart)
post_save.connect(post_save_order, sender=Order)
