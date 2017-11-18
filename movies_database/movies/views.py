from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from movies.models import Movie, Genre
from movies.serializers import MovieDetailSerializer, MovieListSerializer


class MovieApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieDetailSerializer
    queryset = Movie


class MovieListApiView(ListCreateAPIView):
    serializer_class = MovieListSerializer
    queryset = Movie.objects.all()


class GenreMoviesMoviesApiListView(ListCreateAPIView):
    serializer_class = MovieListSerializer

    def get_queryset(self):
        genre = Genre.objects.get(pk=self.request.resolver_match.kwargs['pk'])
        return genre.movie_set.all()
