# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-01-13 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20180109_0053'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_profile',
            name='skills',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]
