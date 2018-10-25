from django.conf.urls import include,url
from . import views
urlpatterns = [
	url(r'^add/$', views.inOutIndex ,name = "index") ]