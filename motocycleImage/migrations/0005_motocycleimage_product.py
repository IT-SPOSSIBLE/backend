# Generated by Django 5.1.7 on 2025-06-19 04:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('motocycleImage', '0004_remove_motocycleimage_moto'),
        ('product', '0003_alter_product_price_alter_product_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='motocycleimage',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.product'),
            preserve_default=False,
        ),
    ]
