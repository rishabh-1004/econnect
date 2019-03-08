# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class FreelancerProfile(models.Model):
	owner=models.ForeignKey(User)
	profile_pic=models.ImageField(upload_to='freelancers_pics',blank=True)
	phone=models.IntegerField(default=0)
	college=models.CharField(max_length=1000)
	school=models.CharField(max_length=1000)
	jobs=models.CharField(max_length=5000)
	internships=models.CharField(max_length=5000)
	projects=models.CharField(max_length=5000)
	skills=models.CharField(max_length=1000)
	training=models.CharField(max_length=5000)
	research=models.CharField(max_length=3000)
	additional=models.CharField(max_length=3000)

	def get_jobs(self):
		return self.jobs.split(",")
	def get_school(self):
		return self.school.split(",")
	def get_college(self):
		return self.college.split(",")
	def get_internships(self):
		return self.internships.split(",")
	def get_projects(self):
		return self.projects.split(",")
	def get_skills(self):
		return self.skills.split(",")
	def get_research(self):
		return self.research.split(",")

class Test(models.Model):
	jobs=models.CharField(max_length=5000)
	school=models.CharField(max_length=100,default='school1')

	def get_jobs(self):
		return self.jobs.split(",")


