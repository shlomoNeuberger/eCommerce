from django.db import models
from django.conf import settings
from django.db.models.signals import post_save, pre_save
# Create your models here.

User = settings.AUTH_USER_MODEL


class BillingProfile(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.deletion.SET_NULL)
    email = models.EmailField(blank=True, null=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    timestemp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.email}"


def user_created_reciver(sender, instance, created, *args, **kwargs):

    if instance.email == '':
        email = "NO mail"
    else:
        email = instance.email
    if created:
        BillingProfile.objects.get_or_create(user=instance, email=email)


def user_cahnged_reciver(sender, instance, *args, **kwargs):
    print(instance)
    qs = BillingProfile.objects.filter(user=instance)
    if qs.count() == 1:
        bill_obj = qs.first()
        bill_obj.email = instance.email
        bill_obj.save()


pre_save.connect(user_cahnged_reciver, sender=User)
post_save.connect(user_created_reciver, sender=User)
