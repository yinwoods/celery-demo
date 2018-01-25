from configparser import ConfigParser


base_config = ConfigParser()
base_config.read('/Users/yinwoods/code/python/zhihu_walker/config.ini')

zhihu_config = base_config['zhihu']
