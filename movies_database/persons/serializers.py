from rest_framework import serializers

from persons.models import Person

from movies.serializers import MovieListSerializer


class PersonListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Person
        fields = (
            'fullname',
            'details_url',
        )


class PersonDetailSerializer(serializers.HyperlinkedModelSerializer):

    movie_set = MovieListSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Person
        fields = (
            'first_name',
            'second_name',
            'year_of_birth',
            'movie_set',
        )