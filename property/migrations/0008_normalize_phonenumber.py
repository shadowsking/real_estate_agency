# Generated by Django 3.2 on 2023-10-23 02:33

from django.db import migrations
import phonenumbers


def normalize_phone_numbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        parsed_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if not phonenumbers.is_valid_number(parsed_number):
            continue

        flat.owner_pure_phone = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)

    Flat.objects.bulk_update(flats, ['owner_pure_phone'])


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(normalize_phone_numbers)
    ]
