# Generated by Django 3.1.3 on 2020-12-06 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('departmants', '0007_auto_20201203_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='parking',
            field=models.CharField(choices=[('F', 'Парковка неохраняемая, бесплатная'), ('Pay', 'Парковка охраняемая, небесплатная'), ('Not', 'Парковки нет')], max_length=255, verbose_name='Парковка'),
        ),
    ]
