class Config(object):
    DEBUG = False
    TESTING = False
    MONGODB_DB = 'flask_mongo_engine_sample'
    MONGODB_HOST = '127.0.0.1'
    MONGODB_PORT = 27017


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
