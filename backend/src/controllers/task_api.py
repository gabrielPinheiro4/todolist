from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, request
from sqlalchemy import select, func
from json import loads
from flask.views import MethodView
from ..db.base.base import db
from ..models.tasks import Tarefas
from ..models.projects import Projetos
from ..models.status import Status
from .status_api import StatusAPI
from .priorities_api import PrioritiesAPI


class TaskAPI(MethodView):

    @jwt_required()
    def get(self):

        user_id = get_jwt_identity()

        projects = db.session.execute(
            select(Projetos.id).where(Projetos.id_usuario == user_id)

        ).all()

        list_projects_ids = [project[0] for project in projects]

        if not projects:
            return {'message': 'Usuário não possui nenhum projeto'}, 404

        if len(request.args) == 0:
            
            tasks = db.session.execute(
                select(Tarefas).where(Tarefas.id_projetos.in_(list_projects_ids))

            ).all()

            tasks_f = [

                {
                    'id': task[0].id,
                    'title': task[0].titulo,
                    'desc': task[0].descricao,
                    'dateCreation': task[0].data_criacao,
                    'dateExpiration': task[0].data_vencimento,
                    'priority': PrioritiesAPI.get_priority_by_id(task[0].id_prioridade),
                    'status': StatusAPI.get_status_by_id(task[0].id_status)
                }

                for task in tasks
            ]

            return jsonify(tasks_f)

        task = db.session.execute(
            select(Tarefas).where(Tarefas.id == request.args.get('taskId'))

        ).one_or_none()

        if not task:
            return {'message': 'Tarefa não encontrada'}, 404

        task, = task

        task_f = {
            'id': task.id,
            'title': task.titulo,
            'desc': task.descricao,
            'dateCreation': task.data_criacao,
            'dateExpiration': task.data_vencimento,
            'priority': PrioritiesAPI.get_priority_by_id(task.id_prioridade),
            'status': StatusAPI.get_status_by_id(task.id_status)
        }

        return jsonify(task_f)

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
            data_vencimento=req_json.get('dateCreation'),
            id_projetos=req_json.get('projectId'),
            id_status=status[0],
            id_prioridade=req_json.get('priorityId')
        )

        db.session.add(new_task)

        db.session.commit()

        return jsonify('Tarefa adicionada com sucesso')

    @jwt_required()
    def patch(self):

        req_json: dict = loads(request.data)

        task = db.session.execute(
            select(Tarefas).where(Tarefas.id == req_json.get('taskId'))

        ).one_or_none()

        if not task:
            return {'message': 'Tarefa não encontrada'}, 404

        task, = task

        task.titulo = req_json.get('title')

        task.descricao = req_json.get('desc')

        task.id_prioridade = req_json.get('priorityId')

        task.id_status = req_json.get('statusId')

        task.data_vencimento = req_json.get('dateExpiration')

        db.session.commit()

        return jsonify('Tarefa alterada com sucesso')
