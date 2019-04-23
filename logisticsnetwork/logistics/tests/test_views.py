import json

from django.db import IntegrityError
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
            'path_data': self.path_data
        }
        self.endpoint = '/v1/logistics/'

    def test_create(self):

        response = self.client.post(self.endpoint, self.payload)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(LogisticsNet.objects.count(), 1)

    def test_create_duplicated_name(self):
        self.client.post(self.endpoint, self.payload)
        with self.assertRaises(IntegrityError):
            self.client.post(self.endpoint, self.payload)

    def test_create_without_name(self):
        self.payload.pop('name')
        response = self.client.post(self.endpoint, self.payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(LogisticsNet.objects.count(), 0)

    def test_create_without_path_data(self):
        self.payload.pop('name')
        response = self.client.post(self.endpoint, self.payload)
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
        LogisticsNetFactory.create(name='Santa Catarina')
        LogisticsNetFactory.create(name='Amazonas')
        LogisticsNetFactory.create(name='Rio de Janeiro')

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

    def test_check_best_path_view_valid(self):
        log = LogisticsNetFactory.create(name='map')
        source, destination, autonomy, fuel_price = 'A', 'D', 10, 2

        params = '?name={}&source={}&destination={}&autonomy={}&fuel_price={}'.format(
            log.name,  source, destination, autonomy, fuel_price
        )
        endpoint = f'/v1/logistics/best-path/{params}'
        response = self.client.get(endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_check_best_path_view_invalid(self):
        log = LogisticsNetFactory.create(name='map')
        source, destination, autonomy, fuel_price = 'A', 'Z', 10, 2

        params = '?name={}&source={}&destination={}&autonomy={}&fuel_price={}'.format(
            log.name,  source, destination, autonomy, fuel_price
        )
        endpoint = f'/v1/logistics/best-path/{params}'
        with self.assertRaises(ValueError):
            self.client.get(endpoint)
