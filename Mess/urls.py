from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$',views.homepage,name='homepage'),
	url(r'^messmenu',views.messmenu,name='messmenu'),
    url(r'^refund/$', views.refund, name='refund'),
    url(r'^feedback/$', views.feedback, name='feedback'), 
    url('^login/(?P<token>.+)$',views.login,name="login"),
    url('^login_user$',views.login_user,name="login_user")
]
