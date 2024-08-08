# Generated by Django 5.0.6 on 2024-08-06 11:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_alter_product_description1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200, null=True)),
                ('description1', models.CharField(blank=True, default='', max_length=250)),
                ('description2', models.CharField(blank=True, default='', max_length=250)),
                ('description3', models.CharField(blank=True, default='', max_length=250)),
                ('description4', models.CharField(blank=True, default='', max_length=250)),
                ('description5', models.CharField(blank=True, default='', max_length=250)),
                ('description6', models.CharField(blank=True, default='', max_length=250)),
                ('description7', models.CharField(blank=True, default='', max_length=250)),
                ('brand', models.CharField(default='un-branded')),
                ('image1', models.ImageField(default='default.jpg', upload_to='product1/img')),
                ('image2', models.ImageField(default='default.jpg', upload_to='product2/img')),
                ('image3', models.ImageField(default='default.jpg', upload_to='product3/img')),
                ('normal_price', models.DecimalField(decimal_places=2, max_digits=4, null=True)),
                ('final_price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=250, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop', to='store.category')),
            ],
            options={
                'verbose_name_plural': 'shops',
                'ordering': ['date_added'],
            },
        ),
    ]
