# Generated by Django 3.2 on 2023-10-23 02:24

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0006_flat_liked_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None, verbose_name='Нормализованный номер владельца'),
        ),
    ]
