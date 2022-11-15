# Generated by Django 4.1.3 on 2022-11-14 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0012_catalog_quantity"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="catalog",
            name="quantity",
        ),
        migrations.AddField(
            model_name="orderitem",
            name="quantity",
            field=models.IntegerField(default=1, verbose_name="Количество"),
        ),
    ]
