from importlib import import_module

from flask import Flask
from flask_cors import CORS

from flask_mongo_engine_sample import settings
from flask_mongo_engine_sample.extensions import db
from flask_mongo_engine_sample.settings import VIEWS
from flask_mongo_engine_sample_util.constants import Settings


def create_app(config=None):
    app = Flask(__name__)

    if config is not None:
        configuration = getattr(settings, config + Settings.CONFIG_SUFFIX)
        app.config.from_object(configuration)

    CORS(app)
    db.init_app(app)

    __register_blueprints(app)

    return app


def __register_blueprints(app):
    views = [import_module('%s.%s' % (module_name, Settings.VIEWS)) for module_name in VIEWS]
    for view in views:
        app.register_blueprint(view.blueprint)
