# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView,UpdateView,CreateView
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from freelancer.forms import  FreelancerProfileForm ,TestForm
from .models import FreelancerProfile, Test

# Create your views here.

class Home(LoginRequiredMixin ,TemplateView):
	template_name="freelancer/home.html"

	def get(self,request):
		return render(request,self.template_name)

#class CreateFreelancerProfile(LoginRequiredMixin,CreateView):
#	form_class= FreelancerProfileForm
#	login_url = 'account:login'
#	model = FreelancerProfile
#	template_name="freelancer/create_profile.html"
#	success_url='freelancer:home'
#
#	def form_valid(self, form):
#	    person = form.save(commit=False)
#	    person.owner = self.request.user
#	    return super(CreateFreelancerProfile,self).form_valid(form)

class TestForm(TemplateView):
	template_name='freelancer/test.html'

	def get(self,request):
		form=FreelancerProfileForm
		args={'form':form}
		return render(request, self.template_name,args)

	def post(self,request):
		forminput=FreelancerProfileForm(request.POST)
		if forminput.is_valid():
			forminput = forminput.save(commit=False)
			forminput.owner=request.user
			forminput.jobs=self.cleaned_data['jobs']
			forminput.save()
		
		return render(request,self.template_name,{'forminput':forminput} )


class UpdateFreelancerProfile(TemplateView):
	template_name='freelancer/update.html'

	def get(self,request):
		obj=FreelancerProfile.objects.get(owner=request.user)
		jobs=obj.get_jobs()#make it a list
		school=obj.get_school()
		internships=obj.get_internships()
		college=obj.get_college()
		projects=obj.get_projects()
		research=obj.get_research()
		skills=obj.get_skills()
		
		form = FreelancerProfileForm(initial={'job1': jobs[0],'job2':jobs[1],'job3':jobs[2],'job4':jobs[3],'school1':school[0],
											'school2':school[1],'college1':college[0],'college2':college[1],'college3':college[2],
											'project1':projects[0],'project2':projects[1],'project3':projects[2],'project4':projects[0],
											'skill1':skills[0],'skill2':skills[1],'skill3':skills[2],'skill4':skills[3],'research1':research[0],
											'research2':research[1],'research3':research[2],'research4':research[3],'internship1':internships[0],
											'internship2':internships[1],'internship3':internships[2],'internship4':internships[3],
							})			
		return render(request,self.template_name,{'form':form})

