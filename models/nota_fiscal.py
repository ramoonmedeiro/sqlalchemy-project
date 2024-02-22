import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from models.model_base import ModelBase
from models.revendor import Revendedor
from models.lote import Lote

lotes_nota_fical = sa.Table(
    "lotes_nota_fiscal",
    ModelBase.metadata,
    sa.Column("id_lote", sa.BigInteger, sa.ForeignKey(f"{Lote.__tablename__}.id")),
    sa.Column("id_nota_fiscal", sa.BigInteger, sa.ForeignKey("notas_fiscais.id")),
)


class NotaFiscal(ModelBase):
    __tablename__: str = "notas_fiscais"

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    date: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    valor: float = sa.Column(sa.DECIMAL(8, 2), nullable=False)
    numero_serie: str = sa.Column(sa.String(length=45), unique=True, nullable=False)
    descricao: str = sa.Column(sa.String(length=200), nullable=False)

    id_revendedor: int = sa.Column(sa.BigInteger, sa.ForeignKey(f"{Revendedor.__tablename__}.id"), nullable=False)
    revendedor: Revendedor = orm.relationship(Revendedor.__class__.__name__, lazy="joined")

    lotes: Lote = orm.relationship(
        Lote.__class__.__name__,
        secondary=lotes_nota_fical,
        backref="lote",
        lazy="joined"
    )
