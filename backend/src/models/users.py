from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from ..db.base.base import db


class Usuarios(db.Model):

    id: Mapped[int] = mapped_column(Integer, autoincrement=True, primary_key=True)

    nome: Mapped[str] = mapped_column(String(70), nullable=False)

    senha: Mapped[str] = mapped_column(String(150), nullable=False)

    email: Mapped[str] = mapped_column(String(150), nullable=False)
