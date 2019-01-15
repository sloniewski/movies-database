from rest_framework import serializers

from person.models import Person

from movie.serializers import MovieListSerializer


class PersonListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = (
            'id',
            'fullname',
            'url',
        )


class PersonDetailSerializer(serializers.ModelSerializer):

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
