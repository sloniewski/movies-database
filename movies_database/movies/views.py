# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import get_object_or_404

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView, Response
from rest_framework import status

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieApiView(RetrieveUpdateDestroyAPIView):
    serializer_class = MovieSerializer
    queryset = Movie


class MovieListApiView(ListCreateAPIView):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()
