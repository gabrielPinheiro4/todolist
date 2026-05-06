from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from src.db.base.base import db
from src.controllers.users_api import UsersAPI
from src.controllers.login_api import LoginAPI
from src.controllers.projects_api import ProjectsAPI
from src.controllers.status_api import StatusAPI
from src.controllers.priorities_api import PrioritiesAPI
from src.controllers.task_api import TaskAPI


class App:

    def __init__(self):

        self.app = Flask(__name__)

        CORS(self.app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

        self.app.config.from_object('config.Config')

        JWTManager(self.app)

        self.app.add_url_rule('/api/users', view_func=UsersAPI.as_view('users'))

        self.app.add_url_rule('/api/login', view_func=LoginAPI.as_view('login'))

        self.app.add_url_rule('/api/projects', view_func=ProjectsAPI.as_view('projects'))

        self.app.add_url_rule('/api/status', view_func=StatusAPI.as_view('status'))

        self.app.add_url_rule('/api/priorities', view_func=PrioritiesAPI.as_view('priorities'))

        self.app.add_url_rule('/api/tasks', view_func=TaskAPI.as_view('tasks'))

        db.init_app(self.app)

        with self.app.app_context():
            db.create_all()

    def run(self):
        self.app.run('0.0.0.0')


if __name__ == '__main__':

    app = App()
    app.run()
