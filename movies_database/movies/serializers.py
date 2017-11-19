from rest_framework import serializers
from movies.models import Movie, Genre, Cast, Crew

from persons.models import Person


class GenreListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = (
            'name',
            'movies_list_url',
        )


class PersonListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Person
        fields = (
            'id',
            'fullname',
            'url',
        )


class CastListSerializer(serializers.ModelSerializer):
    person = PersonListSerializer(
        read_only=True,
    )

    class Meta:
        model = Cast
        fields = (
            'person',
            'character',
        )


class CrewListSerializer(serializers.ModelSerializer):
    person = PersonListSerializer(
        read_only=True,
    )

    class Meta:
        model = Crew
        fields = (
            'person',
            'credit',
        )


class MovieDetailSerializer(serializers.ModelSerializer):

    genre = GenreListSerializer(
        many=True,
        read_only=True,
    )

    cast_movie = CastListSerializer(
        many=True,
        read_only=True,
    )

    crew_movie = CrewListSerializer(
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
            'cast_movie',
            'genre',
            'crew_movie',
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