from flask_jwt_extended import jwt_required
from flask import jsonify, request
from sqlalchemy import select, func
from json import loads
from flask.views import MethodView
from ..db.base.base import db
from ..models.tasks import Tarefas
from ..models.status import Status


class TaskAPI(MethodView):

    @jwt_required()
    def post(self):

        req_json: dict = loads(request.data)

        status = db.session.execute(
            select(Status.id).where(func.lower(Status.tipo) == 'Pendente'.lower())

        ).one_or_none()

        if not status:
            return {'message': 'Status não configurado'}, 500
        
        status, status

        new_task = Tarefas(
            titulo=req_json.get('title'),
            descricao=req_json.get('desc'),
            data_criacao=func.now(),
            data_vencimaneto=req_json.get('dateCreation'),
            id_projetos=req_json.get('projectId'),
            id_status=status[0],
            id_prioridade=req_json.get('projectId')
        )

        db.session.add(new_task)

        db.session.commit()

        return jsonify('Tarefa adicionada com sucesso')