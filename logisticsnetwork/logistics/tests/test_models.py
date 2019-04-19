import json
from decimal import Decimal

from rest_framework import status
from rest_framework.test import APITransactionTestCase

from logistics.models import LogisticsNet, UserSearch
from .factories import LogisticsNetFactory, UserSearchFactory


class LogisticNetModelTestCase(APITransactionTestCase):

    def setUp(self):
        self.path_data = json.dumps(
            [
                {
                    'source': 'C',
                    'destination': 'D',
                    'distance': 20
                },
                {
                    'source': 'D',
                    'destination': 'E',
                    'distance': 30
                },
                {
                    'source': 'E',
                    'destination': 'F',
                    'distance': 80
                }
            ]
        )

    def test_str(self):
        log_net = LogisticsNetFactory.create(
            name='Sao Paulo', state='SP',
        )
        object_text = f'ID: {log_net.pk} - {log_net.name} - {log_net.state}'

        self.assertEqual(str(log_net), object_text)

    def test_create(self):
        log_net = LogisticsNet(
            name='Teste',
            path_data=self.path_data,
            state='SP'
        )
        self.assertIsInstance(log_net, LogisticsNet)


class UserSearchModelTestCase(APITransactionTestCase):

    def test_str(self):
        search = UserSearchFactory.create(
            source='X', destination='Y',
        )
        object_text = f'{search.pk} - From: {search.source} To {search.destination}'

        self.assertEqual(str(search), object_text)

    def test_create(self):
        search = UserSearch(
            source='A',
            destination='W',
            autonomy=Decimal(15),
            fuel_price=Decimal(2.5)
        )
        self.assertIsInstance(search, UserSearch)
