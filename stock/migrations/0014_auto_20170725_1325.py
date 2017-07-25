# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-07-25 13:25
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0013_auto_20170721_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reporter',
            name='phone_number',
            field=models.CharField(blank=True, help_text='The telephone to contact you.', max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number in the format: '+25799999999'. Up to 15 digits allowed.", regex=b'^\\+?1?\\d{9,15}$')], verbose_name='Reporter telephone'),
        ),
        migrations.AlterField(
            model_name='reporter',
            name='supervisor_phone_number',
            field=models.CharField(blank=True, help_text='The telephone to contact you.', max_length=16, validators=[django.core.validators.RegexValidator(message="Phone number in the format: '+25799999999'. Up to 15 digits allowed.", regex=b'^\\+?1?\\d{9,15}$')], verbose_name='Supervisor phone'),
        ),
    ]
