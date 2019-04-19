import json

from rest_framework import status
from rest_framework.test import APITransactionTestCase

from .factories import LogisticsNetFactory
from logistics.models import LogisticsNet


class LogisticNetViewSetTestCase(APITransactionTestCase):

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
        self.payload = {
            'name': 'Alfenas',
            'state': 'MG',
            'path_data': self.path_data
        }

    def test_create(self):
        endpoint_create = '/v1/logistics/'

        response = self.client.post(endpoint_create, self.payload)

        # I checked my ViewSet creating status_code because
        # APIClient is returning status=200 for POST method
        self.assertEqual(
            response.json().get('status_code'), status.HTTP_201_CREATED
        )
        self.assertEqual(LogisticsNet.objects.count(), 1)

    def test_create_without_name(self):
        endpoint_create = '/v1/logistics/'

        self.payload.pop('name')
        response = self.client.post(endpoint_create, self.payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(LogisticsNet.objects.count(), 0)

    def test_create_without_path_data(self):
        endpoint_create = '/v1/logistics/'

        self.payload.pop('name')
        response = self.client.post(endpoint_create, self.payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(LogisticsNet.objects.count(), 0)

    def test_update(self):
        net = LogisticsNetFactory.create()
        endpoint_update = f'/v1/logistics/{net.id}/'

        response = self.client.put(endpoint_update, self.payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_partial_update(self):
        net = LogisticsNetFactory.create()
        endpoint_patch = f'/v1/logistics/{net.id}/'

        payload = {
            'name': 'GO',
            'path_data': self.path_data
        }
        response = self.client.patch(endpoint_patch, payload)

        self.assertEqual(LogisticsNet.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve(self):
        net = LogisticsNetFactory.create()
        endpoint_retrieve = f'/v1/logistics/{net.id}/'

        response = self.client.get(endpoint_retrieve)

        self.assertEqual(LogisticsNet.objects.count(), 1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list(self):
        endpoint_list = '/v1/logistics/'
        LogisticsNetFactory.create()
        LogisticsNetFactory.create()
        LogisticsNetFactory.create()

        response = self.client.get(endpoint_list)

        self.assertEqual(LogisticsNet.objects.count(), 3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete(self):
        net = LogisticsNetFactory.create()
        endpoint_delete = f'/v1/logistics/{net.id}/'

        self.assertEqual(LogisticsNet.objects.count(), 1)

        response = self.client.delete(endpoint_delete)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(LogisticsNet.objects.count(), 0)
