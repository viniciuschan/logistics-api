from collections import OrderedDict

from rest_framework import filters
from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import LogisticsNet
from .serializers import LogisticsNetSerializer


class LogisticsNetViewSet(viewsets.ModelViewSet):
    queryset = LogisticsNet.objects.all()
    serializer_class = LogisticsNetSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'state')

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
