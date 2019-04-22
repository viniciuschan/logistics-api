from rest_framework import serializers

from .models import LogisticsNet
from.utils import has_valid_keys, has_valid_distance


class LogisticsNetSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, required=True)
    path_data = serializers.JSONField(binary=True, required=True)

    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError(
                'Invalid name, it must contain more than 2 characters.'
            )
        elif len(value) > 100:
            raise serializers.ValidationError(
                'Invalid name, you have exceeded 100 characters'
            )
        elif LogisticsNet.objects.filter(name=value).exists():
            raise serializers.ValidationError(
                f'Name {value} is already been used.'
            )
        return value

    def validate_path_data(self, value):
        if not has_valid_keys(value):
            raise serializers.ValidationError(
                'Invalid keys for path data'
            )

        if not has_valid_distance(value):
            raise serializers.ValidationError(
                'Invalid distance for path data, it must a positive integer'
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
    name = serializers.CharField(max_length=100, required=True)
    source = serializers.CharField(max_length=50, required=True)
    destination = serializers.CharField(max_length=50, required=True)
    autonomy = serializers.DecimalField(decimal_places=2, max_digits=4)
    fuel_price = serializers.DecimalField(decimal_places=2, max_digits=4)

    class Meta:
        model = LogisticsNet
        fields = (
            'name',
            'source',
            'destination',
            'autonomy',
            'fuel_price',
        )
