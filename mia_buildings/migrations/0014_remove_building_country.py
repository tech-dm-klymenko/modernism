# Generated by Django 3.1.13 on 2021-11-07 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mia_buildings", "0013_auto_20211105_1939"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="building",
            name="country",
        ),
    ]
