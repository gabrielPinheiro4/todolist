from datetime import date
from sqlalchemy import String, Integer, ForeignKey, Date, func
from sqlalchemy.orm import Mapped, mapped_column
from ..db.base.base import db


class Tarefas(db.Model):

    id: Mapped[int] = mapped_column(
        Integer, primary_key=True, autoincrement=True
    )

    titulo: Mapped[str] = mapped_column(String(60), nullable=False)

    descricao: Mapped[str] = mapped_column(String(80), nullable=False)

    data_criacao: Mapped[date] = mapped_column(
        Date, nullable=False, server_default=func.current_date()
    )

    data_vencimento: Mapped[date] = mapped_column(Date, nullable=False)

    id_projetos: Mapped[int] = mapped_column(
        ForeignKey('projetos.id'), nullable=False
    )

    id_status: Mapped[int] = mapped_column(
        ForeignKey('status.id'), nullable=False
    )

    id_prioridade: Mapped[int] = mapped_column(
        ForeignKey('prioridades.id'), nullable=False
    )
