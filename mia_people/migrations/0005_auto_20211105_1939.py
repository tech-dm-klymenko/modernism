# Generated by Django 3.1.13 on 2021-11-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mia_people", "0004_auto_20211105_1359"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="last_name",
            field=models.CharField(
                help_text="You can add a company name here too if appropriate.",
                max_length=250,
                unique=True,
            ),
        ),
        migrations.AlterField(
            model_name="person",
            name="slug",
            field=models.SlugField(blank=True, max_length=254),
        ),
    ]
