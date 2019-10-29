import json

from rest_framework import filters
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.throttling import (
    AnonRateThrottle, UserRateThrottle
)

from .models import LogisticsNet
from .serializers import (
    LogisticsNetSerializer, BestPathSerializer
)
from .services import GraphService


class LogisticsNetViewSet(viewsets.ModelViewSet):
    """ModelViewSet for LogisticsNet model."""

    queryset = LogisticsNet.objects.all()
    serializer_class = LogisticsNetSerializer
    filter_backends = (filters.SearchFilter,)
    throttle_classes = (AnonRateThrottle, UserRateThrottle,)
    search_fields = ('name',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['get'], url_path='best-path')
    def check_best_path(self, request, *args, **kwargs):
        serializer = BestPathSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        graph_service = GraphService()

        try:
            log_net = LogisticsNet.objects.get(name=serializer.data.get('name'))
        except LogisticsNet.DoesNotExist:
            raise ValueError('Invalid name, Logistics Network not found.')

        response = graph_service.calculate_best_cost(
            path_data=json.dumps(log_net.path_data),
            source=serializer.data.get('source'),
            destination=serializer.data.get('destination'),
            autonomy=serializer.data.get('autonomy'),
            fuel_price=serializer.data.get('fuel_price')
        )
        return Response(response, status=status.HTTP_200_OK)
