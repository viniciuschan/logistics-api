import json

from rest_framework import serializers, status
from rest_framework.test import APITransactionTestCase

from .factories import LogisticsNetFactory
from logistics.models import LogisticsNet
from logistics.serializers import LogisticsNetSerializer


class LogisticsNetSerializerTestCase(APITransactionTestCase):

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
            'name': 'Rio de Janeiro',
            'state': 'RJ',
            'path_data': self.path_data
        }
        self.log_net = LogisticsNetFactory.create(
            name='Ribeirao Preto',
            state='SP',
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

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('name', serializer.errors.keys())

    def test_invalid_name_too_many_characters(self):
        invalid_name = 'teste-teste-teste-teste-teste-teste-teste\
            testeteste-teste-teste-teste-teste-teste-teste-teste-teste'

        data = self.payload
        data.update({'name': invalid_name})

        serializer = LogisticsNetSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('name', serializer.errors.keys())

    def test_invalid_existing_name(self):
        LogisticsNetFactory.create(name='Americana')

        data = self.payload
        data.update({'name': 'Americana'})

        serializer = LogisticsNetSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('name', serializer.errors.keys())

    def test_valid_state(self):
        self.assertEqual(
            self.log_net.state, self.serializer.data['state']
        )

    def test_invalid_state(self):
        data = self.payload
        data.update({'state': 'Sao Paulo'})

        serializer = LogisticsNetSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
        self.assertIn('state', serializer.errors.keys())

    def test_valid_json(self):
        serializer = LogisticsNetSerializer(data=self.payload)
        response = serializer.is_valid(raise_exception=True)

        self.assertTrue(response)

    def test_invalid_json(self):
        path_data = ['A', 'B', 'C']
        data = {
            'name': 'Rio de Janeiro',
            'state': 'RJ',
            'path_data': path_data
        }
        serializer = LogisticsNetSerializer(data=data)

        with self.assertRaises(serializers.ValidationError):
            serializer.is_valid(raise_exception=True)
