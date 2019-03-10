from rest_framework import serializers

from .models import WatchList, WatchListEntry, CustomUser
from movie.serializers import MovieListSerializer


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
        view_name='api-v1:watchlist-detail',
        lookup_field='slug',
    )

    class Meta:
        model = WatchList
        fields = (
            'slug',
            'name',
            'url',
        )


class WatchListEntrySerializer(serializers.ModelSerializer):
    movie = MovieListSerializer()
    list = WatchListSerializer()

    class Meta:
        model = WatchListEntry
        fields = (
            'movie',
            'list',
        )

    def create(self, validated_data):
        pass


class WatchListDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='api-v1:watchlist-detail',
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



