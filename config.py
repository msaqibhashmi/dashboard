import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MONGODB_DB = 'accounts'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017
