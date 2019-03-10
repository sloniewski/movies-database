from rest_framework import serializers

from part.models import Crew, Cast
from movie.models import Movie
from person.models import Person

API_VERSION = 'api-v1'


class PersonListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name=API_VERSION + ':person-detail',
        lookup_field='slug',
        read_only=True,
    )

    class Meta:
        model = Person
        fields = (
            'fullname',
            'url',
        )


class MovieListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name=API_VERSION + ':movie-detail',
        lookup_field='slug',
        read_only=True,
    )

    class Meta:
        model = Movie
        fields = [
            'title',
            'year',
            'url'
        ]


class CastListSerializer(serializers.ModelSerializer):
    person = PersonListSerializer()

    class Meta:
        model = Cast
        fields = (
            'person',
            'character',
        )


class CrewListSerializer(serializers.ModelSerializer):
    person = PersonListSerializer()

    class Meta:
        model = Crew
        fields = (
            'person',
            'credit',
        )


class CastSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer()
    person = PersonListSerializer()

    url = serializers.HyperlinkedIdentityField(
        view_name=API_VERSION + ':cast-detail',
        read_only=True,
    )

    class Meta:
        model = Cast
        fields = (
            'id',
            'character',
            'movie',
            'person',
            'url',
        )


class CrewSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer()
    person = PersonListSerializer()

    url = serializers.HyperlinkedIdentityField(
        view_name=API_VERSION + ':crew-detail',
        read_only=True,
    )

    class Meta:
        model = Crew
        fields = (
            'id',
            'credit',
            'person',
            'movie',
            'url',
        )
