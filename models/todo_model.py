from datetime import datetime
from . import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(1000))
    created_date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.title} - {self.id}"
