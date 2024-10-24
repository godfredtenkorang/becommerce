# Generated by Django 5.0.6 on 2024-10-22 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_alter_applesystem_product_availability_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applesystem',
            name='brand',
            field=models.CharField(default='un-branded', max_length=100),
        ),
        migrations.AlterField(
            model_name='componentsandparts',
            name='brand',
            field=models.CharField(default='un-branded', max_length=100),
        ),
        migrations.AlterField(
            model_name='computeraccessories',
            name='brand',
            field=models.CharField(default='un-branded', max_length=100),
        ),
        migrations.AlterField(
            model_name='gaminglaptops',
            name='brand',
            field=models.CharField(default='un-branded', max_length=100),
        ),
        migrations.AlterField(
            model_name='heelsandslippers',
            name='brand',
            field=models.CharField(default='un-branded', max_length=100),
        ),
        migrations.AlterField(
            model_name='laptopsandtablet',
            name='brand',
            field=models.CharField(default='un-branded', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(default='un-branded', max_length=100),
        ),
        migrations.AlterField(
            model_name='shoesandslippers',
            name='brand',
            field=models.CharField(default='un-branded', max_length=100),
        ),
        migrations.AlterField(
            model_name='surveillancesystems',
            name='brand',
            field=models.CharField(default='un-branded', max_length=100),
        ),
    ]
