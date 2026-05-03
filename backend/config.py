from dotenv import dotenv_values


class Config:

    env = dotenv_values('.env')

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = env.get('SQLALCHEMY_DATABASE_URI')
