from rest_framework import serializers

from movie.models import Movie, Genre
from part.serializers import CastListSerializer, CrewListSerializer


class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = (
            'name',
            'movies_list_url',
        )


class MovieDetailSerializer(serializers.ModelSerializer):

    genre = GenreListSerializer(
        many=True,
        read_only=True,
    )

    cast = CastListSerializer(
        many=True,
        read_only=True,
    )

    crew = CrewListSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'year',
            'director',
            'description',
            'cast',
            'genre',
            'crew',
        )


class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'year',
            'director',
            'url',
        )
