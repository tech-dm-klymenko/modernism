# Generated by Django 3.2.9 on 2022-01-02 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mia_facts", "0008_auto_20211118_2231"),
    ]

    operations = [
        migrations.AlterField(
            model_name="city",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
