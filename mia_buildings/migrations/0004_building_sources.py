# Generated by Django 3.1.13 on 2021-10-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mia_facts", "0002_author_source"),
        ("mia_buildings", "0003_auto_20211023_1752"),
    ]

    operations = [
        migrations.AddField(
            model_name="building",
            name="sources",
            field=models.ManyToManyField(blank=True, to="mia_facts.Source"),
        ),
    ]
