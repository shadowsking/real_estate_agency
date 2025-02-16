# Generated by Django 2.2.24 on 2023-10-22 16:32

from django.db import migrations


def fill_from_construction_year(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats_in_new_buildings = Flat.objects.filter(construction_year__gte=2015)
    flats_in_new_buildings.update(new_building=True)

    flats_in_secondary = Flat.objects.filter(construction_year__lt=2015)
    flats_in_secondary.update(new_building=False)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(fill_from_construction_year)
    ]
