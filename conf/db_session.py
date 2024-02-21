import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker, Session

from models.model_base import ModelBase
import models.__all_models

import os
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())

user_db = os.getenv("POSTGRES_USER")
passwd_db = os.getenv("POSTGRES_PASSWORD")
db = os.getenv("POSTGRES_DB")
host_db = os.getenv("POSTGRES_HOST")
port_db = os.getenv("POSTGRES_PORT")

conn = f"postgresql://{user_db}:{passwd_db}@{host_db}:{port_db}/{db}"
engine = sa.create_engine(
    url=conn,
    echo=False
)

session = sessionmaker(
        bind=engine,
        expire_on_commit=False,
        class_=Session
    )


def create_table():
    ModelBase.metadata.drop_all(engine)
    ModelBase.metadata.create_all(engine)
