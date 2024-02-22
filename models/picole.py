import sqlalchemy as sa
import sqlalchemy.orm as orm
from datetime import datetime
from models.model_base import ModelBase
from models.sabores import Sabores
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.conservante import Conservante
from models.ingrediente import Ingrediente
from models.aditivio_nutritivo import AditivoNutritivo


conservantes_picoles = sa.Table(
    "conservantes_picoles",
    ModelBase.metadata,
    sa.Column("id_conservante", sa.BigInteger, sa.ForeignKey(f"{Conservante.__tablename__}.id")),
    sa.Column("id_picole", sa.BigInteger, sa.ForeignKey("picoles.id")),
)

ingredientes_picoles = sa.Table(
    "ingredientes_picoles",
    ModelBase.metadata,
    sa.Column("id_ingrediente", sa.BigInteger, sa.ForeignKey(f"{Ingrediente.__tablename__}.id")),
    sa.Column("id_picole", sa.BigInteger, sa.ForeignKey("picoles.id")),
)

aditivos_picoles = sa.Table(
    "aditivos_picoles",
    ModelBase.metadata,
    sa.Column("id_aditivo_nutritivo", sa.BigInteger, sa.ForeignKey(f"{AditivoNutritivo.__tablename__}.id")),
    sa.Column("id_picole", sa.BigInteger, sa.ForeignKey("picoles.id")),
)


class Picole(ModelBase):
    __tablename__: str = "picoles"

    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    created_at: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    preco: float = sa.Column(sa.DECIMAL(8, 2), nullable=False)

    id_sabor: int = sa.Column(sa.BigInteger, sa.ForeignKey(f"{Sabores.__tablename__}.id"), nullable=False)
    sabor: Sabores = orm.relationship(Sabores.__class__.__name__, lazy="joined")

    id_embalagem: TipoEmbalagem = sa.Column(sa.BigInteger, sa.ForeignKey(f"{TipoEmbalagem.__tablename__}.id"), nullable=False)
    tipo_embalagem: TipoEmbalagem = orm.relationship(TipoEmbalagem.__class__.__name__, lazy="joined")

    id_tipo_picole: TipoPicole = sa.Column(sa.BigInteger, sa.ForeignKey(f"{TipoPicole.__tablename__}.id"), nullable=False)
    tipo_picole: TipoPicole = orm.relationship(TipoPicole.__class__.__name__, lazy="joined")

    conservantes: Conservante = orm.relationship(
        Conservante.__class__.__name__,
        secondary=conservantes_picoles,
        backref="conservante",
        lazy="joined"
    )

    ingredientes: Ingrediente = orm.relationship(
        Ingrediente.__class__.__name__,
        secondary=ingredientes_picoles,
        backref="ingrediente",
        lazy="joined"
    )

    aditivos: AditivoNutritivo = orm.relationship(
        AditivoNutritivo.__class__.__name__,
        secondary=aditivos_picoles,
        backref="aditivo_nutritivo",
        lazy="joined"
    )
