# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 20:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170617_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 17, 20, 12, 0, 53140)),
        ),
        migrations.AlterField(
            model_name='userblog',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 17, 20, 12, 0, 52220)),
        ),
    ]
