from rest_framework import serializers
from movies.models import Movie
from persons.serializers import PersonSerializer


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    actors = PersonSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Movie
        fields = (
            'title',
            'description',
            'actors',
            'year',
            'genre',
        )
