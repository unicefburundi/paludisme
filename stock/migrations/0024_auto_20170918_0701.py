# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-18 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0023_auto_20170915_0822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='category',
            field=models.CharField(choices=[(b'REG', 'Registering'), (b'SF', 'Final Stock'), (b'SD', 'Stock debut de semaine'), (b'SR', 'Stock Received'), (b'RP', 'Rupture'), (b'CA', 'Cases'), (b'TS', 'Test'), (b'HBC', 'Repports on cases'), (b'HBD', 'Reports on death')], max_length=3),
        ),
    ]