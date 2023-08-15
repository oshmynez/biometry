import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_db():
    db_user = os.environ["DB_USER"]
    db_password = os.environ["DB_PASS"]
    db_name = os.environ["DB_NAME"]
    db_port = os.environ["DB_PORT"]
    db_host = os.environ['DB_HOST']
    connect_string = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(db_user, db_password, db_host, db_port, db_name)
    session = sessionmaker(bind=create_engine(connect_string, echo=False))
    return session()


def commit_db(session):
    if session is not None:
        session.commit()


def close_db(session):
    if session is not None:
        session.commit()
        session.close()
