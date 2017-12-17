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


class CastSerializer(serializers.ModelSerializer):
    movie_url = serializers.URLField(
        source='movie.get_absolute_url',
        read_only=True,
    )
    person_url = serializers.URLField(
        source='person.get_absolute_url',
        read_only=True,
    )

    class Meta:
        model = Cast
        fields = (
            'movie',
            'person',
            'character',
            'movie_url',
            'person_url',
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