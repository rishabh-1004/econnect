from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^home/$',views.HomeView.as_view() ,name="home"),
	url(r'^about/$',views.AboutView.as_view() ,name="about"),
	url(r'^contact/',views.ContactView.as_view(),name="contact")
]
