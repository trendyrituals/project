# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-05 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20180105_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='review',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
