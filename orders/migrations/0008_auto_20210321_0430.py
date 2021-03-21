# Generated by Django 3.1.7 on 2021-03-21 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20210321_0353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('created', 'Created'), ('paid', 'Paid'), ('shipped', 'Shipped'), ('refunded', 'Refunded'), ('cancel', 'Cancel')], default='created', max_length=120),
        ),
    ]
