from celery import Celery

from common import session
from common import tools
from common import dbapi

from models.live import Live
from common.config import zhihu_conf
from common.config import celery_conf


celery = Celery("app",
                broker=celery_conf["broker_url"],
                backend=celery_conf["backend"])
celery.config_from_object("app")


@celery.task
def async_worker(data):

    record = dict()
    tools.flatten_dict(data, record)

    attrs = set([attr for attr in Live.__dict__ if not attr.startswith("_")])
    record_attrs = record.keys()
    for key in (record_attrs - attrs):
        del record[key]

    record = Live(**record)
    dbapi.commit(record)


def cralwer():
    for offset in range(0, 100):
        url = zhihu_conf["url"]
        url = url.replace("{limit}", "10").replace("{offset}", str(offset))
        response = session.get(url)
        for data in response.json()["data"]:
            result = async_worker.apply_async(args=[data], countdown=3)
            result.get()


def main():
    cralwer()


if __name__ == '__main__':
    main()
