import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase


class Revendedor(ModelBase):
    __tablename__: str = "revededores"
    __table_args__ = {'extend_existing': True}

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    created_at: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    cnpj: str = sa.Column(sa.String(length=45), unique=True, nullable=False)
    razao_social: str = sa.Column(sa.String(length=100), unique=True, nullable=False)
    contato: str = sa.Column(sa.String(length=100), unique=True, nullable=False)
