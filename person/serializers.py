from rest_framework import serializers

from person.models import Person
from part.models import Crew, Cast

from movie.serializers import MovieListSerializer


class CrewMemberListSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(
        read_only=True,
    )

    class Meta:
        model = Crew
        fields = (
            'movie',
            'credit',
        )


class CastMemberListSerializer(serializers.ModelSerializer):
    movie = MovieListSerializer(
        read_only=True,
    )

    class Meta:
        model = Cast
        fields = (
            'movie',
            'character',
        )


class PersonListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='person-detail',
        lookup_field='slug',
        read_only=True,
    )

    class Meta:
        model = Person
        fields = (
            'first_name',
            'second_name',
            'url',
            'slug',
        )


class PersonDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='person-detail',
        lookup_field='slug',
    )

    crew_member = CrewMemberListSerializer(
        many=True,
        read_only=True,
    )

    cast_member = CastMemberListSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Person
        fields = (
            'first_name',
            'second_name',
            'year_of_birth',
            'cast_member',
            'crew_member',
            'url',
        )
