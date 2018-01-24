from django.conf.urls import url
from movies import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register(
    'movie',
    views.MovieView,
    base_name='movie',
)

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


urlpatterns = [

    url(r'movies/genre/(?P<pk>\d+)/$',
        views.GenreMoviesMoviesApiListView.as_view(), name='genre-movie-list'),
]

urlpatterns += router.urls
