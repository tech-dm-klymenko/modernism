# Generated by Django 3.1.8 on 2021-06-30 20:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("facts", "0002_factpage_categories"),
    ]

    operations = [
        migrations.RemoveField(model_name="factpage", name="category",),
    ]
