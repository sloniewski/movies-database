from django.conf.urls import url
from movie import views

from rest_framework import routers

app_name = 'movie'

router = routers.SimpleRouter()
router.register(
    'movie',
    views.MovieView,
    base_name='movie',
)

urlpatterns = []

urlpatterns += router.urls
