from ecommerce.utils import unique_order_generator
from django.db import models
from django.db.models.deletion import SET_NULL
from carts.models import Cart
from django.db.models.signals import post_save, pre_save
# Create your models here.

ORDERS_STATUS_CHOICES = (
    ('created', 'Creared'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
    ('cancel', 'Cancel'),
)


class Order(models.Model):
    order_id = models.CharField(max_length=120, blank=True, unique=True)
    cart = models.ForeignKey(Cart, on_delete=SET_NULL, null=True)
    status = models.CharField(
        max_length=120, default='created', choices=ORDERS_STATUS_CHOICES)
    total = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    shipping_total = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2)

    def __str__(self) -> str:
        return self.order_id

    def update_total(self):
        total = self.cart.total
        shipping_total = self.shipping_total
        new_total = total + shipping_total
        self.total = new_total
        self.save()
        return new_total


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
