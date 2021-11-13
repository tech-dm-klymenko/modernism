# Generated by Django 3.1.13 on 2021-11-07 20:52

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ("mia_buildings", "0014_remove_building_country"),
        ("mia_facts", "0005_auto_20211105_1933"),
    ]

    operations = [
        migrations.RemoveField(model_name="city", name="description",),
        migrations.RemoveField(model_name="university", name="country",),
        migrations.AlterField(
            model_name="city",
            name="country",
            field=django_countries.fields.CountryField(max_length=2, null=True),
        ),
        migrations.DeleteModel(name="Country",),
    ]
