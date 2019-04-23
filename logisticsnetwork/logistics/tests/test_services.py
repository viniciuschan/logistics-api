import json
from decimal import Decimal

from rest_framework.test import APITransactionTestCase

from .factories import LogisticsNetFactory
from logistics.services import GraphService


class GraphServiceTestCase(APITransactionTestCase):

    def setUp(self):
        self.path_data = json.dumps(
            [
                {
                    'source': 'A',
                    'destination': 'B',
                    'distance': 10
                },
                {
                    'source': 'A',
                    'destination': 'C',
                    'distance': 20
                },
                {
                    'source': 'B',
                    'destination': 'D',
                    'distance': 15
                },
                {
                    'source': 'B',
                    'destination': 'E',
                    'distance': 50
                },
                {
                    'source': 'C',
                    'destination': 'D',
                    'distance': 30
                },
                {
                    'source': 'D',
                    'destination': 'E',
                    'distance': 30
                }
            ]
        )
        self.log_net = LogisticsNetFactory.create(
            path_data=self.path_data
        )
        self.graph = GraphService()

    def test_init(self):
        graph = GraphService()
        self.assertIsInstance(graph, GraphService)

    def test_load_graph(self):
        loaded = self.graph.load_graph_data(self.log_net.path_data)
        self.assertTrue(loaded)

    def test_get_shortest_path(self):
        self.graph.load_graph_data(self.log_net.path_data)
        shortest_path = self.graph.get_shortest_path('A', 'D')
        self.assertEqual(shortest_path, ['A', 'B', 'D'])

    def test_get_shortest_distance(self):
        self.graph.load_graph_data(self.log_net.path_data)
        distance_value = self.graph.get_shortest_distance('A', 'D')
        self.assertEqual(distance_value, 25)

    def test_calculate_price(self):
        price1 = self.graph.calculate_price(
            distance=Decimal(100),
            autonomy=Decimal(10),
            fuel_price=Decimal(2.5)
        )
        price2 = self.graph.calculate_price(
            distance=Decimal(25),
            autonomy=Decimal(10),
            fuel_price=Decimal(2.5)
        )
        self.assertEqual(price1, Decimal(25))
        self.assertEqual(price2, Decimal(6.25))

    def test_calculate_best_cost(self):
        self.graph.load_graph_data(self.path_data)

        best_cost1 = self.graph.calculate_best_cost(
            path_data=self.path_data,
            source='A',
            destination='D',
            autonomy=Decimal(10),
            fuel_price=Decimal(2.5)
        )
        best_cost2 = self.graph.calculate_best_cost(
            path_data=self.path_data,
            source='A',
            destination='E',
            autonomy=Decimal(10),
            fuel_price=Decimal(2)
        )
        self.assertEqual(
            best_cost1,
            {'shortest_path': ['A', 'B', 'D'], 'best_cost': Decimal('6.25')}
        )
        self.assertEqual(
            best_cost2,
            {'shortest_path': ['A', 'B', 'D', 'E'], 'best_cost': Decimal('11.00')}
        )
