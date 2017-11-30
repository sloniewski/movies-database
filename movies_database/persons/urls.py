from django.conf.urls import url
from persons import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register(
    r'ppl',
    views.PersonViewSet,
    base_name='prsn',
)

urlpatterns = [

    url(r'person/(?P<pk>(\d)+)/$',
        views.PersonApiView.as_view(), name='person-detail'),

    url(r'persons/$',
        views.PersonsListApiView.as_view(), name='person-list'),

]

urlpatterns += router.urls
