# Generated by Django 5.1.4 on 2025-01-11 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_remove_item_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='shop/placeholder_product.jpeg', upload_to='shop/'),
        ),
    ]