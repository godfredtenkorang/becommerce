# Generated by Django 5.0.6 on 2024-08-02 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_product_description1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description1',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='description2',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='description3',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='description4',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='description5',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='description6',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='product',
            name='description7',
            field=models.CharField(blank=True, default='', max_length=250),
        ),
    ]
