from django.conf.urls import include,url
from . import views

urlpatterns = [
	 url(r'^$',views.homepage,name='homepage'),
	url(r'caretakerhostelcomplaint/$', views.caretakerhostelcomplaint ,name = "caretaker"),
	url(r'^inout/$', views.inOutIndex ,name = "inOut"),
	url(r'^hostel_complaint/$', views.HostelComplaintIndex ,name = "HostelComplaint") ,
	url(r'^guestEntry/$', views.GuestEntryIndex ,name = "Guestentry"),
	url(r'^roomregistration/$', views.registration_form ,name = "roomregistration") ]


