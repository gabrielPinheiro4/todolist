from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import jsonify, request
from sqlalchemy import select, func
from flask.views import MethodView
from json import loads
from ..db.base.base import db
from ..models.projects import Projetos


class ProjectsAPI(MethodView):

    @jwt_required()
    def get(self):

        user_id = get_jwt_identity()

        projects_from_user = db.session.execute(
            select(Projetos).where(Projetos.id_usuario == user_id)

        ).all()

        if len(projects_from_user) > 0:

            projects_from_user = [
                {
                    'title': project[0].titulo,
                    'desc': project[0].descricao,
                    'date_creation': project[0].data_criacao
                }

                for project in projects_from_user
            ]

        return jsonify(projects_from_user)

    @jwt_required()
    def post(self):

        req_json: dict = loads(request.data)

        project_created = db.session.execute(
            select(Projetos.titulo).where(Projetos.titulo == req_json.get('title'))

        ).one_or_none()

        if project_created:
            return {'message': 'Projeto já criado'}, 409

        user_id = get_jwt_identity()

        new_project = Projetos(
            titulo=req_json.get('title'),
            descricao=req_json.get('desc'),
            data_criacao=func.current_date(),
            id_usuario=user_id
        )

        db.session.add(new_project)

        db.session.commit()

        return jsonify('Projeto criado com sucesso')
