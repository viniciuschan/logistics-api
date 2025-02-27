from rest_framework import serializers

from .models import LogisticsNet
from .utils import (
    has_valid_keys,
    has_valid_distance,
    has_mandatory_keys,
    has_valid_price
)


class LogisticsNetSerializer(serializers.ModelSerializer):
    """ModelSerializer for LogisticsNet model."""

    name = serializers.CharField(max_length=100, required=True)
    path_data = serializers.JSONField(required=True)

    def validate_name(self, value):
        if not 2 <= len(value) <= 100:
            raise serializers.ValidationError(
                'Invalid name, allowed between 2 and 100 characters'
            )
        elif self.instance and LogisticsNet.objects.exclude(
            pk=self.instance.pk
        ).filter(name=value).exists():
            raise serializers.ValidationError(
                f'Name {value} is already been used.'
            )
        return value

    def validate_path_data(self, value):
        if not has_mandatory_keys(value):
            raise serializers.ValidationError(
                'Missing path data key'
            )

        if not has_valid_keys(value):
            raise serializers.ValidationError(
                'Invalid keys for path data'
            )

        if not has_valid_distance(value):
            raise serializers.ValidationError(
                'Invalid distance, it must be a positive integer'
            )
        return value

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'path_data': instance.path_data,
        }

    class Meta:
        model = LogisticsNet
        fields = (
            'id',
            'name',
            'path_data',
        )


class BestPathSerializer(serializers.ModelSerializer):
    """Serializer to validate Best Path action fields."""

    name = serializers.CharField(max_length=100, required=True)
    source = serializers.CharField(max_length=40, required=True)
    destination = serializers.CharField(max_length=40, required=True)
    autonomy = serializers.DecimalField(
        decimal_places=2, max_digits=4, required=True
    )
    fuel_price = serializers.DecimalField(
        decimal_places=2, max_digits=4, required=True
    )

    def validate_name(self, value):
        if not 2 <= len(value) <= 40:
            raise serializers.ValidationError(
                'Invalid name, allowed between 1 and 100 characters'
            )
        return value

    def validate_source(self, value):
        if not 1 <= len(value) <= 40:
            raise serializers.ValidationError(
                'Invalid source name, allowed between 1 and 40 characters'
            )
        return value

    def validate_destination(self, value):
        if not 1 <= len(value) <= 40:
            raise serializers.ValidationError(
                'Invalid destination name, allowed between 1 and 40 characters'
            )
        return value

    def validate_autonomy(self, value):
        if not has_valid_price(value):
            raise serializers.ValidationError(
                'Invalid autonomy value, it must be a positive number'
            )
        return value

    def validate_fuel_price(self, value):
        if not has_valid_price(value):
            raise serializers.ValidationError(
                'Invalid price, it must be a positive number'
            )
        return value

    class Meta:
        model = LogisticsNet
        fields = (
            'name',
            'source',
            'destination',
            'autonomy',
            'fuel_price',
        )
