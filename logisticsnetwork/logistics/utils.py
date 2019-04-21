from numbers import Number


def has_mandatory_keys(data):
	mandatory_keys = set(['source', 'destination', 'distance'])
	for item in data:
		if not mandatory_keys.issubset(item.keys()):
			return False

	return True


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
