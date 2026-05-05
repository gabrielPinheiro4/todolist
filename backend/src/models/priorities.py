from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from ..db.base.base import db


class Prioridades(db.Model):

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )

    tipo: Mapped[int] = mapped_column(String(50), nullable=False)
