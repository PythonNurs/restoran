# Generated by Django 3.1.3 on 2020-11-30 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodcategory',
            name='title',
            field=models.CharField(db_index=True, max_length=255, verbose_name='Категорий кухни'),
        ),
    ]
