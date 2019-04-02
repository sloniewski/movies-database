from rest_framework import serializers

from part.models import Crew, Cast
from movie.models import Movie
from person.models import Person
from main.serializers import ReadOnlySerializerMixin


class PersonReadOnlySerializer(ReadOnlySerializerMixin, serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='person-detail',
        lookup_field='slug',
        read_only=True,
    )

    class Meta:
        model = Person
        fields = (
            'fullname',
            'slug',
            'url',
        )


class MovieReadOnlySerializer(ReadOnlySerializerMixin, serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='movie-detail',
        lookup_field='slug',
        read_only=True,
    )
    title = serializers.CharField(
        required=False,
        read_only=True
    )
    year = serializers.IntegerField(
        required=False,
        read_only=True
    )

    class Meta:
        model = Movie
        fields = [
            'title',
            'year',
            'url',
            'slug',
        ]


class CastListSerializer(serializers.ModelSerializer):
    person = PersonReadOnlySerializer()

    class Meta:
        model = Cast
        fields = (
            'person',
            'character',
        )


class CrewListSerializer(serializers.ModelSerializer):
    person = PersonReadOnlySerializer()

    class Meta:
        model = Crew
        fields = (
            'person',
            'credit',
        )


class CastSerializer(serializers.ModelSerializer):
    movie = MovieReadOnlySerializer()
    person = PersonReadOnlySerializer()

    url = serializers.HyperlinkedIdentityField(
        view_name='cast-detail',
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

    def create(self, validated_data):
        return self.Meta.model.objects.create(
            movie=self.fields['movie'].get_instance(**validated_data['movie']),
            person=self.fields['person'].get_instance(**validated_data['person']),
            character=validated_data['character'],
        )


class CrewSerializer(serializers.ModelSerializer):
    movie = MovieReadOnlySerializer()
    person = PersonReadOnlySerializer()

    url = serializers.HyperlinkedIdentityField(
        view_name='crew-detail',
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

    def create(self, validated_data):
        return self.Meta.model.objects.create(
            movie=self.fields['movie'].get_instance(**validated_data['movie']),
            person=self.fields['person'].get_instance(**validated_data['person']),
            credit=validated_data['credit'],
        )
