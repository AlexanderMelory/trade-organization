# Generated by Django 5.0.1 on 2024-01-08 10:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Фамилия')),
                ('birth_date', models.DateField(default=datetime.datetime(1994, 1, 15, 10, 37, 24, 750362, tzinfo=datetime.timezone.utc), verbose_name='Дата рождения')),
                ('gender', models.IntegerField(choices=[(1, 'Мужчина'), (2, 'Женщина')], default=1, verbose_name='Пол')),
                ('position', models.CharField(default='Руководитель', max_length=256, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Руководитель',
                'verbose_name_plural': 'Руководители',
                'ordering': ('-first_name',),
            },
        ),
        migrations.CreateModel(
            name='Trader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=256, null=True, verbose_name='Фамилия')),
                ('birth_date', models.DateField(default=datetime.datetime(1994, 1, 15, 10, 37, 24, 750362, tzinfo=datetime.timezone.utc), verbose_name='Дата рождения')),
                ('gender', models.IntegerField(choices=[(1, 'Мужчина'), (2, 'Женщина')], default=1, verbose_name='Пол')),
                ('position', models.CharField(default='Продавец', max_length=256, verbose_name='Должность')),
            ],
            options={
                'verbose_name': 'Продавец',
                'verbose_name_plural': 'Продавцы',
                'ordering': ('-first_name',),
            },
        ),
    ]
