# Generated by Django 5.0.4 on 2024-04-30 08:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("category", "0001_initial"),
        ("products", "0005_alter_product_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="category.category",
            ),
        ),
    ]