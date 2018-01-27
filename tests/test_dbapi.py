import json
import requests

from zhihu_walker.common import dbapi
from zhihu_walker.common.config import zhihu_config
from zhihu_walker.common.tools import flatten_dict
from zhihu_walker.models.live import Live


def parse_data():
    limit = 5
    offset = 0
    url = zhihu_config['url'] + f'&limit={limit}&offset={offset}'
    headers = json.loads(zhihu_config['headers'])
    response = requests.get(url, headers=headers)

    datas = response.json()['data']

    result = dict()
    for data in datas:
        flatten_dict(data, result)
        break
    return result


def test_insert():
    result = parse_data()
    item = Live(**result)
    dbapi.insert(item)


if __name__ == '__main__':
    test_insert()
