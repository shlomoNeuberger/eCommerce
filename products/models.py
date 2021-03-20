from django.db import models
from ecommerce.utils import upload_image_path
# Create your models here.


class ProductManger(models.Manager):
    def featured(self, *args, **kwargs):
        return self.get_queryset().filter(featured=True)


class Product(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.ImageField(
        upload_to=upload_image_path, null=True, blank=True)
    featured = models.BooleanField(default=False)

    objects = ProductManger()

    def __str__(self) -> str:
        return f"{self.title}"
