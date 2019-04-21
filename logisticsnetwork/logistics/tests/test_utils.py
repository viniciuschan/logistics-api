from rest_framework.test import APITransactionTestCase

from logistics.utils import (
    has_mandatory_keys,
    has_valid_keys,
    has_valid_distance
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

    def test_has_mandatory_keys_true(self):
        self.assertTrue(has_mandatory_keys(self.valid_data))

    def test_has_mandatory_keys_false(self):
        data = self.valid_data
        data[0].pop('source')

        self.assertFalse(has_mandatory_keys(data))

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
