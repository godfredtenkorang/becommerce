# Generated by Django 5.0.6 on 2024-10-23 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_coupon_discount_percentage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='discount_percentage',
            field=models.IntegerField(),
        ),
    ]