import json
import requests
from common.config import zhihu_conf


session = requests.Session()
session.headers.update(json.loads(zhihu_conf["headers"]))
