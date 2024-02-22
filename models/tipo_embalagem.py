import sqlalchemy as sa
from datetime import datetime
from models.model_base import ModelBase


class TipoEmbalagem(ModelBase):
    __tablename__: str = "tipos_embalagem"
    __table_args__ = {'extend_existing': True}

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    created_at: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    nome: str = sa.Column(sa.String(length=45), unique=True, nullable=False)