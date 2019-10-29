from rest_framework import serializers
from rest_framework.test import APITransactionTestCase

from .factories import LogisticsNetFactory
from logistics.serializers import (
    LogisticsNetSerializer,
    BestPathSerializer
)


class LogisticsNetSerializerTestCase(APITransactionTestCase):

    def setUp(self):
        self.path_data = [
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
        self.payload = {
            'name': 'Rio de Janeiro',
            'path_data': self.path_data
        }
        self.log_net = LogisticsNetFactory.create(
            name='Ribeirao Preto',
            path_data=self.path_data
        )
        self.serializer = LogisticsNetSerializer(
            instance=self.log_net
        )

    def test_valid_name(self):
        self.assertEqual(
            self.log_net.name, self.serializer.data['name']
        )

    def test_invalid_name_too_low_characters(self):
        data = self.payload
        data.update({'name': 'A'})

        serializer = LogisticsNetSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors.keys())

    def test_invalid_name_too_many_characters(self):
        invalid_name = 'test-test-test-test-test\
            test-testtesttest-test-test-test-test-test\
            test-test-test-test-test-test-test-test-test'
        data = self.payload
        data.update({'name': invalid_name})

        serializer = LogisticsNetSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors.keys())

    def test_valid_json(self):
        serializer = LogisticsNetSerializer(data=self.payload)
        self.assertTrue(serializer.is_valid())

    def test_invalid_json(self):
        path_data = ['A', 'B', 'C']
        data = {
            'name': 'Rio de Janeiro',
            'path_data': path_data
        }
        serializer = LogisticsNetSerializer(data=data)
        with self.assertRaises(AttributeError):
            serializer.is_valid(raise_exception=True)

    def test_valid_path_data(self):
        serializer = LogisticsNetSerializer(data=self.payload)
        self.assertTrue(serializer.is_valid())

    def test_invalid_path_data_key(self):
        invalid_path_data = [
                {
                    'sou': 'C',
                    'destination': 'D',
                    'distance': 20
                },
                {
                    'source': 'D',
                    'destination': 'E',
                    'distance': 30
                },
            ]
        data = {
            'name': 'Tocantins',
            'path_data': invalid_path_data
        }
        serializer = LogisticsNetSerializer(data=data)
        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)

    def test_invalid_path_data_source(self):
        invalid_path_data = [
                {
                    'destination': 'D',
                    'distance': 20
                },
                {
                    'source': 'D',
                    'destination': 'E',
                    'distance': 30
                },
            ]
        data = {
            'name': 'Rio de Janeiro',
            'path_data': invalid_path_data
        }
        serializer = LogisticsNetSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_path_data_destination(self):
        invalid_path_data = [
                {
                    'source': 'C',
                    'distance': 20
                },
                {
                    'source': 'D',
                    'destination': 'E',
                    'distance': 30
                }
            ]
        data = {
            'name': 'Sao Paulo',
            'path_data': invalid_path_data
        }

        serializer = LogisticsNetSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_path_data_distance(self):
        invalid_path_data = [
                {
                    'source': 'C',
                    'destination': 'D',
                },
                {
                    'source': 'D',
                    'destination': 'E',
                    'distance': 30
                }
            ]
        data = {
            'name': 'Araraquara',
            'path_data': invalid_path_data
        }
        serializer = LogisticsNetSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_path_data_distance_negative(self):
        invalid_path_data = [
                {
                    'source': 'C',
                    'destination': 'D',
                    'distance': -20
                },
                {
                    'source': 'D',
                    'destination': 'E',
                    'distance': 30
                }
        ]
        data = {
            'name': 'Sao Jose dos Campos',
            'path_data': invalid_path_data
        }
        serializer = LogisticsNetSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_path_data_distance_not_a_number(self):
        invalid_path_data = [
                {
                    'source': 'C',
                    'destination': 'D',
                    'distance': '25D'
                },
                {
                    'source': 'D',
                    'destination': 'E',
                    'distance': 30
                }
        ]
        data = {
            'name': 'Sao Jose dos Campos',
            'path_data': invalid_path_data
        }
        serializer = LogisticsNetSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_path_data_body_attributes(self):
        data = {
            'name': 'Rio Preto',
            'path_data': '{"a":"b"}'
        }
        serializer = LogisticsNetSerializer(data=data)
        with self.assertRaises(AttributeError):
            serializer.is_valid(raise_exception=True)


class BestPathSerializerTestCase(APITransactionTestCase):

    def setUp(self):
        self.payload = {
            'name': 'Sao Paulo',
            'source': 'A',
            'destination': 'D',
            'autonomy': 10,
            'fuel_price': 2.5
        }
        self.invalid_data = 'test-test-test-test-test\
            test-testtesttest-test-test-test-test-test\
            test-test-test-test-test-test-test-test-test'

    def test_valid_data(self):
        serializer = BestPathSerializer(data=self.payload)
        self.assertTrue(serializer.is_valid())

    def test_invalid_name_too_low_characters(self):
        data = self.payload
        data.update({'name': 'A'})

        serializer = BestPathSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_name_too_many_characters(self):
        data = self.payload
        data.update({'name': self.invalid_data})

        serializer = BestPathSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_source_too_low_characters(self):
        data = self.payload
        data.update({'source': ''})

        serializer = BestPathSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_source_too_many_characters(self):
        data = self.payload
        data.update({'source': self.invalid_data})

        serializer = BestPathSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_destination_too_low_characters(self):
        data = self.payload
        data.update({'destination': ''})

        serializer = BestPathSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_destination_too_many_characters(self):
        data = self.payload
        data.update({'destination': self.invalid_data})

        serializer = BestPathSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_autonomy_not_a_number(self):
        data = self.payload
        data.update({'autonomy': '1A'})

        serializer = BestPathSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_autonomy_negative_number(self):
        data = self.payload
        data.update({'autonomy': -50})

        serializer = BestPathSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_fuel_price_not_a_number(self):
        data = self.payload
        data.update({'fuel_price': 'ABC'})

        serializer = BestPathSerializer(data=data)
        self.assertFalse(serializer.is_valid())

    def test_invalid_fuel_price_negative_number(self):
        data = self.payload
        data.update({'fuel_price': -50})

        serializer = BestPathSerializer(data=data)
        self.assertFalse(serializer.is_valid())
