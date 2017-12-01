from django.conf.urls import url
from persons import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register(
    r'person',
    views.PersonViewSet,
    base_name='person',
)

urlpatterns = [

]

urlpatterns += router.urls
