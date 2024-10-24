# Generated by Django 5.0.6 on 2024-10-24 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_alter_shippingfee_fee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shippingfee',
            old_name='country',
            new_name='region',
        ),
        migrations.AlterField(
            model_name='shippingfee',
            name='fee',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]