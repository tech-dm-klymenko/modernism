# Generated by Django 3.2.15 on 2022-08-14 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mia_buildings", "0019_building_seo_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="building",
            name="published_on_twitter",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
