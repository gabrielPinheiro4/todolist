from flask_jwt_extended import jwt_required
from flask import jsonify
from sqlalchemy import select
from flask.views import MethodView
from ..db.base.base import db
from ..models.status import Status


class StatusAPI(MethodView):

    @jwt_required()
    def get(self):

        all_status = db.session.execute(select(Status)).all()

        if len(all_status) == 0:
            return {'message': 'Status não cadastrados'}, 503

        all_status = [
            { 'id': status[0].id, 'title': status[0].tipo }
            for status in all_status
        ]

        return jsonify(all_status)

    @staticmethod
    def get_status_by_id(id):

        status = db.session.execute(
            select(Status).where(Status.id == id)

        ).one_or_none()

        if not status:
            return False

        return { 'id': status[0].id, 'title': status[0].tipo }
