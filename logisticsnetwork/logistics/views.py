import json
from collections import OrderedDict
from decimal import Decimal

from rest_framework import filters
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import LogisticsNet
from .serializers import LogisticsNetSerializer
from .services import GraphService


class LogisticsNetViewSet(viewsets.ModelViewSet):
    queryset = LogisticsNet.objects.all()
    serializer_class = LogisticsNetSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(
            OrderedDict(
                serializer.data, status_code=status.HTTP_201_CREATED
            )
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=partial
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(
            OrderedDict(
                serializer.data, status_code=status.HTTP_200_OK
            )
        )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)

        return Response(
            OrderedDict(
                serializer.data, status_code=status.HTTP_200_OK
            )
        )

    @action(detail=False, methods=['get'], url_path='check-best-way')
    def check_best_path(self, request, *args, **kwargs):
        name = self.request.query_params.get('name').lower()
        source = self.request.query_params.get('source')
        destination = self.request.query_params.get('destination')
        autonomy = self.request.query_params.get('autonomy')
        fuel_price = self.request.query_params.get('fuel_price')
        graph_service = GraphService()

        try:
            log_net = LogisticsNet.objects.get(name=name)
        except LogisticsNet.DoesNotExist as exc:
            raise exc
        try:
            response = graph_service.calculate_best_cost(
                path_data=json.dumps(log_net.path_data),
                source=source,
                destination=destination,
                autonomy=autonomy,
                fuel_price=fuel_price
            )
        except Exception as exc:
            raise exc

        return Response(response, status=status.HTTP_200_OK)
