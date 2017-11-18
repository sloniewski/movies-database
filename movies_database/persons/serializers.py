from rest_framework import serializers
from persons.models import Person


class PersonGeneralSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = (
            'fullname',
            'details_url',
        )


class PersonDetailSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Person
        fields = (
            'first_name',
            'second_name',
            'year_of_birth',
        )