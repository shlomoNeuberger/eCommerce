# Generated by Django 3.1.7 on 2021-03-17 16:38

from django.db import migrations, models
import ecommerce.utils


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210317_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=ecommerce.utils.upload_image_path),
        ),
    ]
