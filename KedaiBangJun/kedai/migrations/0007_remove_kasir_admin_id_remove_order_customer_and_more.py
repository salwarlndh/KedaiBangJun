# Generated by Django 5.1.2 on 2024-11-29 05:42

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("kedai", "0005_remove_product_stock_customer_admin_kasir_admin_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="customer",
        ),
        migrations.RemoveField(
            model_name="order",
            name="payment_method",
        ),
        migrations.RemoveField(
            model_name="order",
            name="product",
        ),
        migrations.AddField(
            model_name="order",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="order",
            name="customer_name",
            field=models.CharField(default="Unknown Customer", max_length=100),
        ),
        migrations.AddField(
            model_name="order",
            name="price",
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name="order",
            name="product_id",
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name="order",
            name="product_name",
            field=models.CharField(default="default product", max_length=100),
        ),
        migrations.AddField(
            model_name="order",
            name="total",
            field=models.FloatField(default=0.0, editable=False),
        ),
        migrations.AlterField(
            model_name="order",
            name="quantity",
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[("Waiting", "Waiting"), ("Served", "Served")],
                default="Waiting",
                max_length=10,
            ),
        ),
    ]
