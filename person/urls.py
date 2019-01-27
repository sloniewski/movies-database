from rest_framework import routers

from person import views

app_name = 'person'

router = routers.SimpleRouter()
router.register(
    'person',
    views.PersonViewSet,
    base_name='person',
)

urlpatterns = []

urlpatterns += router.urls
