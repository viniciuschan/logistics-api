from rest_framework import serializers

from .models import LogisticsNet


class LogisticsNetSerializer(serializers.ModelSerializer):

    class Meta:
        model = LogisticsNet
        fields = (
            'id',
            'name',
            'path_data',
            'state'
        )
