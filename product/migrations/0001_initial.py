# Generated by Django 4.2.3 on 2023-07-30 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='product/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
