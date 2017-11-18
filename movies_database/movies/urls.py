from django.conf.urls import url
from movies import views


urlpatterns = [

    url(r'movie/(?P<pk>\d+)/$',
        views.MovieApiView.as_view(), name='movie-detail'),

    url(r'movies/$',
        views.MovieListApiView.as_view(), name='movie-list'),

    url(r'movies/genre/(?P<pk>\d+)/$',
        views.GenreMoviesMoviesApiListView.as_view(), name='genre-movie-list'),

]