from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150), nullable=False)


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    trueName = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    pic = db.Column(db.String, nullable=False)

    def addToDb(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def checkInDb(cls, name):
        return cls.query.filter_by(name=name).first()

