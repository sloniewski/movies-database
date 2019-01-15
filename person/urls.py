from rest_framework import routers

from person import views

router = routers.SimpleRouter()
router.register(
    r'person',
    views.PersonViewSet,
    base_name='person',
)

urlpatterns = [

]

urlpatterns += router.urls
