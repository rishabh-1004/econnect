# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from account.forms import (
	RegistrationForm,
	EditProfileForm,
	ProfileTypeForm,
	
	)
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.


def register(request):
	if request.method=='POST':
		form=RegistrationForm(request.POST)
		form1=ProfileTypeForm(request.POST)
		if form.is_valid() and form1.is_valid():
			form.save()
			form1.save()
			return redirect('/account')
	else:
#		form=RegistrationForm()
		form1=ProfileTypeForm()	
		args={'form1':form1,}
		return render(request,'account/reg_form.html',args)

@login_required
def view_profile(request,pk=None):
	if pk:
		user=User.objects.get(pk=pk)
	else:
		user=request.user
	args={'user': user}
	return render(request,'accounts/profile.html',args)

@login_required
def view_edit(request):
	if request.method =='POST':
		form=EditProfileForm(request.POST,instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/account/profile')

	else:
		form=EditProfileForm(instance=request.user)
		args={'form':form}
		return render(request,'accounts/edit_profile.html',args)

@login_required
def change_password(request):
	if request.method == 'POST':
		form=PasswordChangeForm(data=request.POST,user=request.user)
		
		if form.is_valid():
			update_session_auth_hash(request,form.user)
			form.save()
			return redirect('home:home')

	else:
		form=PasswordChangeForm(user=request.user)
		args={'form':form}
		return render(request,'account/change_password.html',args)
