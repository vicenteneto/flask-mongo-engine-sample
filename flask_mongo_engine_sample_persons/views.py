from flask.blueprints import Blueprint
from flask.globals import request

from flask_mongo_engine_sample_persons.models import Person
from flask_mongo_engine_sample_util.constants import URLPrefix

blueprint = Blueprint('persons', __name__, url_prefix=URLPrefix.PERSONS)


# Paginate through person
@blueprint.route('')
def view_persons():
    page = request.args.get('page', 1, int)
    paginated_persons = Person.objects.paginate(page=page, per_page=10)
    return paginated_persons


# 404 if object doesn't exist
@blueprint.route('/<person_id>')
def view_person(person_id):
    person = Person.objects.get_or_404(_id=person_id)
    return person
