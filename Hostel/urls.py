from django.conf.urls import include,url
from . import views
urlpatterns = [
	url(r'^inout/$', views.inOutIndex ,name = "index"),
	url(r'^hostel_complaint/$', views.HostelComplaintIndex ,name = "index1") ,
	url(r'^guestEntry/$', views.GuestEntryIndex ,name = "index2"),
	url(r'^roomregistration/$', views.registration_form ,name = "index3") ]
