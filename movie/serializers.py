from rest_framework import serializers

from movie.models import Genre, Movie
from part.serializers import CastListSerializer, CrewListSerializer

API_VERSION = 'api-v1'


class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = (
            'name',
        )


class MovieDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name=API_VERSION + ':movie-detail',
        lookup_field='slug',
    )
    rating = serializers.FloatField(read_only=True)
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
            'title',
            'year',
            'director',
            'description',
            'cast',
            'genre',
            'crew',
            'url',
            'rating',
            'slug',
        )
        read_only_fields = [
            'slug',
        ]


class MovieListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        read_only=True,
        view_name=API_VERSION + ':movie-detail',
        lookup_field='slug',
    )
    rating = serializers.FloatField(read_only=True)

    class Meta:
        model = Movie
        fields = (
            'title',
            'year',
            'director',
            'url',
            'rating',
            'slug'
        )
        read_only_fields = [
            'slug',
        ]
