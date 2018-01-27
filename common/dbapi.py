from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from zhihu_walker.common.config import zhihu_config

engine = create_engine(zhihu_config['sql_alchemy_conn'])


def insert(record):
    session = Session(bind=engine)
    session.add(record)
    session.commit()
    session.close()
