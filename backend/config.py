from dotenv import dotenv_values


class Config:

    env = dotenv_values('.env')

    DEBUG = True
    SQLALCHEMY_DATABASE_URI = env.get('SQLALCHEMY_DATABASE_URI')
    SECRET_KEY = env.get('SECRET_KEY')
    JWT_SECRET_KEY = env.get('JWT_SECRET_KEY')
    JWT_TOKEN_LOCATION = env.get('JWT_TOKEN_LOCATION')
    JWT_COOKIE_SECURE = False
