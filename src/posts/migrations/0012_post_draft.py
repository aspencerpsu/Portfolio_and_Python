# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-15 04:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_remove_post_draft'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
    ]
