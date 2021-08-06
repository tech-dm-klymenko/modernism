# Generated by Django 3.1.12 on 2021-08-06 21:11

from django.db import migrations, models
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ("facts", "0004_architectuniversity"),
        ("people", "0004_auto_20210806_1806"),
    ]

    operations = [
        migrations.AddField(
            model_name="personpage",
            name="universities",
            field=modelcluster.fields.ParentalManyToManyField(
                blank=True, related_name="universities", to="facts.ArchitectUniversity"
            ),
        ),
        migrations.AlterField(
            model_name="professorpage",
            name="architect_mentors",
            field=modelcluster.fields.ParentalManyToManyField(
                blank=True, related_name="professors", to="people.ArchitectPage"
            ),
        ),
        migrations.AlterField(
            model_name="professorpage",
            name="is_active_architect",
            field=models.BooleanField(
                default=False,
                help_text="Is/Was the professor active as modernist architect?",
            ),
        ),
    ]
