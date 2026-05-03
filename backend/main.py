from flask import Flask
from flask_cors import CORS
from src.controllers.users_api import UsersAPI


class App:

    def __init__(self):

        self.app = Flask(__name__)

        CORS(self.app, resources={r"/api/*": {"origins": "*"}})

        self.app.config.from_object('config.Config')

        self.app.add_url_rule('/api/users', view_func=UsersAPI.as_view('users'))

    def run(self):
        self.app.run('0.0.0.0')


if __name__ == '__main__':

    app = App()
    app.run()
