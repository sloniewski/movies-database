from rest_framework import serializers

from persons.models import Person

from movies.serializers import MovieListSerializer



class PersonListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Person
        fields = (
            'id',
            'fullname',
            'url',
        )


class PersonDetailSerializer(serializers.HyperlinkedModelSerializer):

    movie_cast = MovieListSerializer(
        many=True,
        read_only=True,
    )

    movie_crew = MovieListSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Person
        fields = (
            'id',
            'first_name',
            'second_name',
            'year_of_birth',
            'movie_cast',
            'movie_crew',
        )