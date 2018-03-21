from common.tools import flatten_dict


if __name__ == '__main__':
    data = {
        'a': 'b',
        'c': {'a': 'z'},
        'd': ['e', 'f'],
        'e': [{'a': 'b'}, {'c': 'd'}],
        'f': 1,
        'g': 0.2
    }

    result = dict()
    flatten_dict(data, result)
    print(result)
