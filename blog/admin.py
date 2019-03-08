# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import UserBlog,Comments
# Register your models here.
admin.site.register(UserBlog)
admin.site.register(Comments)