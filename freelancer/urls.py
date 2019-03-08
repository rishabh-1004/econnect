from django.conf.urls import url
from . import views
from django.contrib.auth.decorators import login_required


urlpatterns=[
	url(r'^home/$',views.Home.as_view(),name='home'),
#	url(r'^create_profile/$',views.CreateFreelancerProfile.as_view(),name='create_profile'),
	url(r'^testform/$',views.TestForm.as_view(),name='test'),
	url(r'^update/$',views.UpdateFreelancerProfile.as_view(),name='update')

]

	

