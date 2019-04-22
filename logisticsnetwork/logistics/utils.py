import json
from numbers import Number


# Serializers utils to validate path_data structure
def has_valid_keys(data):
    valid_keys = set(['source', 'destination', 'distance'])
    data_keys = set(key for item in data for key in item.keys())
    if not data_keys.issubset(valid_keys):
        return False
    return True


def has_valid_distance(data):
    for item in data:
        if not isinstance(item['distance'], Number) or item['distance'] < 0:
            return False
    return True


# GraphService utils to convert data to Networkx expected structure
def convert_dict_to_tuple(path_data):
    values_to_load = []
    for value in json.loads(path_data):
        values = (value['source'], value['destination'], value['distance'])
        values_to_load.append(values)

    return values_to_load
