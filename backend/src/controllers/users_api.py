from bcrypt import hashpw, gensalt
from flask.views import MethodView
from sqlalchemy import select
from flask import jsonify, request
from json import loads
from ..models.users import Usuarios
from ..db.base.base import db


class UsersAPI(MethodView):

    def post(self):

        req_json: dict = loads(request.data)

        search_user = db.session.execute(
            select(Usuarios).where(Usuarios.email == req_json.get('email'))

        ).one_or_none()

        if search_user:
            return {'message': 'Email já cadastrado em uma conta'}, 409

        passwd_hashed = hashpw(
            req_json.get('passwd').encode('UTF-8'),
            gensalt()
        )

        new_user = Usuarios(
            nome=req_json.get('name'),
            email=req_json.get('email'),
            senha=passwd_hashed.decode('UTF-8')
        )

        db.session.add(new_user)

        db.session.commit()

        return jsonify('Usuário criado com sucesso')
