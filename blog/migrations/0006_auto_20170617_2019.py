# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 20:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170617_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 17, 20, 19, 25, 193435)),
        ),
        migrations.AlterField(
            model_name='userblog',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 17, 20, 19, 25, 192520)),
        ),
    ]
