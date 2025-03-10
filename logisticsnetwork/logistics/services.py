import networkx as nx

from .utils import convert_dict_to_tuple


class GraphService:
    """Service to calculate graph distance and costs."""

    def __init__(self):
        self.graph = nx.Graph()

    def load_graph_data(self, path_data):
        """ Load graph with valid path_data.
            Networkx expects a list of tuples.
        """

        try:
            valid_data = convert_dict_to_tuple(path_data)
            self.graph.add_weighted_edges_from(valid_data)
        except TypeError:
            raise TypeError('Invalid data type to load graph')
        return True

    def get_shortest_path(self, source, destination):
        """Get shortest path based on source and destination.
            Outputs a list, ['A', 'B', 'D'] for example.
        """

        try:
            shortest_path = nx.dijkstra_path(
                self.graph,
                source.upper(),
                destination.upper()
            )
        except:
            raise ValueError('Invalid route.')
        return shortest_path

    def get_shortest_distance(self, source, destination):
        """Get shortest path based on source and destination.
            Outputs a number value, 25 for example.
        """

        try:
            distance = nx.dijkstra_path_length(
                self.graph,
                source.upper(),
                destination.upper()
            )
        except:
            raise ValueError('Invalid route.')
        return distance

    def calculate_price(self, distance, autonomy, fuel_price):
        """Calculate best cost considering the shortest distance
            between two points.
        """

        try:
            price = float(distance) / float(autonomy) * float(fuel_price)
        except ZeroDivisionError:
            price = 0
        return price

    def calculate_best_cost(self, path_data, source,
                            destination, autonomy, fuel_price):
        self.load_graph_data(path_data)
        shortest_path = self.get_shortest_path(source, destination)
        shortest_distance = self.get_shortest_distance(
            source, destination
        )
        best_cost = self.calculate_price(
            shortest_distance, autonomy, fuel_price
        )

        response = {
            'shortest_path': shortest_path,
            'best_cost': best_cost
        }
        return response
