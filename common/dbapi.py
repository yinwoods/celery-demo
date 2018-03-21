from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from celery.utils.log import get_task_logger

from common.config import zhihu_conf


engine = create_engine(zhihu_conf['sql_alchemy_conn'])
logger = get_task_logger("dbapi")


def commit(record):
    session = Session(bind=engine)
    try:
        session.add(record)
        session.commit()
    except Exception as e:
        logger.debug(e)
    finally:
        session.close()
