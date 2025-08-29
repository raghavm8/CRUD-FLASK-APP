from flask_login import UserMixin
from . import db

class User(UserMixin, db.Model):
    
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(100))
    
    todos = db.relationship(
        "Todo",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan"
    )