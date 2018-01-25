import json
import requests


from zhihu_walker.common.config import zhihu_config
from zhihu_walker.common.tools import flatten_dict


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


def generate_orm_code(result):

    for key, value in result.items():
        if isinstance(value, str):
            print(f'{key} = Column(String(255), nullable=False, default=None)')
        elif isinstance(value, int):
            print(f'{key} = Column(Integer, nullable=False, default=None)')
        elif isinstance(value, float):
            print(f'{key} = Column(Float(20, 5), nullable=False, default=None)')


def generate_sql(result):
    sql = 'create table'
    print(sql)
    # TODO
    pass


if __name__ == '__main__':
    result = parse_data()
    generate_orm_code(result)
    generate_sql(result)
