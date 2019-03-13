from rest_framework import serializers


class ReadOnlySerializerMixin:
    instance_lookup_field = None

    def update(self, validated_data):
        return self.get_instance(**validated_data)

    def create(self, validated_data):
        return self.get_instance(**validated_data)

    def get_instance(self, **kwargs):
        try:
            instance = self.Meta.model.objects.get(**kwargs)
        except self.Meta.model.DoesNotExist:
            raise serializers.ValidationError(
                '{} with provided slug does not exist'.format(self.Meta.model.__name__)
            )
        return instance
