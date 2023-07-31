# Generated by Django 4.2.3 on 2023-07-30 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(through='carts.CartProducts', to='product.product'),
        ),
    ]