import json

from rest_framework import filters, serializers
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import LogisticsNet
from .serializers import LogisticsNetSerializer, BestPathSerializer
from .services import GraphService


class LogisticsNetViewSet(viewsets.ModelViewSet):
    """ModelViewSet for LogisticsNet model."""

    queryset = LogisticsNet.objects.all()
    serializer_class = LogisticsNetSerializer
    filter_backends = (filters.SearchFilter,)
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

    @action(detail=False, methods=['get'], url_path='best-path')
    def check_best_path(self, request, *args, **kwargs):
        serializer = BestPathSerializer(data=self.request.query_params)
        serializer.is_valid(raise_exception=True)
        graph_service = GraphService()

        try:
            log_net = LogisticsNet.objects.get(name=serializer.data.get('name'))
        except:
            raise serializers.ValidationError(
                f'Logistics Net not found. Please choose a valid one.'
            )

        try:
            response = graph_service.calculate_best_cost(
                path_data=json.dumps(log_net.path_data),
                source=serializer.data.get('source'),
                destination=serializer.data.get('destination'),
                autonomy=serializer.data.get('autonomy'),
                fuel_price=serializer.data.get('fuel_price')
            )
        except:
            raise Exception

        return Response(response, status=status.HTTP_200_OK)
