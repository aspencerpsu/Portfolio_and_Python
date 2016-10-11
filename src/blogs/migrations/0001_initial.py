# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import datetime
import blogs.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filetype', models.CharField(unique=True, max_length=5)),
                ('topic', models.CharField(max_length=100)),
                ('abstract', models.TextField(max_length=2000)),
                ('datestamp', models.DateField(default=datetime.date.today)),
                ('timestamp', models.TimeField(default=django.utils.timezone.now)),
                ('content', models.FileField(upload_to=b'/weeklyProject/%Y/%m/')),
                ('figures', models.ImageField(upload_to=b'/img')),
                ('graphs', models.FileField(upload_to=blogs.models.fileback)),
            ],
        ),
    ]
