from django.urls import reverse
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from users.permissions import IsAdminOrReadOnly
from movie.models import Movie, Genre
from movie.serializers import (
    MovieDetailSerializer,
    MovieListSerializer,
)

from main.utils import DefaultPaginator


class MovieViewSet(ModelViewSet):
    model = Movie
    serializer_class = MovieDetailSerializer
    queryset = Movie.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminOrReadOnly)
    pagination_class = DefaultPaginator

    def get_serializer_class(self):
        if self.request.method.lower() == 'get' and self.request.path == reverse('movie:movie-list'):
            return MovieListSerializer
        else:
            return super(MovieViewSet, self).get_serializer_class()


class GenreMoviesMoviesApiListView(ListCreateAPIView):
    serializer_class = MovieListSerializer

    def get_queryset(self):
        genre = Genre.objects.get(pk=self.request.resolver_match.kwargs['pk'])
        return genre.movie_set.all()
