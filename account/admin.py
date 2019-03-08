# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from account.models import BlogProfile,ProfileType



class BlogProfileAdmin(admin.ModelAdmin):
	list_display=('user','website','phone','user_info')

	def user_info(self,obj):
		return obj.description

	def get_queryset(self,request):
		queryset = super(BlogProfileAdmin, self).get_queryset(request)
		queryset=queryset.order_by('-phone','user')
		return queryset

	user_info.short_description = 'INFO'

admin.site.register(BlogProfile, BlogProfileAdmin)


admin.site.register(ProfileType)