# Generated by Django 5.0.6 on 2024-08-17 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0026_banner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='date_added',
            field=models.DateTimeField(verbose_name='date added'),
        ),
    ]
