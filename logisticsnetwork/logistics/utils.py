from numbers import Number


def has_mandatory_keys(data):
    for item in data:
        if not 'source' in item.keys() and not 'destination' in item.keys() and not 'distance' in item.keys():
            return False

    return True


def has_invalid_keys(data):
    keys = set(key for item in data for key in item.keys())
    for item in keys:
        if item not in ['source', 'destination', 'distance']:
            return True

    return False


def is_valid_distance(data):
    for item in data:
        if not isinstance(item['distance'], Number) or item['distance'] < 0:
            return False

    return True
