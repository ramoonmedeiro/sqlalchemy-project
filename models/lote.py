import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from models.model_base import ModelBase
from models.tipo_picole import TipoPicole


class Lote(ModelBase):
    __tablename__: str = "lotes"
    __table_args__ = {'extend_existing': True}

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    created_at: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    id_picole: int = sa.Column(sa.BigInteger, sa.ForeignKey(f"{TipoPicole.__tablename__}.id"), nullable=False)
    tipo_picole: TipoPicole = orm.relationship(TipoPicole.__class__.__name__, lazy="joined")
    quantidade: str = sa.Column(sa.Integer, nullable=False)
