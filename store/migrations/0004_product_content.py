# Generated by Django 5.0.6 on 2024-08-02 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_remove_product_discount_remove_product_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='content',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
