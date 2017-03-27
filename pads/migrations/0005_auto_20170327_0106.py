# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-27 01:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pads', '0004_locker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locker',
            name='pad',
        ),
        migrations.AddField(
            model_name='pad',
            name='locker',
            field=models.ManyToManyField(to='pads.Locker'),
        ),
        migrations.AlterField(
            model_name='locker',
            name='status',
            field=models.CharField(blank=True, default='empty', max_length=20, null=True),
        ),
    ]
