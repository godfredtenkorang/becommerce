# Generated by Django 5.0.6 on 2024-08-11 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0013_alter_orderitem_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='status',
            field=models.CharField(choices=[('Order Placed', 'Order Placed'), ('Waiting to be Shipped', 'Waiting to be Shipped'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered')], default='Order Placed', max_length=50),
        ),
    ]
