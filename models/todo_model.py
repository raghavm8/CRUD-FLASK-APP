from datetime import datetime
from . import db
from .Enums.priority_enum import Priority
from .Enums.status_enum import Status

class Todo(db.Model):
    
    __tablename__ = "todos"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000))
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    priority = db.Column(db.Enum(Priority), default=Priority.MEDIUM, nullable=False)
    status = db.Column(db.Enum(Status), default=Status.ASSIGNED, nullable=False)
    due_date = db.Column(db.DateTime)

    def __repr__(self):
        return f"{self.title} - {self.priority.value} - {self.status.value}"
