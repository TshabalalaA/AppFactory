from . import db
from sqlalchemy.sql import func



class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(50), nullable=False)
    firstname = db.Column(db.String(50) ,nullable=False)
    contactNo = db.Column(db.String(10), unique=True , nullable=False)
    # date = db.Column(db.DateTime(timezone=True), default=func.now())
    age = db.Column(db.Integer(), nullable=False)
    check = db.Column(db.String(50), nullable=False)

    out = db.Column(db.Integer(), nullable=False)
    movies = db.Column(db.Integer(), nullable=False)
    tv = db.Column(db.Integer(), nullable=False)
    radio = db.Column(db.Integer() , nullable=False)
