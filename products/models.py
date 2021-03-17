from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.FileField(
        upload_to="image/products/", null=True, blank=True)
