from django.conf.urls import url
from movies import views


urlpatterns = [

    url(r'movie/(?P<pk>(\d)+)/$',
        views.MovieApiView.as_view(), name='movie-detail'),

    url(r'movies/$',
        views.MovieListApiView.as_view(), name='movie-list'),

]