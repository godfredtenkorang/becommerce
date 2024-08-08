# Generated by Django 5.0.6 on 2024-08-06 20:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_laptopsandtablet_remove_homeshop_homecategory_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='laptopsandtablet',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='laptop', to='store.category'),
        ),
    ]