# Generated by Django 3.1.13 on 2021-11-13 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mia_people", "0008_auto_20211113_1916"),
    ]

    operations = [
        migrations.RemoveField(model_name="person", name="place_of_birth",),
        migrations.RemoveField(model_name="person", name="place_of_death",),
    ]
