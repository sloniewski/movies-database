from rest_framework import serializers

from part.models import Crew, Cast
from person.models import Person


class PersonListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='person:person-detail',
        lookup_field='slug',
    )

    class Meta:
        model = Person
        fields = (
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
        source='person.url',
        read_only=True,
    )
    person_name = serializers.CharField(
        source='person.fullname',
        read_only=True,
    )
    url = serializers.URLField(
        source='get_absolute_url',
        read_only=True,
    )

    class Meta:
        model = Cast
        fields = (
            'id',
            'movie',
            'person',
            'character',
            'movie_url',
            'person_url',
            'person_name',
            'url',
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


class CrewSerializer(serializers.ModelSerializer):
    movie_url = serializers.URLField(
        source='movie.get_absolute_url',
        read_only=True,
    )
    person_url = serializers.URLField(
        source='person.get_absolute_url',
        read_only=True,
    )

    class Meta:
        model = Crew
        fields = (
            'person',
            'movie',
            'credit',
            'movie_url',
            'person_url',
        )
