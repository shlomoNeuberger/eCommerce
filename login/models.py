from django.db import models

# Create your models here.


class GuestEmail(models.Model):
    email = models.EmailField(blank=True, null=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    timestemp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.email}"
