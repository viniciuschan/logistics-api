import json
from numbers import Number


# Serializers utils to validate path_data structure
def has_valid_keys(data):
    valid_keys = set(['source', 'destination', 'distance'])
    try:
        data_keys = set(key for item in data for key in item.keys())
    except AttributeError:
        raise AttributeError('Invalid path data body')

    if data_keys.issubset(valid_keys):
        return True
    return False


def has_mandatory_keys(data):
    mandatory_keys = set(['source', 'destination', 'distance'])
    for item in data:
        if not mandatory_keys.issubset(item.keys()):
            return False
    return True


def has_valid_distance(data):
    for item in data:
        if not isinstance(item['distance'], Number) or item['distance'] < 0:
            return False
    return True


def has_valid_price(value):
    if isinstance(value, Number) and (0 < value < 99):
        return True
    return False


# GraphService utils to convert data to Networkx expected structure
def convert_dict_to_tuple(path_data):
    values_to_load = []
    for value in json.loads(path_data):
        values = (
            value['source'].upper(),
            value['destination'].upper(),
            value['distance']
        )
        values_to_load.append(values)
    return values_to_load
