from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import detail_route

from movies.models import Movie, Genre
from movies.serializers import MovieDetailSerializer, MovieListSerializer


class MovieView(ModelViewSet):
    model = Movie
    serializer_class = MovieListSerializer
    queryset = Movie.objects.all()

    @detail_route(methods=['get'])
    def details(self, request, pk):
        serializer = MovieDetailSerializer(
            instance=get_object_or_404(self.model, pk=pk),
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)


class GenreMoviesMoviesApiListView(ListCreateAPIView):
    serializer_class = MovieListSerializer

    def get_queryset(self):
        genre = Genre.objects.get(pk=self.request.resolver_match.kwargs['pk'])
        return genre.movie_set.all()