# Generated by Django 3.1.3 on 2020-12-03 08:23

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0004_auto_20201130_1702'),
        ('departmants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='music',
            field=models.CharField(default=1, max_length=255, verbose_name='Музыка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='parking',
            field=models.CharField(default=1, max_length=255, verbose_name='Парковка'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='department',
            name='phone_of_department',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='department',
            name='food',
            field=models.ManyToManyField(blank=True, related_name='department_food', to='foods.FoodCategory', verbose_name='Кухня'),
        ),
        migrations.AlterField(
            model_name='department',
            name='seats',
            field=models.PositiveIntegerField(blank=True, default=0, null=True, verbose_name='Количество мест'),
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(verbose_name='Дата')),
                ('people', models.PositiveIntegerField(verbose_name='Число людей')),
                ('number', models.CharField(blank=True, max_length=255, null=True, validators=[django.core.validators.RegexValidator(message='Телефон должен быть в формате +996[код][номер]', regex='^(\\+996)\\d{9}$')], verbose_name='Телефон')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to='departmants.department', verbose_name='Место расположения')),
            ],
        ),
    ]
