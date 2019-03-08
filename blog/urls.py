from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns=[
	url(r'^$',views.BlogHome.as_view(template_name='blog/blog_home.html'),name='blog_home'),
	url(r'^blog_single/(?P<id>\d+)/$',views.OpenBlog.as_view(),name='blog_single'),
	url(r'^write_blog/$',views.WriteBlog.as_view(),name='write_blog'),
	url(r'^my_blog/$',views.MyBlog.as_view(),name='myblog'),
	url(r'^edit_blog/(?P<pk>\d+)/$',views.UserBlogUpdate.as_view(),name='my_blog_update'),
	url(r'^profile/$',views.viewProfile.as_view(),name='view_profile'),
	url(r'^edit_profile/(?P<pk>\d+)/$',views.BlogProfileUpdate.as_view(),name='profile_update'),
	url(r'^create_profile/$',views.CreateBlogProfile.as_view(),name='create_profile'),
	url(r'^test/$',views.Test.as_view(),name='test'),
	
	
]

	



