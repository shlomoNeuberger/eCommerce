from django.db import models
from django.db.models.signals import pre_save
from ecommerce.utils import unique_slug_generator
from products.models import Product
# Create your models here.


class Tag(models.Model):
    slug = models.SlugField(blank=True, null=True)
    title = models.CharField(max_length=120)
    timestemp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    products = models.ManyToManyField(Product, blank=True)

    def __str__(self) -> str:
        return f'{self.title}'


def tag_pre_save_reciver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(tag_pre_save_reciver, sender=Tag)
