# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import TemplateView, UpdateView,CreateView
from django.shortcuts import render, redirect
from blog.models import UserBlog,Comments 
from account.models import BlogProfile
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.forms import EnterBlog, EnterComments, ComplexFieldForm
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

class BlogHome(TemplateView):
	
	template_name='blog/blog_home.html'
		

	def get(self, request):
		blogs=UserBlog.objects.all()
		paginator = Paginator(blogs, 3)
		page = request.GET.get('page')
		try:
			blogs = paginator.page(page)
		except PageNotAnInteger:
	        # If page is not an integer, deliver first page.
			blogs = paginator.page(1)
		except EmptyPage:
	        # If page is out of range (e.g. 9999), deliver last page of results.
			blogs = paginator.page(paginator.num_pages)
		return render(request,self.template_name,{'blogs':blogs})

class OpenBlog(TemplateView):
	template_name='blog/blog_single.html'

	def get(self,request,id):
		blogs=UserBlog.objects.get(pk=id)
		try:
			comments=Comments.objects.filter(blog=blogs)
			form=EnterComments()
			args={'blog':blogs,'comments':comments,'form':form}
		except:
			form=EnterComments()
			args={'blog':blogs,'comment':comment}
			
		return render(request,self.template_name,args)

	def post(self,request,id):
		blogs=UserBlog.objects.get(pk=id)
		comment=EnterComments(request.POST)
		if comment.is_valid():
			comment=comment.save(commit=False)
			comment.blog=blogs
			comment.owner=request.user
			comment.save()
			form=EnterComments()
		comments=Comments.objects.filter(blog=blogs)
		args={'blog':blogs,'comments':comments,'form':form}
		return render(request,self.template_name,args)

		

class WriteBlog(LoginRequiredMixin,TemplateView):
	login_url = 'account:login'
	template_name='blog/blog_write.html'

	def get(self,request):
		form=EnterBlog()
		args={'form':form}
		return render(request,self.template_name,args)

	def post(self,request):
		blog_input=EnterBlog(request.POST)
		if blog_input.is_valid():
			blog_input = blog_input.save(commit=False)
			blog_input.user=request.user
			blog_input.save()
		return redirect('blog:blog_home')

class MyBlog(LoginRequiredMixin,TemplateView):
	login_url = 'account:login'
	template_name='blog/my_blog.html'

	
	def get(self,request):
		blogs=UserBlog.objects.filter(user=request.user)
		paginator = Paginator(blogs, 3)
		page = request.GET.get('page')
		try:
			blogs = paginator.page(page)
		except PageNotAnInteger:
	        # If page is not an integer, deliver first page.
			blogs = paginator.page(1)
		except EmptyPage:
	        # If page is out of range (e.g. 9999), deliver last page of results.
			blogs = paginator.page(paginator.num_pages)
		args={'blogs': blogs}
		return render(request,self.template_name,args)

class UserBlogUpdate(LoginRequiredMixin,UpdateView):
	login_url = 'account:login'
	model=UserBlog
	fields=['title','body']
	template_name_suffix='_update_form'
	success_url = reverse_lazy('blog:myblog')

class BlogProfileUpdate(LoginRequiredMixin,UpdateView):
	login_url = 'account:login'
	model=BlogProfile
	fields=['description','city','website','phone','image']
	template_name='blog/blogprofile_update_form.html'
	success_url=reverse_lazy('blog:view_profile')

class viewProfile(LoginRequiredMixin,TemplateView):
	template_name='blog/view_profile.html'

	def get(self,request):
		try:
#			BlogProfile.objects.get(user=request.user):
			profile=BlogProfile.objects.get(user=request.user)
			args={'profile':profile}
			return render(request,self.template_name,args)

		except:
			return redirect('blog:create_profile')
		

class CreateBlogProfile(LoginRequiredMixin,CreateView):
		login_url = 'account:login'
		model = BlogProfile
		fields=['description','city','website','phone','image',]
		template_name="blog/create_profile.html"
		success_url='blog:view_profile'

		def form_valid(self, form):
		    person = form.save(commit=False)
		    person.user = self.request.user
		    #article.save()  # This is redundant, see comments.
		    return super(CreateBlogProfile, self).form_valid(form)

class Test(TemplateView):
	template_name='blog/test.html'

	def get(self,request):
		form=ComplexFieldForm()
		args={'form':form}
		return render(request,self.template_name,args)

	def post(self,request):
		form_input=ComplexFieldForm(request.POST)
		if form_input.is_valid():
			value=form_input.cleaned_data
			value=value['field1']
			s="#"
			value=value.split(",")
			final=s.join(value)
		else:
			value="Invalid"
		return render(request,self.template_name,{'value':value,'final':final})


