from django.db import models
from django.conf import settings
from django.db.models.signals import m2m_changed, pre_save, post_save
from django.db.models.deletion import CASCADE
from django.http.request import HttpRequest
from products.models import Product
import decimal


# Create your models here.
User = settings.AUTH_USER_MODEL


class CartModelManger(models.Manager):
    def new_or_get(self, request: HttpRequest):
        cart_id = request.session.get("cart_id", None)
        cart_obj, is_created = Cart.objects.get_or_create(id=cart_id)
        if not is_created and request.user.is_authenticated:
            cart_obj.user = request.user
            cart_obj.save()
        return cart_obj, is_created


class Cart(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    subtotal = models.DecimalField(
        default=0.00, max_digits=5, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=7, decimal_places=2)
    discount = models.DecimalField(
        default=0.00, max_digits=5, decimal_places=0)
    updated = models.DateTimeField(null=True, blank=True,)
    timestemp = models.DateTimeField(auto_now_add=True)

    objects = CartModelManger()

    def __str__(self) -> str:
        return f"{self.id}"


def pre_save_cart_reciver(sender, instance: Cart, action, *args, **kwargs):
    if "post" in action:
        products = instance.products.all()
        subtotal = 0
        for product in products:
            subtotal += product.price
        instance.subtotal = subtotal
        instance.save()


def pre_save_cart_total_reciver(sender, instance: Cart, *args, **kwargs):
    if instance.total != instance.subtotal:
        instance.total = instance.subtotal
        instance.save()


m2m_changed.connect(pre_save_cart_reciver, sender=Cart.products.through)
pre_save.connect(pre_save_cart_total_reciver, sender=Cart)
