# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import FreelancerProfile,Test

# Register your models here.

admin.site.register(FreelancerProfile)
admin.site.register(Test)