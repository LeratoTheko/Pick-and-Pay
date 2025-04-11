# Generated by Django 5.2 on 2025-04-10 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('category', models.CharField(choices=[('groceries', 'Groceries'), ('electronics', 'Electronics'), ('clothing', 'Clothing')], max_length=50)),
                ('stock', models.PositiveIntegerField()),
                ('image', models.ImageField(null=True, upload_to='product_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
