# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-30 07:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0010_auto_20170530_0623'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tests',
            old_name='quantity',
            new_name='tdr',
        ),
        migrations.RemoveField(
            model_name='tests',
            name='product',
        ),
    ]