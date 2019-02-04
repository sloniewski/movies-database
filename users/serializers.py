from rest_framework import serializers

from .models import WatchList, WatchListEntry


class WatchListSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='users:watchlist-detail',
        lookup_field='slug',
    )

    class Meta:
        model = WatchList
        fields = (
            'id',
            'name',
            'url',
        )


class WatchListDetailSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='users:watchlist-detail',
        lookup_field='slug',
    )

    class Meta:
        model = WatchList
        fields = (
            'id',
            'name',
            'url',
            'entries',
        )


class WatchListEntrySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='users:watchlist_entry-detail',
        lookup_field='pk',
    )

    class Meta:
        model = WatchListEntry
        fields = (
            'list',
            'movie',
            'url',
        )
