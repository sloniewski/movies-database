from rest_framework import serializers

from part.models import Crew, Cast
from person.models import Person


class PersonListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = (
            'id',
            'fullname',
            'url',
        )


class CastListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='part:cast-detail',
        lookup_field='pk',
    )

    person = PersonListSerializer(
        read_only=True,
    )

    class Meta:
        model = Cast
        fields = (
            'id',
            'person',
            'character',
            'url',
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
            'id',
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
