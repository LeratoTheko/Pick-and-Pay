# Generated by Django 5.2 on 2025-04-11 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pay', '0002_alter_product_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='subcategory',
            field=models.CharField(choices=[('Refrigerators & Freezers', 'Refrigerators & Freezers'), ('Microwaves', 'Microwaves'), ('Ovens & Stoves', 'Ovens & Stoves'), ('Dishwashers', 'Dishwashers'), ('Blenders & Juicers', 'Blenders & Juicers'), ('Toasters & Sandwich Makers', 'Toasters & Sandwich Makers'), ('Coffee Machines & Kettles', 'Coffee Machines & Kettles'), ('Food Processors', 'Food Processors'), ('Washing Machines', 'Washing Machines'), ('Tumble Dryers', 'Tumble Dryers'), ('Steam Irons & Garment Steamers', 'Steam Irons & Garment Steamers'), ('Air Conditioners', 'Air Conditioners'), ('Fans', 'Fans'), ('Heaters', 'Heaters'), ('Electric Blankets', 'Electric Blankets')], max_length=100),
        ),
    ]
