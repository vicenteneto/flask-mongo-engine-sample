from flask_mongo_engine_sample.extensions import db


class Person(db.Document):
    login = db.StringField(required=True)
    name = db.StringField(max_length=50)
    age = db.IntField()
