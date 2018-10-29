from django.conf.urls import include,url
from . import views
urlpatterns = [
	url(r'^inout/$', views.inOutIndex ,name = "index"),
	url(r'^hos_comp/$', views.HostelComplaintIndex ,name = "index")  ]