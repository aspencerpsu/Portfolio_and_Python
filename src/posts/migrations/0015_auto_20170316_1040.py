# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-16 15:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0014_auto_20170316_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(default='None At The Moment', max_length=120),
        ),
    ]
