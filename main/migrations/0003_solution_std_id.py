# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-13 16:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_bid_std_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='solution',
            name='std_id',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]
