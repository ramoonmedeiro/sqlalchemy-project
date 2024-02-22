import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future.engine import Engine

from models.model_base import ModelBase

from typing import Optional

import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

import logging

import sys
sys.path.append('../')
import models.__all_models


logging.basicConfig(level=logging.INFO)

user_db = os.getenv("POSTGRES_USER")
passwd_db = os.getenv("POSTGRES_PASSWORD")
db = os.getenv("POSTGRES_DB")
host_db = os.getenv("POSTGRES_HOST")
port_db = os.getenv("POSTGRES_PORT")


logging.info(f"Connecting to {host_db}:{port_db}/{db} as {user_db}")
conn = f"postgresql://{user_db}:{passwd_db}@{host_db}:{port_db}/{db}"


def create_engine(conn) -> Engine:
    engine = sa.create_engine(conn)
    return engine


def create_session(engine):
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


def create_tables() -> None:
    ModelBase.metadata.create_all(create_engine(conn))
