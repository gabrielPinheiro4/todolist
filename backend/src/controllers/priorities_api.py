from flask_jwt_extended import jwt_required
from flask import jsonify
from sqlalchemy import select
from flask.views import MethodView
from ..db.base.base import db
from ..models.priorities import Prioridades


class PrioritiesAPI(MethodView):

    @jwt_required()
    def get(self):

        all_priorities = db.session.execute(select(Prioridades)).all()

        if len(all_priorities) == 0:
            return {'message': 'Prioridades não cadastradas'}, 503

        all_priorities = [
            { 'id': priority[0].id, 'title': priority[0].tipo }
            for priority in all_priorities
        ]

        return jsonify(all_priorities)