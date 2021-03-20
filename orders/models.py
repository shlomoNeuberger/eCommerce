from ecommerce.utils import unique_order_generator
from django.db import models
from django.db.models.deletion import SET_NULL
from carts.models import Cart
from django.db.models.signals import pre_save
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


def product_pre_save_reciver(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.order_id = unique_order_generator(instance)


pre_save.connect(product_pre_save_reciver, Order)
