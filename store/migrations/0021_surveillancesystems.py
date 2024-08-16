# Generated by Django 5.0.6 on 2024-08-16 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_componentsandparts'),
    ]

    operations = [
        migrations.CreateModel(
            name='SurveillanceSystems',
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
                ('normal_price', models.PositiveBigIntegerField(null=True)),
                ('final_price', models.PositiveBigIntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(max_length=250, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='surveillance', to='store.category')),
            ],
            options={
                'verbose_name_plural': 'Surveillance Systems',
                'ordering': ['date_added'],
            },
        ),
    ]
