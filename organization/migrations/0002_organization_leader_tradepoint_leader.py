# Generated by Django 5.0.1 on 2024-01-08 11:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
        ('stuff', '0002_alter_leader_birth_date_alter_trader_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='organizations', to='stuff.leader', verbose_name='Руководитель'),
        ),
        migrations.AddField(
            model_name='tradepoint',
            name='leader',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='trade_points', to='stuff.leader', verbose_name='Руководитель'),
        ),
    ]
