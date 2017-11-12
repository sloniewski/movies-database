from django.conf.urls import url
from . import views


urlpatterns = [

    url(r'person/(?P<pk>(\d)+)/$',
        views.PersonApiView.as_view(), name='person-api'),

]