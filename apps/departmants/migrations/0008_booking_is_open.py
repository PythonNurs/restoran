# Generated by Django 3.1.3 on 2020-12-01 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departmants', '0007_remove_booking_open'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
    ]