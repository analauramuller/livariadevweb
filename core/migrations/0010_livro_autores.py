# Generated by Django 5.1.4 on 2024-12-07 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0009_autor"),
    ]

    operations = [
        migrations.AddField(
            model_name="livro",
            name="autores",
            field=models.ManyToManyField(blank=True, related_name="livros", to="core.autor"),
        ),
    ]
