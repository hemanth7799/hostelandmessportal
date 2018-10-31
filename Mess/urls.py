from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^refund/$', views.refund, name='refund'),
    url(r'^feedback/$', views.feedback, name='feedback'), 
]
