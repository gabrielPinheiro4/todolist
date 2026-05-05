from datetime import date
from sqlalchemy import String, Integer, ForeignKey, Date, func
from sqlalchemy.orm import Mapped, mapped_column
from ..db.base.base import db


class Projetos(db.Model):

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )

    titulo: Mapped[str] = mapped_column(String(60), nullable=False)

    data_criacao: Mapped[date] = mapped_column(
        Date, nullable=False, server_default=func.current_date()
    )

    descricao: Mapped[str] = mapped_column(String(80), nullable=False)

    id_usuario: Mapped[int] = mapped_column(
        ForeignKey('usuarios.id'), nullable=False
    )
