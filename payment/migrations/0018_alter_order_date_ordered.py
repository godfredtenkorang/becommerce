# Generated by Django 5.0.6 on 2024-08-17 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0017_rename_client_order_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(verbose_name='date ordered'),
        ),
    ]
