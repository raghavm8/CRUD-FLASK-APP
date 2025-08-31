from datetime import datetime
from flask_login import UserMixin
from . import db
from .Enums.role_enum import Role

class User(UserMixin, db.Model):
    
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    name = db.Column(db.String(100))
    role = db.Column(db.Enum(Role), default=Role.USER, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    manager_id = db.Column(db.Integer)
    
    todos = db.relationship(
        "Todo",
        backref="user",
        lazy=True,
        cascade="all, delete-orphan"
    )