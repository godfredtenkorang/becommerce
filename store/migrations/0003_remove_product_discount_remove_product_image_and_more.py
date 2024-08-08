# Generated by Django 5.0.6 on 2024-08-02 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_rename_price_product_final_price_product_discount_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AddField(
            model_name='product',
            name='image1',
            field=models.ImageField(default='default.jpg', upload_to='product1/img'),
        ),
        migrations.AddField(
            model_name='product',
            name='image2',
            field=models.ImageField(default='default.jpg', upload_to='product2/img'),
        ),
        migrations.AddField(
            model_name='product',
            name='image3',
            field=models.ImageField(default='default.jpg', upload_to='product3/img'),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=250, unique=True),
        ),
    ]