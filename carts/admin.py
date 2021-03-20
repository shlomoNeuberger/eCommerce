from carts.models import Cart
from django.contrib import admin

# Register your models here.


class CartAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'total']

    class Meta:
        model = Cart


admin.site.register(Cart, CartAdmin)
