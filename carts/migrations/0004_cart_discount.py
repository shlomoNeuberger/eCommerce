# Generated by Django 3.1.7 on 2021-03-20 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0003_cart_subtotal'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='discount',
            field=models.IntegerField(default=0),
        ),
    ]