# Generated by Django 3.1.8 on 2021-06-30 20:24

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('facts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='factpage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, related_name='fact', to='facts.FactCategory'),
        ),
    ]
