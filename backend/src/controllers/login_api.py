from sqlalchemy import select
from flask.views import MethodView
from flask import request, make_response
from json import loads
from bcrypt import checkpw
from flask_jwt_extended import create_access_token, set_access_cookies, get_csrf_token
from datetime import timedelta, date
from ..models.users import Usuarios
from ..db.base.base import db


class LoginAPI(MethodView):

    def post(self):
        
        req_json: dict = loads(request.data)

        error = { 'message': 'Email ou senha incorreto' }, 404

        user_found = db.session.execute(
            select(Usuarios).where(Usuarios.email == req_json.get('email'))

        ).one_or_none()

        if not user_found:
            return error

        user_found, = user_found

        passwd_is_correct = checkpw(
            req_json.get('passwd').encode('UTF-8'),
            user_found.senha.encode('UTF-8')
        )

        if not passwd_is_correct:
            return error

        date_expires = date.today() + timedelta(days=1)

        token = create_access_token(
            identity=f'{user_found.id}',
            expires_delta=timedelta(seconds=86400)
        )

        response = make_response('user')

        set_access_cookies(response, token, max_age=86400)

        response.set_cookie(
            'csrf_access_token',
            value=get_csrf_token(token),
            httponly=False,
            expires=date_expires
        )

        return response
