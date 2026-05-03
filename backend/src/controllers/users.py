from flask.views import MethodView
from flask import jsonify, request


class UsersAPI(MethodView):

    def post(self):

        return 'ola mundo'
