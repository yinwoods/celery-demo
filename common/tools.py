import json


def flatten_dict(data, result, prefix=None):

    keys = data.keys()
    for key in keys:

        value = data[key]
        if prefix is not None:
            key = prefix + '_' + key

        if isinstance(value, dict):
            flatten_dict(value, result, prefix=key)
        elif isinstance(value, list):
            result[key] = json.dumps(value)
        elif isinstance(value, str):
            result[key] = value
        elif isinstance(value, int):
            result[key] = value
        elif isinstance(value, float):
            result[key] = value
        else:
            result[key] = value
    return result
