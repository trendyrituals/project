# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-14 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_solution_std_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
