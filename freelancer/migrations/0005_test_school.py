# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-19 11:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelancer', '0004_auto_20170718_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='school',
            field=models.CharField(default='school1', max_length=100),
        ),
    ]
