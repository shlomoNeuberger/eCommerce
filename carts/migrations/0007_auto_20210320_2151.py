# Generated by Django 3.1.7 on 2021-03-20 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0006_auto_20210320_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]