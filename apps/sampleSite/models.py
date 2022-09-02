from apps.app import db
from sqlalchemy.sql import func

class Kweet(db.Model):
    __tablename__="kweet"
    id = db.Column(db.Integer,primary_key=True)
    message = db.Column(db.String)
    create_at = db.Column(db.DateTime,server_default=func.now())


class Reserve(db.Model):
    __tablename__="reserve"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String)
    start_at =db.Column(db.DateTime)
    end_at = db.Column(db.DateTime)
    count = db.Column(db.Integer)

class Kakeibo(db.Model):
    __tablename__="kakeibo"
    id = db.Column(db.Integer,primary_key=True)
    date = db.Column(db.DateTime)
    budget = db.Column(db.Integer)
    item = db.Column(db.String)
    cost = db.Column(db.Integer)