from django.conf.urls import url
from movies import views

from rest_framework import routers

router = routers.SimpleRouter()
router.register(
    'movie',
    views.MovieView,
    base_name='movie',
)


urlpatterns = [

    url(r'movies/genre/(?P<pk>\d+)/$',
        views.GenreMoviesMoviesApiListView.as_view(), name='genre-movie-list'),
]

urlpatterns += router.urls