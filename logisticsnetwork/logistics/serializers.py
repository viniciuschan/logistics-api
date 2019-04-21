import json

from rest_framework import serializers

from .models import LogisticsNet


class LogisticsNetSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    state = serializers.CharField(max_length=2)
    path_data = serializers.JSONField(binary=True)

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
                f'Name {value} is already been used, please choose another one.'
            )
        return value

    def validate_state(self, value):
        if len(value) != 2:
            raise serializers.ValidationError(
                'State name cannot be longer than 2 characters'
            )
        return value

    class Meta:
        model = LogisticsNet
        fields = (
            'id',
            'name',
            'path_data',
            'state',
        )
