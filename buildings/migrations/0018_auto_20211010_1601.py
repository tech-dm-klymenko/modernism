# Generated by Django 3.1.13 on 2021-10-10 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0023_add_choose_permissions"),
        ("buildings", "0017_buildingpage_search_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="buildingsindexpage",
            name="search_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Search image",
            ),
        ),
        migrations.AddField(
            model_name="placesindexpage",
            name="search_image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
                verbose_name="Search image",
            ),
        ),
    ]
