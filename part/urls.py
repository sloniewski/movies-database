from part import views

from rest_framework import routers

app_name = 'part'


router = routers.SimpleRouter()
router.register(
    'cast',
    views.CastView,
    base_name='cast',
)

router.register(
    'crew',
    views.CrewView,
    base_name='crew',
)


urlpatterns = []

urlpatterns += router.urls
