import json

from rest_framework.test import APITransactionTestCase

from logistics.utils import (
    has_valid_keys,
    has_valid_distance,
    convert_dict_to_tuple
)


class UtilsTestCase(APITransactionTestCase):

    def setUp(self):
        self.valid_data = [
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

    def test_has_valid_keys_true(self):
        self.assertTrue(has_valid_keys(self.valid_data))

    def test_has_valid_keys_false(self):
        invalid_data = [
            {
                'sou': 'C',
                'destination': 'D',
                'distance': 20
            }
        ]
        self.assertFalse(has_valid_keys(invalid_data))

    def test_has_valid_distance_number(self):
        self.assertTrue(has_valid_distance(self.valid_data))

    def test_has_valid_distance_not_a_number(self):
        invalid_data = [
            {
                'source': 'C',
                'destination': 'D',
                'distance': '50 KM'
            }
        ]

        self.assertFalse(has_valid_distance(invalid_data))

    def test_has_valid_distance_positive(self):
        self.assertTrue(has_valid_distance(self.valid_data))

    def test_has_valid_distance_negative(self):
        invalid_data = [
            {
                'source': 'C',
                'destination': 'D',
                'distance': -50
            }
        ]
        self.assertFalse(has_valid_distance(invalid_data))

    def convert_dict_to_tuple(self):
        path_data = json.dumps(
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
        valid_data = [
            ('A', 'B', 10), ('A', 'C', 20), ('B', 'D', 15),
            ('B', 'E', 50), ('C', 'D', 30), ('D', 'E', 30)
        ]
        converted_values = convert_dict_to_tuple(path_data)
        self.assertEqual(converted_values, valid_data)
