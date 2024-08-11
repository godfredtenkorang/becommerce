# Generated by Django 5.0.6 on 2024-08-10 01:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_payment_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='order_item',
        ),
        migrations.AddField(
            model_name='payment',
            name='shipping',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.shippingaddress'),
        ),
    ]
