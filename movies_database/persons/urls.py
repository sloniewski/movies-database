from django.conf.urls import url
from persons import views


urlpatterns = [

    url(r'person/(?P<pk>(\d)+)/$',
        views.PersonApiView.as_view(), name='person-detail'),

]