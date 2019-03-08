# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,render_to_response
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm



# Create your views here.
class HomeView(TemplateView):
	template_name='home/home.html'

	def get(self,request):
		return render(request,self.template_name)

class AboutView(TemplateView):
	template_name='home/about.html'

	def get(self,request):
		return render(request,self.template_name)

class ContactView(TemplateView):
	template_name='home/contact.html'
	title='Contact Form'
	confirm_message=None

	def get(self,request):
		form=ContactForm()
		args={'form':form,'title':self.title}
		return render(request,self.template_name,args)

	def post(self,request):
		form=ContactForm(request.POST)
		if form.is_valid():
			name=form.cleaned_data['name']
			comment= form.cleaned_data['comment']
			subject='Message from my site'
			message='%s %s' %(comment, name)
			emaiFrom=form.cleaned_data['email']
			emailTo=[settings.EMAIL_HOST_USER]
			send_mail(subject,message,emaiFrom,emailTo,fail_silently=False)
			title="Thanks!"
			confirm_message="Thanks for the message we will get back to you"
			form=None
			args={'form':form,'title':self.title,'confirm_message':confirm_message}
		return render(request,self.template_name,args)





