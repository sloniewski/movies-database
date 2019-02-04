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
