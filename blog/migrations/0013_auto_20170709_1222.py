# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-09 12:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20170709_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 9, 12, 22, 47, 95139)),
        ),
        migrations.AlterField(
            model_name='userblog',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 9, 12, 22, 47, 94143)),
        ),
    ]