# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-16 15:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0012_post_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default='', max_length=120),
        ),
    ]
