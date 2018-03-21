from configparser import ConfigParser


base_conf = ConfigParser()
base_conf.read('/Users/yinwoods/code/python/zhihu_walker/config.ini')

zhihu_conf = base_conf['zhihu']

redis_conf = base_conf["redis"]

celery_conf = base_conf["celery"]
