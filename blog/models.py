# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.
class UserBlog(models.Model):
	user=models.ForeignKey(User)
	title=models.CharField(max_length=150)
	body=models.CharField(max_length=500)
	created=models.DateTimeField(default=datetime.datetime.now())
	updated=models.DateTimeField(auto_now=True)
	image=models.ImageField(upload_to='blog_pics',blank=True)

class Comments(models.Model):
	blog=models.ForeignKey(UserBlog,on_delete=models.CASCADE)
	owner=models.ForeignKey(User)
	comment=models.CharField(max_length=200)
	created_on=models.DateTimeField(default=datetime.datetime.now())
