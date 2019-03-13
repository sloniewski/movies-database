from rest_framework import serializers

from .models import WatchList, WatchListEntry, CustomUser
from movie.serializers import MovieListSerializer
from main.serializers import ReadOnlySerializerMixin


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'username',
            'email',
        ]


class WatchListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='watchlist-detail',
        lookup_field='slug',
    )

    class Meta:
        model = WatchList
        fields = (
            'slug',
            'name',
            'url',
        )


class MovieReadOnlySerializer(ReadOnlySerializerMixin, MovieListSerializer):
    slug = serializers.SlugField(required=True)


class WatchListReadOnlySerializer(ReadOnlySerializerMixin, WatchListSerializer):
    slug = serializers.SlugField(required=True)


class WatchListEntrySerializer(serializers.ModelSerializer):
    movie = MovieReadOnlySerializer()
    list = WatchListReadOnlySerializer()

    class Meta:
        model = WatchListEntry
        fields = (
            'id',
            'movie',
            'list',
        )

    def create(self, validated_data):
        watch_list = self.fields['list'].get_instance(**validated_data['list'])
        movie = self.fields['movie'].get_instance(**validated_data['movie'])
        return self.Meta.model.objects.create(
            list=watch_list,
            movie=movie,
        )


class WatchListDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='watchlist-detail',
        lookup_field='slug',
    )
    entries = WatchListEntrySerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = (
            'name',
            'url',
            'entries',
            'created',
            'edited',
        )



