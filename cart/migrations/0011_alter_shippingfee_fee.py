# Generated by Django 5.0.6 on 2024-10-23 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0010_alter_shippingfee_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingfee',
            name='fee',
            field=models.CharField(max_length=10),
        ),
    ]
