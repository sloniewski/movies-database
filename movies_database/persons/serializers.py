from rest_framework import serializers
from persons.models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = (
            'first_name',
            'second_name',
            'year_of_birth',
        )