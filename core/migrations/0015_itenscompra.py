# Generated by Django 5.1.4 on 2024-12-15 13:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0014_compra"),
    ]

    operations = [
        migrations.CreateModel(
            name="ItensCompra",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("quantidade", models.IntegerField(default=1)),
                (
                    "compra",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="itens", to="core.compra"
                    ),
                ),
                (
                    "livro",
                    models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name="+", to="core.livro"),
                ),
            ],
        ),
    ]
