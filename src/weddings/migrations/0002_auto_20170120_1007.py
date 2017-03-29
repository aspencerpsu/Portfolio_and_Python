# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-20 15:07
from __future__ import unicode_literals

from django.db import migrations, models
import weddings.models


class Migration(migrations.Migration):

    dependencies = [
        ('weddings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='wedding',
            name='height_field',
            field=models.IntegerField(default=800),
        ),
        migrations.AddField(
            model_name='wedding',
            name='meet',
            field=models.TextField(db_column='How Did You Meet The Bride/Groom?', default='nope', max_length=700),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='wedding',
            name='width_field',
            field=models.IntegerField(default=800),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='whoyouare',
            field=models.TextField(db_column='Tell Wedding Guests Who You Are!', max_length=700),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='yourface',
            field=models.ImageField(db_column='Your Face', height_field='height_field', upload_to=weddings.models.upload_location, width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='wedding',
            name='zodiacsign',
            field=models.CharField(choices=[('Aries', '\u2648'), ('Taurus', '\u2649'), ('Gemini', '\u264a'), ('Cancer', '\u264b'), ('Leo', '\u264c'), ('Virgo', '\u264d'), ('Libro', '\u264e'), ('Scorpius', '\u264f'), ('Sagittarius', '\u2650'), ('Capicorn', '\u2651'), ('Aquarius', '\u2652'), ('Pisces', '\u2653')], db_column='Zodiac Sign', default='Virgo', max_length=11),
        ),
        migrations.AlterModelTable(
            name='wedding',
            table='Wedding',
        ),
    ]