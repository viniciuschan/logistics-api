from decimal import Decimal
from factory import SubFactory
from factory.django import DjangoModelFactory

from logistics.models import LogisticsNet


class LogisticsNetFactory(DjangoModelFactory):

    class Meta:
        model = LogisticsNet

    name = 'Sao Paulo'
    date_added = '2019-04-18'
    path_data = [
        {'source': 'A', 'destination': 'B', 'distance': 10},
        {'source': 'A', 'destination': 'C', 'distance': 20},
        {'source': 'B', 'destination': 'D', 'distance': 15},
        {'source': 'B', 'destination': 'E', 'distance': 50},
        {'source': 'C', 'destination': 'D', 'distance': 30},
        {'source': 'D', 'destination': 'E', 'distance': 30}
    ]
