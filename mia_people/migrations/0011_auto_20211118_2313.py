# Generated by Django 3.2.9 on 2021-11-18 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mia_people", "0010_alter_person_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="architect",
            name="is_developer",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="architect",
            name="is_professor",
            field=models.BooleanField(default=False),
        ),
    ]
