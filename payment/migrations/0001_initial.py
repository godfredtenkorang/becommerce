# Generated by Django 5.1.7 on 2025-04-10 08:41

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=255)),
                ('shipping_address', models.TextField(max_length=10000)),
                ('amount_paid', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date_ordered', models.DateTimeField(null=True, verbose_name='date ordered')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Orders',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('Order Placed', 'Order Placed'), ('Waiting to be Shipped', 'Waiting to be Shipped'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], default='Order Placed', max_length=50)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='payment.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Order Items',
                'ordering': ['-date_added'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=300)),
                ('email', models.EmailField(default='', max_length=255)),
                ('address', models.CharField(default='', max_length=300)),
                ('phone_number', models.CharField(default=0, max_length=20)),
                ('country', models.CharField(default='Ghana', max_length=20)),
                ('city', models.CharField(default='', max_length=255)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=255, null=True)),
                ('amount', models.PositiveBigIntegerField(default=0)),
                ('ref', models.CharField(max_length=200)),
                ('verified', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=255)),
                ('address', models.CharField(max_length=300)),
                ('phone_number', models.CharField(default=0, max_length=20)),
                ('country', models.CharField(default='Ghana', max_length=20)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Shipping Address',
            },
        ),
    ]
