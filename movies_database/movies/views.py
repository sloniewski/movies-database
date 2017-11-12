# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, Response

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieApiView(APIView):

    def get_object(self, pk):
        return get_object_or_404(Movie, pk=pk)

    def get(self, request, pk):
        movie = self.get_object(pk)
        serializer = MovieSerializer(movie, context={'request': request})
        return Response(serializer.data)


class MovieListApiView(APIView):

    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True, context={"request": request})
        return Response(serializer.data)

