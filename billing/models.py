from login.models import GuestEmail
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.signals import post_save, pre_save
# Create your models here.

User = settings.AUTH_USER_MODEL


class BillingProfileManger(models.Manager):
    def new_or_get(self, request):
        user = request.user
        guest_email = request.session.get("guest_id")
        created = False
        obj = None
        if user.is_authenticated:
            email = user.email
            obj, created = self.model.objects.get_or_create(
                user=user, email=email)
        elif guest_email:
            guest = GuestEmail.objects.get(id=guest_email)
            obj, created = self.model.objects.get_or_create(
                email=guest.email)
        else:
            pass
        return obj, created


class BillingProfile(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.deletion.SET_NULL)
    email = models.EmailField(blank=True, null=True)
    update = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    timestemp = models.DateTimeField(auto_now_add=True)

    objects = BillingProfileManger()

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

ADDRESS_TYPE = (
    ('billing', 'Billinh'),
    ('shipping', 'Shipping')
)


class Address(models.Model):
    billing_profile = models.ForeignKey(BillingProfile, on_delete=CASCADE)
    address_type = models.CharField(max_length=100, choices=ADDRESS_TYPE)
    address_line_1 = models.CharField(max_length=100)
    address_line_2 = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)

    def __str__(self) -> str:
        return f"{self.billing_profile}"
