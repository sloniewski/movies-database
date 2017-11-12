from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie


class MovieListApiView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
