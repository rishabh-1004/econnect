# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20170617_2019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogprofile',
            name='image',
            field=models.ImageField(blank=True, default='default_user.jpg', upload_to='profile_image'),
        ),
    ]