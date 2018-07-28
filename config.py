import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'test'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    Debug = True

class TestingConfig(Config):
    TESTING = True

config = {
    'development' : DevelopmentConfig,
    'testint' : TestingConfig,

    'default' : DevelopmentConfig
}