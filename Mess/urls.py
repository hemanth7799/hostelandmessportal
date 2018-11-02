from django.conf.urls import include,url
from . import views
app_name = 'Mess'
urlpatterns = [
    url(r'^refund/$', views.refund, name='refund'),
    url(r'^feedback/$', views.feedback, name='feedback'), 
    url(r'^feedbacklist/$', views.feedbacklist, name='feedbacklist'),
    url(r'^refundlist/$', views.refundlist, name='refundlist'),
    url('^login/(?P<token>.+)$',views.login,name="login")
    url('^$',views.login_user,name="login_user")
]
