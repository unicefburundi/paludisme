# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-29 12:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0003_auto_20170329_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockproduct',
            name='reporting_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]