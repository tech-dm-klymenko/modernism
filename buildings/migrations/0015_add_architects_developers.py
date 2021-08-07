# Generated by Django 3.1.12 on 2021-08-07 08:49

from django.db import migrations


def add_people_to_fields(apps, schema_editor):
    BuildingPage = apps.get_model("buildings", "BuildingPage")
    building_pages = BuildingPage.objects.all()

    for page in building_pages:
        architects_relations = page.architects.all()
        developers_relations = page.developers.all()
        for arch_rel in architects_relations:
            arch_rel.architect.related_buildings.add(page)

        for dev_rel in developers_relations:
            dev_rel.developer.related_buildings.add(page)

        page.save()


def do_nothing_reverse_function(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ("buildings", "0014_auto_20210807_0843"),
    ]

    operations = [
        migrations.RunPython(add_people_to_fields, do_nothing_reverse_function),
    ]
