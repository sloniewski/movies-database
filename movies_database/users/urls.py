from django.conf.urls import url

from users import views

urlpatterns = [

    url(r'login/$', views.LoginApiView.as_view(), name='session-login'),

    url(r'whoami/$', views.WhoAmI.as_view(), name='whoami'),

]