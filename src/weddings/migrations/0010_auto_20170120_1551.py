# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-01-20 20:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('weddings', '0009_auto_20170120_1514'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wedding',
            name='age',
        ),
        migrations.RemoveField(
            model_name='wedding',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='wedding',
            name='meet',
        ),
        migrations.RemoveField(
            model_name='wedding',
            name='name',
        ),
        migrations.RemoveField(
            model_name='wedding',
            name='whoyouare',
        ),
        migrations.RemoveField(
            model_name='wedding',
            name='width_field',
        ),
        migrations.RemoveField(
            model_name='wedding',
            name='zodiacsign',
        ),
    ]
