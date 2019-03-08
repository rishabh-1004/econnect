# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save


CATEGORIES = (  
    ('Freelancer', 'freelancer'),
    ('Mentor', 'mentor'),
    ('Startup', 'startup'),
)
# Create your models here.
class BlogProfile(models.Model):
	user = models.OneToOneField(User)
	description = models.CharField(max_length=250,default='')
	city= models.CharField(max_length=100,default='')
	website=models.URLField(default='',blank=True)
	phone=models.IntegerField(default=0)
	image=models.ImageField(upload_to='profile_image',blank=True,default='default_user.jpg')
	
	def __str__(self):
		return self.user.username

def create_profile(sender,**kwargs):
	if kwargs['created']:
		blog_profile=BlogProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)

class ProfileType(models.Model):
	user = models.OneToOneField(User)
	account_type=models.CharField(max_length=10,choices=CATEGORIES)

	def __str__(self):
		return self.user.username

def create_profile(sender,**kwargs):
	if kwargs['created']:
		blog_profile=ProfileType.objects.create(user=kwargs['instance'])

post_save.connect(create_profile,sender=User)