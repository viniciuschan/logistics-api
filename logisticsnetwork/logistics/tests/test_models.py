import json

from rest_framework.test import APITransactionTestCase

from logistics.models import LogisticsNet
from .factories import LogisticsNetFactory


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
        log_net = LogisticsNetFactory.create(name='Sao Paulo')
        object_text = f'ID: {log_net.pk} - Name: {log_net.name}'
        self.assertEqual(str(log_net), object_text)

    def test_create(self):
        log_net = LogisticsNet(
            name='Teste',
            path_data=self.path_data
        )
        self.assertIsInstance(log_net, LogisticsNet)
