# Generated by Django 5.0.6 on 2024-11-12 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0017_alter_shippingfee_fee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingfee',
            name='fee',
            field=models.CharField(max_length=10),
        ),
    ]
