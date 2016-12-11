from flask.blueprints import Blueprint

from flask_mongo_engine_sample_util.constants import URLPrefix

blueprint = Blueprint('persons', __name__, url_prefix=URLPrefix.PERSONS)
