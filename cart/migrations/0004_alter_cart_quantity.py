# Generated by Django 5.0.4 on 2024-05-02 09:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cart", "0003_alter_cart_quantity"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cart",
            name="quantity",
            field=models.IntegerField(default=1, null=True),
        ),
    ]
