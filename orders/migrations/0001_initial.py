# Generated by Django 3.1.7 on 2021-03-20 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carts', '0006_auto_20210320_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordert_id', models.CharField(blank=True, max_length=120)),
                ('status', models.CharField(choices=[('created', 'Creared'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('refunded', 'Refunded'), ('cancel', 'Cancel')], default='created', max_length=120)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('shipping_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=7)),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='carts.cart')),
            ],
        ),
    ]