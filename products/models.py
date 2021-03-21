from django.db import models
from django.db.models import Q
from django.db.models.signals import pre_save
from ecommerce.utils import upload_image_path, unique_slug_generator
# Create your models here.


class ProductQuerySet(models.query.QuerySet):
    def active(self, *args, **kwargs):
        return self.filter(active=True)

    def featured(self, *args, **kwargs):
        return self.filter(featured=True)

    def search(self, query, *args, **kwargs):
        lookup = Q(description__icontains=query) | Q(
            title__icontains=query) | Q(tag__title__icontains=query)
        return self.filter(lookup).distinct()


class ProductManger(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def featured(self, *args, **kwargs):
        return self.get_queryset().featured()

    def search(self, query, *args, **kwargs):
        lookup = Q(description__icontains=query) | Q(
            title__icontains=query) | Q(tag__title__icontains=query)
        return self.filter(lookup).distinct()


class Product(models.Model):
    slug = models.SlugField(blank=True, null=True, unique=True)
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(
        upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    objects = ProductManger()

    def __str__(self) -> str:
        return f"{self.title}"

    def get_tags(self):
        return self.tag_set.all()


def product_pre_save_reciver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_reciver, sender=Product)
